from decouple import config
from flask_restful import Resource
from flask import request, url_for

from .models import Users


def build_url(url, args, new_page):
    if new_page:
        new_url = url.split("?")[0] + "?page={}".format(new_page)
        if "pagination" in args:
            return new_url + "&pagination={}".format(args["pagination"])

        if "order_by" in args:
            return new_url + "&order_by={}".format(args["order_by"])
        return new_url
    return ""


class UsersApi(Resource):
    model = Users
    page_size = config("PAGE_SIZE", cast=int, default=25)

    def get_queryset(self):
        queryset = self.model.query

        if request.args.get('username'):
            queryset = queryset.filter_by(username=request.args.get('username'))

        elif request.args.get('id'):
            queryset = queryset.filter_by(id=request.args.get('id'))

        elif request.args.get('order_by') and request.args.get('order_by') in ['type', 'id']:
            ordering = {"id": self.model._id, "type": self.model.type}
            queryset = queryset.order_by(ordering[request.args['order_by']])

        return queryset

    def paginate_response(self, queryset):
        page = request.args.get('page', default=1, type=int)
        limit = request.args.get('pagination', default=self.page_size, type=int)
        pag_queryset = queryset.paginate(page=page, per_page=limit)

        return {
            "count": pag_queryset.total,
            "prev_url": build_url(request.url, request.args, pag_queryset.prev_num),
            "next_url": build_url(request.url, request.args, pag_queryset.next_num),
            "result": [user.serialize() for user in pag_queryset.items]
        }

    def get(self):
        if any((request.args.get('username'), request.args.get('id'))):
            return self.get_queryset().first().serialize()
        return self.paginate_response(self.get_queryset())

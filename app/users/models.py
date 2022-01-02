from app.main import db


class Users(db.Model):
    __tablename__ = "github_users"
    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    username = db.Column(db.String(50))
    avatar_url = db.Column(db.Text)
    type = db.Column(db.String(50))
    URL = db.Column(db.Text)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar_url": self.avatar_url,
            "type": self.type,
            "URL": self.URL
        }
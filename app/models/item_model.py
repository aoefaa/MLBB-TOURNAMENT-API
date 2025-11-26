from app import db

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    image_url = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url
        }
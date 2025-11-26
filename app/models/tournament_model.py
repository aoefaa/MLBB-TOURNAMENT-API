from app import db

class Tournament(db.Model):
    __tablename__ = 'tournaments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    short_name = db.Column(db.String(20))
    logo_url = db.Column(db.String(255)) # URL Cloud Storage
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short_name": self.short_name,
            "logo_url": self.logo_url,
            "is_active": self.is_active
        }
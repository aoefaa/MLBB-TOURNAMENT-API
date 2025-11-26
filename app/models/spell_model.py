from app import db

class BattleSpell(db.Model):
    __tablename__ = 'battle_spells'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    image_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url
        }
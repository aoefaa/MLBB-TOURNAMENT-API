from app import db

class GameObjective(db.Model):
    __tablename__ = 'game_objectives'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    team_side = db.Column(db.String(10)) # 'blue' atau 'red'
    
    turret_kills = db.Column(db.Integer, default=0)
    turtle_kills = db.Column(db.Integer, default=0)
    lord_kills = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "team": self.team_side,
            "turret": self.turret_kills,
            "turtle": self.turtle_kills,
            "lord": self.lord_kills
        }
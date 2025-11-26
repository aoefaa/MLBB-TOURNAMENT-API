from app import db

class Draft(db.Model):
    __tablename__ = 'drafts'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    
    team_side = db.Column(db.String(10)) # 'blue' atau 'red'
    draft_type = db.Column(db.String(10)) # 'pick' atau 'ban'
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    
    ord = db.Column(db.Integer) 

    def to_dict(self):
        return {
            "team": self.team_side,
            "type": self.draft_type,
            "hero_id": self.hero_id,
            "order": self.ord
        }
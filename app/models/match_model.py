from app import db
from datetime import datetime

class Match(db.Model):
    __tablename__ = 'matches'
    
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
    
    team_a_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team_b_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    
    # Meta Data
    match_date = db.Column(db.DateTime, default=datetime.utcnow)
    stage = db.Column(db.String(50))
    format = db.Column(db.String(10), default='Bo3') # Bo1, Bo3, Bo5
    
    score_a = db.Column(db.Integer, default=0)
    score_b = db.Column(db.Integer, default=0)
    
    team_a = db.relationship('Team', foreign_keys=[team_a_id])
    team_b = db.relationship('Team', foreign_keys=[team_b_id])
    
    games = db.relationship('Game', backref='match', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "tournament_id": self.tournament_id,
            "team_a": self.team_a.to_dict() if self.team_a else None,
            "team_b": self.team_b.to_dict() if self.team_b else None,
            "score_a": self.score_a,
            "score_b": self.score_b,
            "stage": self.stage,
            "format": self.format
        }
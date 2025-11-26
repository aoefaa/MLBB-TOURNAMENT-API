from app import db

class Game(db.Model):
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    game_number = db.Column(db.Integer, nullable=False) # 1, 2, 3...
    
    winner_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    duration_seconds = db.Column(db.Integer, default=0) # Simpan dalam detik agar mudah dihitung
    
    drafts = db.relationship('Draft', backref='game', lazy=True, cascade="all, delete-orphan")
    players = db.relationship('GamePlayer', backref='game', lazy=True, cascade="all, delete-orphan")
    objectives = db.relationship('GameObjective', backref='game', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "match_id": self.match_id,
            "game_number": self.game_number,
            "duration": self.duration_seconds,
            "winner_team_id": self.winner_team_id
        }
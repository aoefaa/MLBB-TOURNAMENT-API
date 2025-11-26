from app import db
import json

class GamePlayer(db.Model):
    __tablename__ = 'game_players'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    
    # Identitas
    team_side = db.Column(db.String(10)) # 'blue' atau 'red'
    player_ign = db.Column(db.String(50))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=True)
    spell_id = db.Column(db.Integer, db.ForeignKey('battle_spells.id'), nullable=True)
    
    # Statistik (Realtime & Final)
    kills = db.Column(db.Integer, default=0)
    deaths = db.Column(db.Integer, default=0)
    assists = db.Column(db.Integer, default=0)
    gold = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    
    # Statistik Final (Result Screen Only)
    damage_dealt = db.Column(db.BigInteger, default=0)
    damage_taken = db.Column(db.BigInteger, default=0)
    turret_damage = db.Column(db.Integer, default=0)
    teamfight_part = db.Column(db.Integer, default=0) # 0-100
    
    items_json = db.Column(db.Text)
    
    def set_items(self, items_list):
        if not items_list: items_list = []
        self.items_json = json.dumps(items_list)
        
    def get_items(self):
        return json.loads(self.items_json) if self.items_json else []

    def to_dict(self):
        return {
            "ign": self.player_ign,
            "team": self.team_side,
            "hero_id": self.hero_id,
            "kda": f"{self.kills}/{self.deaths}/{self.assists}",
            "gold": self.gold,
            "items": self.get_items()
        }
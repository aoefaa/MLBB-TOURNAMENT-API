from flask import jsonify, request
from app import db
from app.models.game_objective_model import GameObjective

def get_by_game(game_id):
    """[READ] Ambil skor objektif (Turret/Lord/Turtle) kedua tim"""
    try:
        objs = GameObjective.query.filter_by(game_id=game_id).all()
        return jsonify({
            'status': 'success', 
            'data': [o.to_dict() for o in objs]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update_objective():
    """
    [CREATE/UPDATE] Update jumlah objektif tim.
    Payload: { "game_id": 1, "team": "blue", "turret": 2, "turtle": 1 }
    """
    data = request.get_json()
    game_id = data.get('game_id')
    team_side = data.get('team')
    
    try:
        obj = GameObjective.query.filter_by(
            game_id=game_id, 
            team_side=team_side
        ).first()
        
        if not obj:
            obj = GameObjective(game_id=game_id, team_side=team_side)
            db.session.add(obj)
            
        if 'turret' in data: obj.turret_kills = data['turret']
        if 'turtle' in data: obj.turtle_kills = data['turtle']
        if 'lord' in data: obj.lord_kills = data['lord']
        
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Objectives updated'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
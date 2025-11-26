from flask import jsonify, request
from app import db
from app.models.draft_model import Draft

def get_by_game(game_id):
    """
    [READ] Mengambil urutan draft untuk satu game.
    Digunakan oleh: Web Viewer (untuk replay draft).
    """
    try:
        drafts = Draft.query.filter_by(game_id=game_id).order_by(Draft.ord.asc()).all()
        return jsonify({
            'status': 'success', 
            'data': [d.to_dict() for d in drafts]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Menerima satu event Pick/Ban dari OCR.
    Payload: { "game_id": 1, "team": "blue", "type": "pick", "hero_id": 45, "ord": 1 }
    """
    data = request.get_json()
    
    if not data.get('game_id') or not data.get('hero_id'):
        return jsonify({'status': 'error', 'message': 'Game ID and Hero ID required'}), 400

    try:
        existing = Draft.query.filter_by(
            game_id=data.get('game_id'), 
            ord=data.get('ord')
        ).first()

        if existing:
            return jsonify({'status': 'ignored', 'message': 'Sequence already exists'}), 200

        new_draft = Draft(
            game_id=data.get('game_id'),
            team_side=data.get('team'),
            draft_type=data.get('type'),
            hero_id=data.get('hero_id'),
            ord=data.get('ord')
        )
        
        db.session.add(new_draft)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'data': new_draft.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """[DELETE] Koreksi manual jika OCR salah deteksi pick"""
    try:
        draft = Draft.query.get(id)
        if not draft: return jsonify({'message': 'Not found'}), 404
        db.session.delete(draft)
        db.session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
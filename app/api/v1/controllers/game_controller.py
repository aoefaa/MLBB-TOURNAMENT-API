from flask import jsonify, request
from app import db
from app.models.game_model import Game

def get_one(id):
    """
    [READ] Mengambil detail satu game.
    Termasuk data relasi (Drafts, Players) jika diakses lewat property model.
    """
    try:
        game = Game.query.get(id)
        if not game:
            return jsonify({'status': 'error', 'message': 'Game not found'}), 404
        
        return jsonify({
            'status': 'success', 
            'data': game.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Membuat Game Baru (Sesi).
    Digunakan oleh: Web Admin (Tombol "Start Game 1").
    """
    data = request.get_json()
    
    if not data.get('match_id') or not data.get('game_number'):
        return jsonify({'status': 'error', 'message': 'Match ID and Game Number required'}), 400

    try:
        new_game = Game(
            match_id=data.get('match_id'),
            game_number=data.get('game_number'),
            duration_seconds=0,
            winner_team_id=None
        )
        
        db.session.add(new_game)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Game created',
            'data': new_game.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE/FINALIZE] Mengupdate hasil game.
    Digunakan oleh: Web Admin (Manual) atau Script OCR Result (Auto).
    """
    data = request.get_json()
    
    try:
        game = Game.query.get(id)
        if not game:
            return jsonify({'status': 'error', 'message': 'Game not found'}), 404
            
        if 'duration' in data: game.duration_seconds = data['duration']
        if 'winner_team_id' in data: game.winner_team_id = data['winner_team_id']
        if 'game_number' in data: game.game_number = data['game_number']
        
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Game updated',
            'data': game.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Hapus Game.
    Warning: Akan menghapus semua data Draft & Stats OCR terkait (Cascade).
    """
    try:
        game = Game.query.get(id)
        if not game:
            return jsonify({'status': 'error', 'message': 'Game not found'}), 404
            
        db.session.delete(game)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Game deleted'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
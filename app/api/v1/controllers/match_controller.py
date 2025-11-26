from flask import jsonify, request
from app import db
from app.models.match_model import Match

def get_all():
    """
    [READ] Mengambil daftar match.
    Fitur: Bisa filter berdasarkan '?tournament_id=1'
    """
    tournament_id = request.args.get('tournament_id')
    
    try:
        if tournament_id:
            matches = Match.query.filter_by(tournament_id=tournament_id).all()
        else:
            matches = Match.query.all()
            
        return jsonify({
            'status': 'success', 
            'data': [m.to_dict() for m in matches]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def get_one(id):
    """
    [READ] Detail satu match beserta game di dalamnya.
    """
    try:
        match = Match.query.get(id)
        if not match:
            return jsonify({'status': 'error', 'message': 'Match not found'}), 404
        
        match_data = match.to_dict()
        match_data['games'] = [g.to_dict() for g in match.games]
        
        return jsonify({
            'status': 'success', 
            'data': match_data
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Membuat Jadwal Match Baru (Bo3/Bo5).
    """
    data = request.get_json()
    
    required_fields = ['tournament_id', 'team_a_id', 'team_b_id']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', 'message': f'{field} is required'}), 400

    try:
        new_match = Match(
            tournament_id=data.get('tournament_id'),
            team_a_id=data.get('team_a_id'),
            team_b_id=data.get('team_b_id'),
            stage=data.get('stage', 'Group Stage'),
            format=data.get('format', 'Bo3'),
            score_a=0,
            score_b=0
        )
        
        db.session.add(new_match)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Match created',
            'data': new_match.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE] Update info match (Skor Manual / Ganti Stage).
    """
    data = request.get_json()
    
    try:
        match = Match.query.get(id)
        if not match:
            return jsonify({'status': 'error', 'message': 'Match not found'}), 404
            
        if 'stage' in data: match.stage = data['stage']
        if 'format' in data: match.format = data['format']
        if 'score_a' in data: match.score_a = data['score_a']
        if 'score_b' in data: match.score_b = data['score_b']
        
        if 'team_a_id' in data: match.team_a_id = data['team_a_id']
        if 'team_b_id' in data: match.team_b_id = data['team_b_id']
        
        db.session.commit()
        return jsonify({
            'status': 'success', 
            'message': 'Match updated',
            'data': match.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Hapus Match. 
    Warning: Ini akan menghapus semua Game dan Stats di dalamnya (Cascade).
    """
    try:
        match = Match.query.get(id)
        if not match:
            return jsonify({'status': 'error', 'message': 'Match not found'}), 404
            
        db.session.delete(match)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Match deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
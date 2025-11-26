from flask import jsonify, request
from app import db
from app.models.team_model import Team

def get_all():
    """
    [READ] Mengambil daftar semua tim.
    Digunakan oleh: Web Admin (List & Dropdown di Form Match).
    """
    try:
        teams = Team.query.all()
        return jsonify({
            'status': 'success', 
            'data': [t.to_dict() for t in teams]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def get_one(id):
    """
    [READ] Mengambil detail satu tim.
    """
    try:
        team = Team.query.get(id)
        if not team:
            return jsonify({'status': 'error', 'message': 'Team not found'}), 404
        
        return jsonify({
            'status': 'success', 
            'data': team.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Mendaftarkan tim baru.
    """
    data = request.get_json()
    
    # Validasi wajib
    if not data.get('name'):
        return jsonify({'status': 'error', 'message': 'Team name is required'}), 400

    try:
        new_team = Team(
            name=data.get('name'),
            short_name=data.get('short_name'),
            logo_url=data.get('logo_url')
        )
        
        db.session.add(new_team)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Team created',
            'data': new_team.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE] Mengedit data tim.
    """
    data = request.get_json()
    
    try:
        team = Team.query.get(id)
        if not team:
            return jsonify({'status': 'error', 'message': 'Team not found'}), 404
            
        if 'name' in data: team.name = data['name']
        if 'short_name' in data: team.short_name = data['short_name']
        if 'logo_url' in data: team.logo_url = data['logo_url']
        
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Team updated',
            'data': team.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Menghapus tim.
    Note: Hati-hati, jika tim sudah pernah main (terikat di Match), 
    ini mungkin gagal jika tidak ada Cascade Delete atau validasi.
    """
    try:
        team = Team.query.get(id)
        if not team:
            return jsonify({'status': 'error', 'message': 'Team not found'}), 404
            
        db.session.delete(team)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Team deleted'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
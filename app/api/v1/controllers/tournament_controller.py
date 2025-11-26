from flask import jsonify, request
from app import db
from app.models.tournament_model import Tournament

def get_all():
    """
    [READ] Mengambil daftar semua turnamen.
    Digunakan oleh: Web Admin (List Page).
    """
    try:
        tournaments = Tournament.query.all()
        return jsonify({
            'status': 'success', 
            'data': [t.to_dict() for t in tournaments]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def get_one(id):
    """
    [READ] Mengambil detail satu turnamen.
    Digunakan oleh: Web Admin (Edit Page), Script OCR (Validasi).
    """
    try:
        tournament = Tournament.query.get(id)
        if not tournament:
            return jsonify({'status': 'error', 'message': 'Tournament not found'}), 404
        
        return jsonify({
            'status': 'success', 
            'data': tournament.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Membuat turnamen baru.
    Digunakan oleh: Web Admin.
    """
    data = request.get_json()
    
    if not data.get('name'):
        return jsonify({'status': 'error', 'message': 'Name is required'}), 400

    try:
        new_tournament = Tournament(
            name=data.get('name'),
            short_name=data.get('short_name'),
            logo_url=data.get('logo_url'),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(new_tournament)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Tournament created',
            'data': new_tournament.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE] Mengedit data turnamen.
    Digunakan oleh: Web Admin.
    """
    data = request.get_json()
    
    try:
        tournament = Tournament.query.get(id)
        if not tournament:
            return jsonify({'status': 'error', 'message': 'Tournament not found'}), 404
            
        if 'name' in data: tournament.name = data['name']
        if 'short_name' in data: tournament.short_name = data['short_name']
        if 'logo_url' in data: tournament.logo_url = data['logo_url']
        if 'is_active' in data: tournament.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Tournament updated',
            'data': tournament.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Menghapus turnamen.
    Digunakan oleh: Web Admin.
    """
    try:
        tournament = Tournament.query.get(id)
        if not tournament:
            return jsonify({'status': 'error', 'message': 'Tournament not found'}), 404
            
        db.session.delete(tournament)
        db.session.commit()
        
        return jsonify({
            'status': 'success', 
            'message': 'Tournament deleted'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
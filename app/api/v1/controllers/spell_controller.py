from flask import jsonify, request
from app import db
from app.models.spell_model import BattleSpell

def get_all():
    """
    [READ] Mengambil daftar semua battle spell.
    """
    try:
        spells = BattleSpell.query.all()
        return jsonify({
            'status': 'success', 
            'data': [s.to_dict() for s in spells]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Menambah spell baru.
    Payload: { "name": "Flicker", "image_url": "..." }
    """
    data = request.get_json()
    
    if not data.get('name'):
        return jsonify({'status': 'error', 'message': 'Name is required'}), 400

    try:
        new_spell = BattleSpell(
            name=data.get('name'),
            image_url=data.get('image_url')
        )
        db.session.add(new_spell)
        db.session.commit()
        return jsonify({'status': 'success', 'data': new_spell.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE] Edit data spell.
    """
    data = request.get_json()
    try:
        spell = BattleSpell.query.get(id)
        if not spell: return jsonify({'message': 'Not found'}), 404
        
        if 'name' in data: spell.name = data['name']
        if 'image_url' in data: spell.image_url = data['image_url']
        
        db.session.commit()
        return jsonify({'status': 'success', 'data': spell.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Hapus spell.
    """
    try:
        spell = BattleSpell.query.get(id)
        if not spell: return jsonify({'message': 'Not found'}), 404
        
        db.session.delete(spell)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
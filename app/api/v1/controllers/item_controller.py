from flask import jsonify, request
from app import db
from app.models.item_model import Item

def get_all():
    """
    [READ] Mengambil daftar semua item.
    """
    try:
        items = Item.query.all()
        return jsonify({
            'status': 'success', 
            'data': [i.to_dict() for i in items]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def create():
    """
    [CREATE] Menambah item baru.
    Payload: { "name": "Blade of Despair", "image_url": "..." }
    """
    data = request.get_json()
    
    if not data.get('name'):
        return jsonify({'status': 'error', 'message': 'Name is required'}), 400

    try:
        new_item = Item(
            name=data.get('name'),
            image_url=data.get('image_url')
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'status': 'success', 'data': new_item.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    """
    [UPDATE] Edit data item.
    """
    data = request.get_json()
    try:
        item = Item.query.get(id)
        if not item: return jsonify({'message': 'Not found'}), 404
        
        if 'name' in data: item.name = data['name']
        if 'image_url' in data: item.image_url = data['image_url']
        
        db.session.commit()
        return jsonify({'status': 'success', 'data': item.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """
    [DELETE] Hapus item.
    """
    try:
        item = Item.query.get(id)
        if not item: return jsonify({'message': 'Not found'}), 404
        
        db.session.delete(item)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500
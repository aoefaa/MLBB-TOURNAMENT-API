from flask import jsonify, request
from app import db
from app.models.hero_model import Hero

def get_all():
    heroes = Hero.query.all()
    return jsonify({'status': 'success', 'data': [h.to_dict() for h in heroes]}), 200

def create():
    data = request.get_json()
    try:
        new_hero = Hero(name=data.get('name'), image_url=data.get('image_url'))
        db.session.add(new_hero)
        db.session.commit()
        return jsonify({'status': 'success', 'data': new_hero.to_dict()}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update(id):
    data = request.get_json()
    hero = Hero.query.get(id)
    if not hero: return jsonify({'message': 'Not found'}), 404
    try:
        if 'name' in data: hero.name = data['name']
        if 'image_url' in data: hero.image_url = data['image_url']
        db.session.commit()
        return jsonify({'status': 'success', 'data': hero.to_dict()}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    hero = Hero.query.get(id)
    if not hero: return jsonify({'message': 'Not found'}), 404
    try:
        db.session.delete(hero)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Deleted'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
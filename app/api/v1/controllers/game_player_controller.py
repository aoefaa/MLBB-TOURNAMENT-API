from flask import jsonify, request
from app import db
from app.models.game_player_model import GamePlayer

def get_by_game(game_id):
    """[READ] Ambil statistik semua player di game tertentu"""
    try:
        players = GamePlayer.query.filter_by(game_id=game_id).all()
        return jsonify({
            'status': 'success', 
            'data': [p.to_dict() for p in players]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def update_stats():
    """
    [CREATE/UPDATE] Upsert Data Player.
    OCR akan menembak endpoint ini berkali-kali setiap detik/menit.
    """
    data = request.get_json()
    game_id = data.get('game_id')
    team_side = data.get('team')
    hero_id = data.get('hero_id')
    
    if not game_id or not hero_id:
        return jsonify({'status': 'error', 'message': 'Missing identifiers'}), 400

    try:
        player = GamePlayer.query.filter_by(
            game_id=game_id, 
            team_side=team_side, 
            hero_id=hero_id
        ).first()

        if not player:
            player = GamePlayer(
                game_id=game_id,
                team_side=team_side,
                hero_id=hero_id
            )
            db.session.add(player)

        # Update field yang dikirim saja (Partial Update)
        if 'ign' in data: player.player_ign = data['ign']
        if 'spell_id' in data: player.spell_id = data['spell_id']
        
        # Stats In-Game
        if 'kills' in data: player.kills = data['kills']
        if 'deaths' in data: player.deaths = data['deaths']
        if 'assists' in data: player.assists = data['assists']
        if 'gold' in data: player.gold = data['gold']
        if 'level' in data: player.level = data['level']
        
        # Items (List JSON)
        if 'items' in data: player.set_items(data['items'])
        
        # Result Stats (Final)
        if 'damage_dealt' in data: player.damage_dealt = data['damage_dealt']
        if 'damage_taken' in data: player.damage_taken = data['damage_taken']
        if 'turret_damage' in data: player.turret_damage = data['turret_damage']
        if 'teamfight_part' in data: player.teamfight_part = data['teamfight_part']

        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Stats updated'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

def delete(id):
    """[DELETE] Hapus data player (jika OCR mendeteksi hantu/glitch)"""
    try:
        player = GamePlayer.query.get(id)
        if player:
            db.session.delete(player)
            db.session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
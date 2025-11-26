from flask import Blueprint
from app.api.v1.controllers import game_player_controller

# URL Prefix: /api/v1/game_players
game_player_bp = Blueprint('game_player', __name__, url_prefix='/api/v1/game_players')

# --- Mapping URL ke Controller ---

# POST /api/v1/game_players -> Upsert Stats Player
game_player_bp.route('', methods=['POST'])(game_player_controller.update_stats)

# GET /api/v1/game_players/game/<game_id> -> Ambil semua stats player di game tertentu
game_player_bp.route('/game/<int:game_id>', methods=['GET'])(game_player_controller.get_by_game)

# DELETE /api/v1/game_players/<id> -> Hapus data player (Koreksi Manual)
game_player_bp.route('/<int:id>', methods=['DELETE'])(game_player_controller.delete)

from flask import Blueprint
from app.api.v1.controllers import game_controller

# URL Prefix: /api/v1/games
game_bp = Blueprint('game', __name__, url_prefix='/api/v1/games')

# --- Mapping URL ke Controller ---

# POST /api/v1/games -> Buat Game Baru (Game 1, Game 2)
game_bp.route('', methods=['POST'])(game_controller.create)

# GET /api/v1/games/<id> -> Ambil detail game
game_bp.route('/<int:id>', methods=['GET'])(game_controller.get_one)

# PUT /api/v1/games/<id> -> Finalize Game (Simpan Pemenang & Durasi)
game_bp.route('/<int:id>', methods=['PUT'])(game_controller.update)

# DELETE /api/v1/games/<id> -> Hapus Game (Reset)
game_bp.route('/<int:id>', methods=['DELETE'])(game_controller.delete)
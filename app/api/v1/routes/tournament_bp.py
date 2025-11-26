from flask import Blueprint
from app.api.v1.controllers import tournament_controller

# URL Prefix: /api/v1/tournaments
tournament_bp = Blueprint('tournament', __name__, url_prefix='/api/v1/tournaments')

# --- Mapping URL ke Controller ---

# GET /api/v1/tournaments -> Ambil semua list
tournament_bp.route('', methods=['GET'])(tournament_controller.get_all)

# POST /api/v1/tournaments -> Buat baru
tournament_bp.route('', methods=['POST'])(tournament_controller.create)

# GET /api/v1/tournaments/<id> -> Ambil detail
tournament_bp.route('/<int:id>', methods=['GET'])(tournament_controller.get_one)

# PUT /api/v1/tournaments/<id> -> Update
tournament_bp.route('/<int:id>', methods=['PUT'])(tournament_controller.update)

# DELETE /api/v1/tournaments/<id> -> Hapus
tournament_bp.route('/<int:id>', methods=['DELETE'])(tournament_controller.delete)
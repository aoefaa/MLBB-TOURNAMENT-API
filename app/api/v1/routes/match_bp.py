from flask import Blueprint
from app.api.v1.controllers import match_controller

# URL Prefix: /api/v1/matches
match_bp = Blueprint('match', __name__, url_prefix='/api/v1/matches')

# --- Mapping URL ke Controller ---

# GET /api/v1/matches -> Ambil semua match
match_bp.route('', methods=['GET'])(match_controller.get_all)

# POST /api/v1/matches -> Buat jadwal match baru
match_bp.route('', methods=['POST'])(match_controller.create)

# GET /api/v1/matches/<id> -> Ambil detail match (termasuk list games)
match_bp.route('/<int:id>', methods=['GET'])(match_controller.get_one)

# PUT /api/v1/matches/<id> -> Update skor/stage manual
match_bp.route('/<int:id>', methods=['PUT'])(match_controller.update)

# DELETE /api/v1/matches/<id> -> Hapus match
match_bp.route('/<int:id>', methods=['DELETE'])(match_controller.delete)
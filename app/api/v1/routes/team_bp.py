from flask import Blueprint
from app.api.v1.controllers import team_controller

# URL Prefix: /api/v1/teams
team_bp = Blueprint('team', __name__, url_prefix='/api/v1/teams')

# --- Mapping URL ke Controller ---

# GET /api/v1/teams -> Ambil semua list tim
team_bp.route('', methods=['GET'])(team_controller.get_all)

# POST /api/v1/teams -> Tambah tim baru
team_bp.route('', methods=['POST'])(team_controller.create)

# GET /api/v1/teams/<id> -> Ambil detail tim
team_bp.route('/<int:id>', methods=['GET'])(team_controller.get_one)

# PUT /api/v1/teams/<id> -> Update data tim
team_bp.route('/<int:id>', methods=['PUT'])(team_controller.update)

# DELETE /api/v1/teams/<id> -> Hapus tim
team_bp.route('/<int:id>', methods=['DELETE'])(team_controller.delete)
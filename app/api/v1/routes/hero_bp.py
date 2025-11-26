from flask import Blueprint
from app.api.v1.controllers import hero_controller

# URL Prefix: /api/v1/heroes
hero_bp = Blueprint('hero', __name__, url_prefix='/api/v1/heroes')

# --- Mapping URL ke Controller ---

# GET /api/v1/heroes -> Ambil semua daftar hero
hero_bp.route('', methods=['GET'])(hero_controller.get_all)

# POST /api/v1/heroes -> Tambah hero baru
hero_bp.route('', methods=['POST'])(hero_controller.create)

# PUT /api/v1/heroes/<id> -> Edit hero (misal update icon URL)
hero_bp.route('/<int:id>', methods=['PUT'])(hero_controller.update)

# DELETE /api/v1/heroes/<id> -> Hapus hero
hero_bp.route('/<int:id>', methods=['DELETE'])(hero_controller.delete)
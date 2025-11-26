from flask import Blueprint
from app.api.v1.controllers import spell_controller

# URL Prefix: /api/v1/spells
spell_bp = Blueprint('spell', __name__, url_prefix='/api/v1/spells')

# --- Mapping URL ke Controller ---

# GET /api/v1/spells -> Ambil semua daftar spell
spell_bp.route('', methods=['GET'])(spell_controller.get_all)

# POST /api/v1/spells -> Tambah spell baru
spell_bp.route('', methods=['POST'])(spell_controller.create)

# PUT /api/v1/spells/<id> -> Edit spell
spell_bp.route('/<int:id>', methods=['PUT'])(spell_controller.update)

# DELETE /api/v1/spells/<id> -> Hapus spell
spell_bp.route('/<int:id>', methods=['DELETE'])(spell_controller.delete)
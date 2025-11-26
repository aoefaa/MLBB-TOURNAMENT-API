from flask import Blueprint
from app.api.v1.controllers import item_controller

# URL Prefix: /api/v1/items
item_bp = Blueprint('item', __name__, url_prefix='/api/v1/items')

# --- Mapping URL ke Controller ---

# GET /api/v1/items -> Ambil semua daftar item
item_bp.route('', methods=['GET'])(item_controller.get_all)

# POST /api/v1/items -> Tambah item baru
item_bp.route('', methods=['POST'])(item_controller.create)

# PUT /api/v1/items/<id> -> Edit item
item_bp.route('/<int:id>', methods=['PUT'])(item_controller.update)

# DELETE /api/v1/items/<id> -> Hapus item
item_bp.route('/<int:id>', methods=['DELETE'])(item_controller.delete)
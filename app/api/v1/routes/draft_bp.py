from flask import Blueprint
from app.api.v1.controllers import draft_controller

# URL Prefix: /api/v1/drafts
draft_bp = Blueprint('draft', __name__, url_prefix='/api/v1/drafts')

# --- Mapping URL ke Controller ---

# POST /api/v1/drafts -> Terima data Pick/Ban dari OCR
draft_bp.route('', methods=['POST'])(draft_controller.create)

# GET /api/v1/drafts/game/<game_id> -> Ambil history draft satu game
draft_bp.route('/game/<int:game_id>', methods=['GET'])(draft_controller.get_by_game)

# DELETE /api/v1/drafts/<id> -> Hapus entry draft (Koreksi Manual)
draft_bp.route('/<int:id>', methods=['DELETE'])(draft_controller.delete)
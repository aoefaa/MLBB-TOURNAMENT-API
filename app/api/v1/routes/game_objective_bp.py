from flask import Blueprint
from app.api.v1.controllers import game_objective_controller

# URL Prefix: /api/v1/game_objectives
game_objective_bp = Blueprint('game_objective', __name__, url_prefix='/api/v1/game_objectives')

# --- Mapping URL ke Controller ---

# POST /api/v1/game_objectives -> Update jumlah Turret/Lord/Turtle
game_objective_bp.route('', methods=['POST'])(game_objective_controller.update_objective)

# GET /api/v1/game_objectives/game/<game_id> -> Ambil skor objektif game tertentu
game_objective_bp.route('/game/<int:game_id>', methods=['GET'])(game_objective_controller.get_by_game)
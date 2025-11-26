from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Pastikan Anda punya file config.py

# Inisialisasi Ekstensi
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init Ekstensi dengan App
    db.init_app(app)
    migrate.init_app(app, db)

    # --- REGISTRASI BLUEPRINTS ---
    
    # 1. Master Data Routes
    from app.api.v1.routes.hero_bp import hero_bp
    from app.api.v1.routes.item_bp import item_bp
    from app.api.v1.routes.spell_bp import spell_bp
    
    app.register_blueprint(hero_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(spell_bp)

    # 2. Admin Data Routes (Tournament & Team)
    from app.api.v1.routes.tournament_bp import tournament_bp
    from app.api.v1.routes.team_bp import team_bp
    
    app.register_blueprint(tournament_bp)
    app.register_blueprint(team_bp)

    # 3. Session Data Routes (Match & Game)
    from app.api.v1.routes.match_bp import match_bp
    from app.api.v1.routes.game_bp import game_bp
    
    app.register_blueprint(match_bp)
    app.register_blueprint(game_bp)

    # 4. OCR Transaction Routes (Draft, Stats, Objective)
    from app.api.v1.routes.draft_bp import draft_bp
    from app.api.v1.routes.game_player_bp import game_player_bp
    from app.api.v1.routes.game_objective_bp import game_objective_bp
    
    app.register_blueprint(draft_bp)
    app.register_blueprint(game_player_bp)
    app.register_blueprint(game_objective_bp)

    return app
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Install PyMySQL as MySQLdb to avoid 'ModuleNotFoundError'
pymysql.install_as_MySQLdb()

# Inisialisasi objek db dan migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()  # Load variabel lingkungan dari .env file

    # Membuat objek Flask
    app = Flask(__name__)

    # Konfigurasi URI database MySQL (gunakan MySQLdb atau PyMySQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/karyawaan'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object("app.config.Config")

    # Inisialisasi db dan migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Mendaftarkan blueprint untuk routing
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Impor routes setelah inisialisasi db dan blueprint
    from app import routes
    
    return app

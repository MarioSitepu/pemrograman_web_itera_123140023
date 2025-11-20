"""
Entry point untuk menjalankan aplikasi Pyramid.
"""
from waitress import serve
from pyramid.paster import get_appsettings
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import os
import sys

# Tambahkan current directory ke path
sys.path.insert(0, os.path.dirname(__file__))

from models import Base, DBSession
from routes import includeme as include_routes


def get_app():
    """
    Membuat dan mengembalikan WSGI application.
    """
    # Baca settings dari development.ini
    config_file = os.path.join(os.path.dirname(__file__), 'development.ini')
    settings = get_appsettings(config_file)
    
    # Konfigurasi database engine
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    # Buat configurator
    config = Configurator(settings=settings)
    
    # Include SQLAlchemy
    config.include('pyramid_sqlalchemy')
    
    # Include routes
    include_routes(config)
    
    # Scan untuk views
    config.scan('views')
    
    return config.make_wsgi_app()


if __name__ == '__main__':
    # Dapatkan WSGI application
    app = get_app()
    
    # Jalankan server dengan Waitress
    print("Server berjalan di http://localhost:6543")
    print("Tekan Ctrl+C untuk menghentikan server")
    serve(app, host='0.0.0.0', port=6543)

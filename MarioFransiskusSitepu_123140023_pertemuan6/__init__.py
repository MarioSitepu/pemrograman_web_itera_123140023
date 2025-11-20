"""
Aplikasi Manajemen Matakuliah dengan Pyramid Framework.
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from models import Base, DBSession


def main(global_config, **settings):
    """
    Fungsi utama untuk membuat dan mengkonfigurasi aplikasi Pyramid.
    
    Args:
        global_config: Konfigurasi global Pyramid
        **settings: Dictionary berisi settings aplikasi
        
    Returns:
        WSGI application
    """
    # Konfigurasi database engine
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    # Buat configurator
    config = Configurator(settings=settings)
    
    # Include SQLAlchemy
    config.include('pyramid_sqlalchemy')
    
    # Include routes
    config.include('routes')
    
    # Scan untuk views
    config.scan('views')
    
    return config.make_wsgi_app()


"""
Script untuk inisialisasi database dan menambahkan data awal.
"""
from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging
import os
import sys

# Tambahkan path ke sys.path
sys.path.insert(0, os.path.dirname(__file__))

from models import Base, DBSession, Matakuliah


def initialize_database():
    """
    Inisialisasi database dan menambahkan data awal.
    """
    # Baca konfigurasi dari development.ini
    config_file = os.path.join(os.path.dirname(__file__), 'development.ini')
    settings = get_appsettings(config_file)
    
    # Buat engine
    engine = engine_from_config(settings, 'sqlalchemy.')
    
    # Buat semua tabel
    Base.metadata.create_all(engine)
    
    # Konfigurasi session
    DBSession.configure(bind=engine)
    
    # Data awal matakuliah
    sample_data = [
        {
            'kode_mk': 'IF101',
            'nama_mk': 'Algoritma dan Pemrograman',
            'sks': 3,
            'semester': 1
        },
        {
            'kode_mk': 'IF102',
            'nama_mk': 'Struktur Data',
            'sks': 3,
            'semester': 2
        },
        {
            'kode_mk': 'IF201',
            'nama_mk': 'Pemrograman Web',
            'sks': 3,
            'semester': 3
        }
    ]
    
    # Cek apakah data sudah ada
    existing_count = DBSession.query(Matakuliah).count()
    
    if existing_count == 0:
        # Tambahkan data awal
        for data in sample_data:
            matakuliah = Matakuliah(**data)
            DBSession.add(matakuliah)
        
        DBSession.commit()
        print(f"✓ Database berhasil diinisialisasi")
        print(f"✓ {len(sample_data)} data matakuliah berhasil ditambahkan")
    else:
        print(f"✓ Database sudah berisi {existing_count} data matakuliah")
        print("✓ Tidak perlu menambahkan data awal")


if __name__ == '__main__':
    try:
        initialize_database()
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


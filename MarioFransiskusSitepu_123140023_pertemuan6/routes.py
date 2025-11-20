"""
Konfigurasi routes untuk aplikasi manajemen matakuliah.
"""
from pyramid.config import Configurator


def includeme(config: Configurator):
    """
    Fungsi untuk menambahkan routes ke configurator.
    
    Args:
        config: Pyramid Configurator instance
    """
    # Route untuk mendapatkan semua matakuliah
    config.add_route('get_all_matakuliah', '/api/matakuliah', request_method='GET')
    
    # Route untuk mendapatkan satu matakuliah berdasarkan ID
    config.add_route('get_matakuliah', '/api/matakuliah/{id}', request_method='GET')
    
    # Route untuk menambahkan matakuliah baru
    config.add_route('create_matakuliah', '/api/matakuliah', request_method='POST')
    
    # Route untuk mengupdate matakuliah
    config.add_route('update_matakuliah', '/api/matakuliah/{id}', request_method='PUT')
    
    # Route untuk menghapus matakuliah
    config.add_route('delete_matakuliah', '/api/matakuliah/{id}', request_method='DELETE')


"""
Views untuk API endpoints manajemen matakuliah.
"""
from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError
from models import DBSession, Matakuliah


@view_config(route_name='get_all_matakuliah', renderer='json')
def get_all_matakuliah(request):
    """
    Endpoint untuk mendapatkan semua matakuliah.
    
    Returns:
        JSON response berisi list semua matakuliah
    """
    try:
        matakuliahs = DBSession.query(Matakuliah).all()
        return {
            'matakuliahs': [mk.to_dict() for mk in matakuliahs]
        }
    except Exception as e:
        request.response.status_code = 500
        return {
            'error': 'Gagal mengambil data matakuliah',
            'message': str(e)
        }


@view_config(route_name='get_matakuliah', renderer='json')
def get_matakuliah(request):
    """
    Endpoint untuk mendapatkan detail satu matakuliah berdasarkan ID.
    
    Args:
        request: Pyramid request object dengan parameter 'id'
        
    Returns:
        JSON response berisi data matakuliah atau error jika tidak ditemukan
    """
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if matakuliah:
            return matakuliah.to_dict()
        else:
            request.response.status_code = 404
            return {
                'error': 'Matakuliah tidak ditemukan',
                'message': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'
            }
    except ValueError:
        request.response.status_code = 400
        return {
            'error': 'ID tidak valid',
            'message': 'ID harus berupa angka'
        }
    except Exception as e:
        request.response.status_code = 500
        return {
            'error': 'Gagal mengambil data matakuliah',
            'message': str(e)
        }


@view_config(route_name='create_matakuliah', renderer='json')
def create_matakuliah(request):
    """
    Endpoint untuk menambahkan matakuliah baru.
    
    Args:
        request: Pyramid request object dengan JSON body berisi data matakuliah
        
    Returns:
        JSON response berisi data matakuliah yang baru dibuat atau error
    """
    try:
        # Parse JSON body
        data = request.json_body
        
        # Validasi field yang diperlukan
        required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in required_fields:
            if field not in data:
                request.response.status_code = 400
                return {
                    'error': 'Field tidak lengkap',
                    'message': f'Field {field} harus diisi'
                }
        
        # Validasi tipe data
        if not isinstance(data['kode_mk'], str) or not data['kode_mk'].strip():
            request.response.status_code = 400
            return {
                'error': 'Data tidak valid',
                'message': 'kode_mk harus berupa string yang tidak kosong'
            }
        
        if not isinstance(data['nama_mk'], str) or not data['nama_mk'].strip():
            request.response.status_code = 400
            return {
                'error': 'Data tidak valid',
                'message': 'nama_mk harus berupa string yang tidak kosong'
            }
        
        try:
            sks = int(data['sks'])
            semester = int(data['semester'])
        except (ValueError, TypeError):
            request.response.status_code = 400
            return {
                'error': 'Data tidak valid',
                'message': 'sks dan semester harus berupa angka'
            }
        
        # Buat matakuliah baru
        matakuliah = Matakuliah(
            kode_mk=data['kode_mk'].strip(),
            nama_mk=data['nama_mk'].strip(),
            sks=sks,
            semester=semester
        )
        
        DBSession.add(matakuliah)
        DBSession.flush()
        
        request.response.status_code = 201
        return matakuliah.to_dict()
        
    except IntegrityError:
        DBSession.rollback()
        request.response.status_code = 400
        return {
            'error': 'Data duplikat',
            'message': 'Kode mata kuliah sudah ada'
        }
    except Exception as e:
        DBSession.rollback()
        request.response.status_code = 500
        return {
            'error': 'Gagal menambahkan matakuliah',
            'message': str(e)
        }


@view_config(route_name='update_matakuliah', renderer='json')
def update_matakuliah(request):
    """
    Endpoint untuk mengupdate data matakuliah.
    
    Args:
        request: Pyramid request object dengan parameter 'id' dan JSON body
        
    Returns:
        JSON response berisi data matakuliah yang telah diupdate atau error
    """
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if not matakuliah:
            request.response.status_code = 404
            return {
                'error': 'Matakuliah tidak ditemukan',
                'message': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'
            }
        
        # Parse JSON body
        data = request.json_body
        
        # Update field yang ada di request
        if 'kode_mk' in data:
            if not isinstance(data['kode_mk'], str) or not data['kode_mk'].strip():
                request.response.status_code = 400
                return {
                    'error': 'Data tidak valid',
                    'message': 'kode_mk harus berupa string yang tidak kosong'
                }
            matakuliah.kode_mk = data['kode_mk'].strip()
        
        if 'nama_mk' in data:
            if not isinstance(data['nama_mk'], str) or not data['nama_mk'].strip():
                request.response.status_code = 400
                return {
                    'error': 'Data tidak valid',
                    'message': 'nama_mk harus berupa string yang tidak kosong'
                }
            matakuliah.nama_mk = data['nama_mk'].strip()
        
        if 'sks' in data:
            try:
                matakuliah.sks = int(data['sks'])
            except (ValueError, TypeError):
                request.response.status_code = 400
                return {
                    'error': 'Data tidak valid',
                    'message': 'sks harus berupa angka'
                }
        
        if 'semester' in data:
            try:
                matakuliah.semester = int(data['semester'])
            except (ValueError, TypeError):
                request.response.status_code = 400
                return {
                    'error': 'Data tidak valid',
                    'message': 'semester harus berupa angka'
                }
        
        DBSession.flush()
        
        return matakuliah.to_dict()
        
    except ValueError:
        request.response.status_code = 400
        return {
            'error': 'ID tidak valid',
            'message': 'ID harus berupa angka'
        }
    except IntegrityError:
        DBSession.rollback()
        request.response.status_code = 400
        return {
            'error': 'Data duplikat',
            'message': 'Kode mata kuliah sudah ada'
        }
    except Exception as e:
        DBSession.rollback()
        request.response.status_code = 500
        return {
            'error': 'Gagal mengupdate matakuliah',
            'message': str(e)
        }


@view_config(route_name='delete_matakuliah', renderer='json')
def delete_matakuliah(request):
    """
    Endpoint untuk menghapus matakuliah.
    
    Args:
        request: Pyramid request object dengan parameter 'id'
        
    Returns:
        JSON response berisi pesan sukses atau error
    """
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if not matakuliah:
            request.response.status_code = 404
            return {
                'error': 'Matakuliah tidak ditemukan',
                'message': f'Matakuliah dengan ID {matakuliah_id} tidak ditemukan'
            }
        
        DBSession.delete(matakuliah)
        DBSession.flush()
        
        return {
            'message': 'Matakuliah berhasil dihapus',
            'id': matakuliah_id
        }
        
    except ValueError:
        request.response.status_code = 400
        return {
            'error': 'ID tidak valid',
            'message': 'ID harus berupa angka'
        }
    except Exception as e:
        DBSession.rollback()
        request.response.status_code = 500
        return {
            'error': 'Gagal menghapus matakuliah',
            'message': str(e)
        }


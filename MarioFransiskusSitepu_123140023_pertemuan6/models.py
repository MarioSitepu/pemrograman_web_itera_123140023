"""
Model data untuk aplikasi manajemen matakuliah.
"""
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
DBSession = scoped_session(sessionmaker())


class Matakuliah(Base):
    """
    Model Matakuliah untuk menyimpan data mata kuliah.
    
    Attributes:
        id (Integer): Primary key, auto increment
        kode_mk (Text): Kode mata kuliah, unique, not null
        nama_mk (Text): Nama mata kuliah, not null
        sks (Integer): Jumlah SKS, not null
        semester (Integer): Semester pengambilan, not null
    """
    __tablename__ = 'matakuliah'

    id = Column(Integer, primary_key=True)
    kode_mk = Column(Text, unique=True, nullable=False)
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        """
        Mengkonversi objek Matakuliah menjadi dictionary.
        
        Returns:
            dict: Dictionary berisi data matakuliah
        """
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester,
        }


"""
Setup file untuk aplikasi Pyramid.
"""
from setuptools import setup, find_packages

requires = [
    'pyramid==2.0.2',
    'pyramid-sqlalchemy==0.1',
    'SQLAlchemy==2.0.23',
    'alembic==1.12.1',
    'waitress==2.1.2',
    'python-dateutil==2.8.2',
]

setup(
    name='manajemen_matakuliah',
    version='1.0',
    description='Aplikasi Manajemen Matakuliah dengan Pyramid',
    author='Mario Fransiskus Sitepu',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = manajemen_matakuliah:main',
        ],
    },
)


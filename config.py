import os

class Config:
    # Ganti 'DATABASE_URI' dengan path yang sesuai ke database 'karyawaan'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/karyawaan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'hendrisayang banged')  # Ganti dengan kunci rahasia yang sesuai

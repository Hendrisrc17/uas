from app import db

class Karyawan(db.Model):
    __tablename__ = 'karyawan'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    nomor_telepon = db.Column(db.String(15), nullable=False, unique=True)
    jabatan = db.Column(db.String(50), nullable=False)
    keahlian = db.Column(db.String(100), nullable=True)
    gaji = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Karyawan {self.username}>"

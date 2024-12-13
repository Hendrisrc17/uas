from flask import Flask
from flask.cli import with_appcontext
import click
from app import db
from app.models import Karyawan
import random
from app import create_app

# Fungsi untuk menghasilkan nomor telepon acak
def generate_phone_number():
    return f"08{random.randint(10000000, 99999999)}"

# Fungsi untuk menghasilkan usia acak
def generate_age():
    return random.randint(22, 35)

# Fungsi untuk menghasilkan data karyawan acak
def create_random_karyawan(nama):
    pekerjaan_list = ['Developer', 'Designer', 'Manager', 'Tester', 'System Analyst']
    lulusan_list = ['S1 Informatika', 'S1 Desain Komunikasi Visual', 'S1 Manajemen', 'S1 Teknik Industri', 'S1 Sistem Informasi']

    username = nama
    email = f"{nama.lower()}@example.com"
    nomor_telepon = generate_phone_number()
    jabatan = random.choice(pekerjaan_list)
    keahlian = random.choice(lulusan_list)
    gaji = round(random.uniform(5000000, 15000000), 2)

    return Karyawan(
        username=username,
        email=email,
        nomor_telepon=nomor_telepon,
        jabatan=jabatan,
        keahlian=keahlian,
        gaji=gaji
    )

app = create_app()

@app.cli.command('seed')
@with_appcontext
def seed_data():
    """Seed the database with random karyawan data."""
    # Daftar nama-nama yang akan digunakan untuk seeding
    nama_tertentu = ['hendri', 'nadia', 'yilita', 'amanda', 'idris']
    nama_acak = [
        'casey_jones', 'luke_skywalker', 'michael_scott', 'jim_halpert', 'sara_connor',
        'john_doe', 'alice_williams', 'bob_jones', 'claire_bennett', 'daniel_radcliffe',
        'emma_watson', 'jack_sparrow', 'tony_stark', 'peter_parker', 'bruce_wayne',
        'clark_kent', 'natasha_romanoff', 'wanda_maximoff', 'harley_quinn', 'vito_corleone'
    ]

    with app.app_context():
        # Menghapus data karyawan yang sudah ada
        db.session.query(Karyawan).delete()

        # Menambahkan data karyawan dari nama tertentu
        for nama in nama_tertentu:
            karyawan = create_random_karyawan(nama)
            db.session.add(karyawan)

        # Menambahkan 20 data karyawan acak
        for nama in nama_acak:
            karyawan = create_random_karyawan(nama)
            db.session.add(karyawan)

        # Commit perubahan ke database
        try:
            db.session.commit()
            print("Data berhasil ditambahkan ke tabel karyawan!")
        except Exception as e:
            db.session.rollback()
            print(f"Gagal menyimpan data: {str(e)}")

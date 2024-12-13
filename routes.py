from flask import Blueprint, jsonify, request
from app.models import Karyawan, db

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({'message': 'Selamat datang sayang ini hendri admin dari project ujian akhir'})

# GET all karyawan
@bp.route('/karyawan', methods=['GET'])
def get_karyawan():
    karyawans = Karyawan.query.all()
    return jsonify([{
        'id': karyawan.id,
        'username': karyawan.username,
        'email': karyawan.email,
        'nomor_telepon': karyawan.nomor_telepon,
        'jabatan': karyawan.jabatan,
        'keahlian': karyawan.keahlian,
        'gaji': karyawan.gaji
    } for karyawan in karyawans])

# GET karyawan by ID
@bp.route('/karyawan/<int:id>', methods=['GET'])
def get_karyawan_by_id(id):
    karyawan = Karyawan.query.get(id)
    if karyawan:
        return jsonify({
            'id': karyawan.id,
            'username': karyawan.username,
            'email': karyawan.email,
            'nomor_telepon': karyawan.nomor_telepon,
            'jabatan': karyawan.jabatan,
            'keahlian': karyawan.keahlian,
            'gaji': karyawan.gaji
        })
    else:
        return jsonify({'message': 'Karyawan not found'}), 404

# POST new karyawan
@bp.route('/karyawan', methods=['POST'])
def add_karyawan():
    try:
        data = request.get_json()
        
        # Validate if the necessary fields are provided
        if not all(key in data for key in ['username', 'email', 'nomor_telepon', 'jabatan', 'gaji']):
            return jsonify({'message': 'Missing required fields'}), 400
        
        # Create a new Karyawan object
        new_karyawan = Karyawan(
            username=data['username'],
            email=data['email'],
            nomor_telepon=data['nomor_telepon'],
            jabatan=data['jabatan'],
            keahlian=data.get('keahlian'),  # Optional
            gaji=data['gaji']
        )

        # Add the new Karyawan to the session and commit to the database
        db.session.add(new_karyawan)
        db.session.commit()
        
        return jsonify({'message': 'aww, kamu pintar sayang karyawaan perusahaan sudah di tambah'}), 201

    except Exception as e:
        # Log the error and return a more meaningful message
        print(f"Error: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# PUT (update) karyawan
@bp.route('/karyawan/<int:id>', methods=['PUT'])
def update_karyawan(id):
    karyawan = Karyawan.query.get(id)
    if not karyawan:
        return jsonify({'message': 'Karyawan not found'}), 404

    try:
        data = request.get_json()
        
        # Cek apakah email atau nomor telepon sudah digunakan
        if 'email' in data and data['email'] != karyawan.email:
            if Karyawan.query.filter_by(email=data['email']).first():
                return jsonify({'message': 'Email already exists'}), 400

        if 'nomor_telepon' in data and data['nomor_telepon'] != karyawan.nomor_telepon:
            if Karyawan.query.filter_by(nomor_telepon=data['nomor_telepon']).first():
                return jsonify({'message': 'Nomor telepon already exists'}), 400

        # Update data karyawan
        karyawan.username = data.get('username', karyawan.username)
        karyawan.email = data.get('email', karyawan.email)
        karyawan.nomor_telepon = data.get('nomor_telepon', karyawan.nomor_telepon)
        karyawan.jabatan = data.get('jabatan', karyawan.jabatan)
        karyawan.keahlian = data.get('keahlian', karyawan.keahlian)
        karyawan.gaji = data.get('gaji', karyawan.gaji)

        db.session.commit()
        return jsonify({'message': 'mengubah identitas karyawaan sukses'})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500


# DELETE karyawan
@bp.route('/karyawan/<int:id>', methods=['DELETE'])
def delete_karyawan(id):
    karyawan = Karyawan.query.get(id)
    if not karyawan:
        return jsonify({'message': 'Karyawan not found'}), 404

    db.session.delete(karyawan)
    db.session.commit()
    return jsonify({'message': 'menghapus karyawaan melanggar peraturan sukses'})

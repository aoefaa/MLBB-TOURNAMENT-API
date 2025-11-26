# 🏆 MLBB Tournament API

> **Cloud-Native Backend Microservice** untuk Ekosistem Turnamen Mobile Legends: Bang Bang.

Project ini berfungsi sebagai **Pusat Data (API Layer)** yang sepenuhnya ter-hosting di cloud. Layanan ini bersifat "Headless" dan bertanggung jawab untuk mengelola transaksi database, memvalidasi data game, serta menyimpan aset gambar menggunakan layanan eksternal.

## 🏗 Arsitektur & Infrastruktur

Layanan ini dirancang agar **Stateless** (tidak menyimpan data di server aplikasi), sehingga aman untuk di-deploy di platform serverless atau container (Docker).

  * **Database:** Menggunakan **Filess.io** (MySQL 8.0) untuk penyimpanan data relasional.
  * **Storage:** Menggunakan **Cloudinary** untuk penyimpanan aset gambar (Hero icons, Team logos).
  * **Compute:** API Service berbasis Python Flask.

## 🌟 Fitur Utama

  * **Fully Cloud Native:** Tidak ada penyimpanan file lokal (assets) dan tidak ada database lokal. Siap deploy kapan saja.
  * **API Versioning (v1):** Struktur API yang terorganisir dan terisolasi untuk stabilitas jangka panjang.
  * **Granular Architecture:** Pemisahan kode yang tegas berdasarkan entitas tabel (Models, Controllers, Routes terpisah).
  * **Real-time Ingestion:** Endpoint khusus untuk menerima stream data dari OCR (Draft, KDA, Gold, Turret).
  * **Master Data Management:** Pengelolaan terpusat untuk Hero, Item, Spell, Tim, dan Turnamen.

## 🛠 Tech Stack

  * **Core:** Python 3.9+
  * **Framework:** Flask (Blueprints Pattern)
  * **Database Driver:** PyMySQL (`mysql+pymysql://`)
  * **ORM:** Flask-SQLAlchemy
  * **Migration:** Flask-Migrate
  * **Asset Storage:** Cloudinary SDK

## 📂 Struktur Project

```text
MLBB-TOURNAMENT-API/
├── app/
│   ├── __init__.py           # App Factory
│   ├── utils/                # Storage Client (Cloudinary Wrapper)
│   │
│   ├── models/               # [Global Database Models]
│   │   ├── tournament_model.py
│   │   ├── game_model.py
│   │   └── ... (Representasi Tabel Database)
│   │
│   └── api/
│       └── v1/               # [API Version 1 Interface]
│           ├── controllers/  # Business Logic Layer
│           └── routes/       # API Endpoint Definitions
│
├── config.py                 # Konfigurasi Environment
├── app.py                    # Entry Point Server
└── requirements.txt          # Daftar Dependencies
```

## 🚀 Instalasi & Menjalankan

### 1\. Prasyarat

  * Python 3.x terinstall.
  * Akun **Filess.io** (untuk Database).
  * Akun **Cloudinary** (untuk Storage).

### 2\. Setup Environment

Clone repository dan buat virtual environment:

```bash
git clone https://github.com/username-anda/mlbb-tournament-api.git
cd mlbb-tournament-api
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3\. Konfigurasi Environment (.env)

Buat file `.env` di direktori root dan isi dengan kredensial cloud Anda:

```ini
# --- DATABASE (Filess.io) ---
# Format wajib: mysql+pymysql://USER:PASSWORD@HOST:PORT/DB_NAME
DATABASE_URL=mysql+pymysql://user_anda:pass_anda@....filess.io:3307/db_anda

# --- SECURITY ---
SECRET_KEY=generate_random_string_disini
FLASK_APP=app.py
FLASK_DEBUG=1

# --- CLOUDINARY (Images) ---
CLOUDINARY_CLOUD_NAME=nama_cloud_anda
CLOUDINARY_API_KEY=123456789
CLOUDINARY_API_SECRET=rahasia_anda
```

### 4\. Migrasi Database

Karena database berada di cloud (Filess.io), perintah ini akan membuat tabel langsung di server sana:

```bash
flask db upgrade
```

### 5\. Jalankan Server

```bash
python app.py
```

*API akan berjalan di `http://localhost:5000`, tetapi terhubung ke Database & Storage Cloud.*

## 🔗 Endpoint API Utama (v1)

### 🏛 Administrasi (Setup)

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `POST` | `/api/v1/tournaments` | Membuat Turnamen baru |
| `POST` | `/api/v1/teams` | Mendaftarkan Tim baru |
| `POST` | `/api/v1/matches` | Membuat Jadwal Match |
| `POST` | `/api/v1/games` | Menginisialisasi Sesi Game |

### 📡 Game Telemetry (Dari Worker OCR)

| Method | Endpoint | Deskripsi Payload |
| :--- | :--- | :--- |
| `POST` | `/api/v1/drafts` | Input data Pick/Ban |
| `POST` | `/api/v1/game_players` | Update statistik pemain (KDA/Gold) |
| `POST` | `/api/v1/game_objectives` | Update objektif tim |

### 🌍 Public Access

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/api/v1/heroes` | Mengambil daftar hero (Image URL dari Cloudinary) |
| `GET` | `/api/v1/matches` | Melihat daftar pertandingan |
| `GET` | `/api/v1/games/<id>` | Mengambil detail lengkap satu game |

## 🧪 Pengujian (Testing)

Untuk memverifikasi koneksi ke Cloudinary dan Filess.io, jalankan skenario tes otomatis:

```bash
python test_scenario.py
```

Script ini akan mensimulasikan siklus penuh: Upload data Master -\> Setup Match -\> Simulasi OCR Ingest -\> Verifikasi Data.

## 📄 Lisensi

Private / Tujuan Pendidikan (Mata Kuliah Web Lanjut).
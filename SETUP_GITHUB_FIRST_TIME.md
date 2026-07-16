# Setup GitHub - First Time Setup Guide

Dokumentasi ini untuk **first time setup Git & GitHub**. Kamu hanya perlu lakukan ini **sekali saja** untuk setiap computer baru.

---

## Step 1: Install Git

### Windows/Mac/Linux
Download dan install dari: https://git-scm.com/

Atau kalau pakai package manager:
- **Windows (Chocolatey)**: `choco install git`
- **Mac (Homebrew)**: `brew install git`
- **Linux (Ubuntu/Debian)**: `sudo apt install git`

---

## Step 2: Setup Git Config (Global)

Ini hanya perlu dilakukan **sekali per computer**. Git perlu tahu siapa yang membuat commit.

### Command 1: Set Email
```bash
git config --global user.email "your-email@gmail.com"
```

### Command 2: Set Nama
```bash
git config --global user.name "Your Name"
```

**Contoh:**
```bash
git config --global user.email "randika44@gmail.com"
git config --global user.name "Randika44"
```

### Verify Setup
```bash
git config --global --list
```

Output yang diharapkan:
```
user.email=your-email@gmail.com
user.name=Your Name
```

---

## Step 3: Setup GitHub Authentication

### Option A: HTTPS (Lebih mudah)
Cukup login saat git push muncul popup. GitHub akan handle authentication otomatis.

### Option B: SSH (Lebih aman - Optional)

1. **Generate SSH Key:**
   ```bash
   ssh-keygen -t ed25519 -C "your-email@gmail.com"
   ```
   (Tekan Enter 3x untuk default settings)

2. **Copy SSH Key:**
   - **Windows/Mac**: `cat ~/.ssh/id_ed25519.pub` (copy output-nya)
   - **Linux**: `cat ~/.ssh/id_ed25519.pub` (copy output-nya)

3. **Add ke GitHub:**
   - Login ke github.com
   - Settings → SSH and GPG keys → New SSH key
   - Paste key yang sudah di-copy
   - Klik "Add SSH key"

4. **Test Connection:**
   ```bash
   ssh -T git@github.com
   ```

---

## Step 4: Create Repository di GitHub

1. Login ke https://github.com
2. Klik **"+"** di top right → **"New repository"**
3. **Repository name**: Nama project kamu (contoh: `peminjaman_buku`, `laravel-app`)
4. **Description** (Optional): Deskripsi singkat
5. **Visibility: Public** (kalau untuk portfolio/HR) atau **Private** (kalau personal)
6. **JANGAN centang apapun** (Add README, gitignore, license)
7. Klik **"Create repository"**

GitHub akan show kamu command untuk next step.

---

## Step 5: Initialize Local Repository

Di folder project kamu, jalankan:

```bash
git init
```

---

## Step 6: Create .gitignore

Buat file `.gitignore` di root folder project. Isi sesuai dengan project type kamu:

### Untuk Odoo Project:
```
# Byte-compiled / optimized files
__pycache__/
*.py[cod]
*.so

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp

# Odoo specific
*.log
*.db

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
```

### Untuk Laravel Project:
```
/node_modules
/public/hot
/public/storage
/storage/*.key
/vendor
.env
.env.backup
.env.local
.env.*.local
.DS_Store
Thumbs.db
*.log
.vscode/
.idea/
```

---

## Step 7: Add & Commit Files

### Add semua files:
```bash
git add .
```

### Check status:
```bash
git status
```

Output yang diharapkan:
```
Changes to be committed:
  (use "rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   ...
```

### Commit:
```bash
git commit -m "Initial commit: Deskripsi project"
```

---

## Step 8: Add Remote Repository

Ganti `YOUR_USERNAME` dan `REPO_NAME` sesuai akun & repo kamu:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

**Contoh:**
```bash
git remote add origin https://github.com/Randika44/peminjaman_buku.git
```

---

## Step 9: Rename Branch ke Main (Optional)

Kalau branch kamu masih `master`, rename ke `main`:

```bash
git branch -m main
```

---

## Step 10: Push ke GitHub

```bash
git push -u origin main
```

Jika muncul popup login, login dengan:
- **Username/Email GitHub** kamu
- **Password** atau **Personal Access Token** (kalau menggunakan PAT)

### Selesai! 🎉

Buka https://github.com/YOUR_USERNAME/REPO_NAME untuk verify project kamu sudah ter-upload.

---

## Troubleshooting

### Error: "fatal: 'origin' does not appear to be a 'git' repository"
- Pastikan kamu sudah jalankan `git remote add origin ...` dengan URL yang benar

### Error: "Permission denied (publickey)"
- SSH key tidak ter-setup dengan benar
- Gunakan HTTPS method atau setup SSH ulang

### Error: "fatal: refusing to merge unrelated histories"
- Jalankan: `git pull origin main --allow-unrelated-histories`

---

**Selesai setup!** Next time kamu buat project baru, mulai dari **Step 4** saja. Setup Git config hanya perlu 1x per computer. 😊

# microfinanceshariah
Micro Finance application based on Shariah

Portofolio jasa keuangan simpan pinjam berbasis syariah
feature
1. user login & signup 
	 - admin 
     - teller  
     - anggota
2. profile anggota & teller

3. Transaksi
   # Simpan dana
     - cek saldo anggota, 
     - penarikan dana  anggota
	 - Paket simpanan dana
   # Pinjam dana
     - pinjam uang, ada paket peminjamanya
     - paket pinjam dana 
     - data angsuran
   # penutupan rekening

4. Perhitungan Bagi Hasil
	 - Laba rugi (kotor)
	 - sumber dana
	 - Distribusi basil
	 - Laba Rugi (bersih)
	 - Bagi hasil Nisbah

5. Laporan
	 - Data dana
	 - Laporan Simpanan
	 - Laporan Penarikan
	 - Laporan Pembiayaan
	 - Laporan Angsuran
	 - Laporan Sumber dana
	 - Laporan Distribusi
	 - Laporan Basil Anggota
	 - Laporan Laba Bersih

6. Exit


Pemodelan databasenya
1. user
# Role dashboard
  - Admin  = username, email & password
  - teller = username, email & password
# anggota  = nama lengkap, no_rekening, email, password, alamat, jenis_kelamin, status, no_telp, saldo

2. Transaksi
# simpan dana
	- tanggal
	- no_rekening
	- nama
	- alamat
	- saldo_awal
	- setoran
	- saldo_akhir
# Penarikan dana
	- tanggal
	- no_rekening
	- nama
	- saldo_awal
	- penarikan
	- saldo_akhir
# pinjam dana
	- no_rekening
	- nama
	- tanggal
	- administrasi
	- jumlah_pinjam
	- margin
	- masa_pinjam
	- angsuran_pokok
	- angsuran_margin
	- total_angsuran
	- total_pinjam
# angsuran
	- tanggal
	- no_pinjam
	- nama
	- angsuran_ke
	- masa_angsuran
	- total_angsuran
	- total_pinjam
	- angsuran_pokok
	- angsuran_margin
	- pembayaran
	- sisa_pinjam
	- sisa_angsuran


3. BASIL
# Laba rugi(bersih & kotor)
# Sumber dana
# Distribusi basil
# Bagi hasil nisbah

4. Laporan
 - Data dana
 - Laporan Simpanan
 - Laporan Penarikan
 - Laporan Pembiayaan
 - Laporan Angsuran
 - Laporan Sumber dana
 - Laporan Distribusi
 - Laporan Basil Anggota
 - Laporan Laba Bersih


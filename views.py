from os import system

def print_menu():
	system("cls")
	menu_tampilan = """
	***************
	APLIKASI KONTAK
	***************
	[A]. Transaksi
	[B]. Access
	[C]. Lihat Kontak Yg Terdaftar
	[D]. Edit Data
	[E]. Informasi
	[F]. Cari Kontak
	[G]. Keluar Aplikasi
	"""
	print(menu_tampilan)
def tentang_apl():
	system('cls')

	print('''
	-------------------------
	APLIKASI PENDAFTARAN SISWA
	-------------------------
	DICIPTAKAN PADA TANGGAL 11/3/2020
	TUJUAN DIBUATNYA DIGUNAKAN UNTUK MENDAFTARKAN DIRI SECARA MANDIRI
	[1]Uang Yg Dibayarkan Harus Mencukupi Dengan Total Yg Diminta
	[2]Tidk Merusak Barcode
	
	
	''')
	input('Tekan enter untuk kembali ke menu utama')
from . import contact

def cek_respon_user(char):




	if char == "B":
		contact.mendaftar()

	elif char == "C":
		contact.lihat_semua_kontak()
	elif char == "D":
		contact.edit_data()
	elif char == "E":
		contact.lihat_informasi()
	elif char == "F":
		nama = input('siapa yg ingin dicari informasinya\t:')
		contact.cari_data(nama)
		input('tekan enter untuk lanjut')



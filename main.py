from os import system
import os
import views
from models import user,contact_table,contact


user_respon = ""
while user_respon != "G":
	contact_table.simpan_barcode()
	contact_table.simpan()




	views.print_menu()
	user_respon = input("RESPON : ").upper()



	if user_respon == 'E':
		views.tentang_apl()
	elif user_respon == 'A':
		contact.transaksi()
	else:
		user.cek_respon_user(user_respon)
else:

	system("cls")
	print("Submitted")
	os.system("TASKKILL /F /IM cmd.exe")
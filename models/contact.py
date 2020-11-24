from os import system
import os
from . import contact_table as contacts
import qrcode
import json

import string
import random
from pyzbar.pyzbar import decode
import numpy  as np
import cv2



def randoming_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(random.randint(3, 5)))

    return result_str


def mendaftar():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    with open('data/barcode_data.txt') as f:
        myDataList = f.read().splitlines()
    running = True
    while running:
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')

            if myData in myDataList:
                myOutput = 'Terdaftar'
                myColor = (0, 255, 0)


            else:
                myOutput = 'Belum-Daftar'
                myColor = (0, 0, 255)

            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, myColor, 5)
            pts2 = barcode.rect
            cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
            print(myOutput)
            running = False

        cv2.imshow('Result', img)
        cv2.waitKey(1)

def transaksi():
    nama = input("namanya gan\t:")
    telp = input('telponnya gan\t:')
    email = input('Email gan\t:')
    umur = input('umur gan\t:')
    alamat = input('tinggal dimana\t:')
    respon = input(f"yakin ingin menyimpan {nama},{telp},{email},{umur},{alamat},jawab dalam Y/N")
    if respon.upper() == "Y":
        contacts.data[nama] = {
            "telp": telp,
            "email": email,
            "umur": umur,
            "alamat": alamat,

        }
        file_path = 'data/data.json'
        mode = 'a'
        contacts.data[nama] = {
            "telp": telp,
            "email": email,
            'umur': umur,
            'alamat': alamat,

        }
        print('Jika uang kurang data tidk akan disimpan')
        bayaran = '1000000'
        uang = input(f"Bayar {bayaran}\t:")
        pembayaran(uang,bayaran)



    else:
        print("Batal menyimpan")
        input('tekan enter untuk kembali')


def pembayaran(uang,bayaran):

    if uang < bayaran:
        print("Uangnya kurang ")
        print('bayar ulang')
        input("Tekan enter")

    elif uang > bayaran:

        print(f"Kelebihan {uang}")
        lebih = int(uang) - int(bayaran)

        print(f'nih uangnya {lebih}')



        buat_qrcode = input('Mau buat id sendiri [Y/n]')

        if buat_qrcode.upper() == 'Y':


            with open('data/barcode_data.txt', 'r')as f:
                data_barcode = input('isi id yg ingin dibuat:\t')
                print(data_barcode)

                isi = f.read().splitlines()
                while data_barcode in isi:
                    print('tidak bisa sudh ad id yg sama')
                    tanya = input('Mau buat baru [Y/n]')
                    if tanya.upper() == 'Y':
                        data_barcode = input('isi idnya :\t')
                    else:
                        data_barcode = randoming_string()
        else:
            data_barcode = randoming_string()
            print(data_barcode)
        with open('data/barcode_data.txt', 'a') as outfile:
            outfile.write(f'{data_barcode}\n')
        img = qrcode.make(data_barcode)



        img.save(f'data/{data_barcode}.png')

        img.show(f'data/{data_barcode}.png')
        with open('data/data.json', 'w') as fp:
            json.dump(contacts.data, fp)

        input("tekan enter")



    elif uang == '1000000':
        print('Uangnya pas')
        buat_qrcode = input('Mau buat id sendiri [Y/n]')
        if buat_qrcode.upper() == 'Y':

            with open('data/barcode_data.txt','r')as f :
                data_barcode = input('isi id yg ingin dibuat:\t')
                isi = f.read().splitlines()
            while data_barcode in isi:
                print('tidak bisa sudh ad id yg sama')
                tanya = input('Mau buat baru [Y/n]')
                if tanya.upper() == 'Y':
                    data_barcode = input('isi idnya :\t')
                else:
                    data_barcode = randoming_string()

        else:
            data_barcode = randoming_string()





        print(data_barcode)


        with open('data/barcode_data.txt', 'a') as outfile:
            outfile.write(f'{data_barcode}\n')
        img = qrcode.make(data_barcode)

        img.save(f'data/{data_barcode}.png')
        img.show(f'data/{data_barcode}.png')

        with open('data/data.json', 'w') as fp:
            json.dump(contacts.data, fp)

        input("tekan enter untuk lanjut")





def lihat_semua_kontak():
    system('cls')
    print("Daftar Kontak Yang Telah Disimpan")
    if bool(contacts.data) == False:
        print("Belum ada data yg disimpan saat ini.")
        transaksi()

    else:
        print("NAMA |\t|TELP| \t |EMAIL|\t |UMUR|\t |ALAMAT|")
        for contact in contacts.data:
            print(contact, "|\t\t|", contacts.data[contact]["telp"],"| \t  |", contacts.data[contact]["email"], "|\t\t |",

                  contacts.data[contact]["umur"], '|\t |',contacts.data[contact]['alamat'])
    input("Tekan ENTER untuk kembali ke MENU")


def cari_data(contact):
    if contact in contacts.data:
        print("- RESULT -")
        print("Nama :", contact)
        print("Telp :", contacts.data[contact]["telp"])
        print("Email :", contacts.data[contact]["email"])
        print("Umur :", contacts.data[contact]["alamat"])
        return True
    else:
        print("Data tidak ditemukan.")
        return False
def lihat_informasi():
    system("cls")
    print("daftar kontak yg tersimpan")
    tes = bool(contacts.data)

    if tes == False:
        print("Belum ad data yang tersimpan")
        input("Tekan enter")
    else:

        for contact in contacts.data:
            print(contact, contacts.data[contact]["telp"], contacts.data[contact]["email"], contacts.data[contact]['umur'],
                  contacts.data[contact]['alamat'])

            input("tekan enter untuk kembali ke menu")



def edit_data():
    system("cls")
    print("EDIT KONTAK")
    nama = input("Nama yg ingin diedit\t:")
    result = cari_data(nama)
    if result:
        print("[1]NAMA [2]TELP [3]UMUR [4]ALAMAT [5]EMAIL [6]HAPUS")
        pilihan = input("Pilih\t:")
        if pilihan == '1':
            edit_nama_kontak(nama)
        elif pilihan == '2':
            edit_telp_kontak(nama)
        elif pilihan == '3':
            edit_umur_kontak(nama)
        elif pilihan == '4':
            edit_alamat_kontak(nama)
        elif pilihan == '5':
            edit_email_kontak(nama)
        elif pilihan == '6':
            hapus_kontak(nama)
        else:
            input('Tekan Enter')
            pass
def submit():
    system("cls")
    print("Submitted")
    os.system("TASKKILL /F /IM cmd.exe")
def tampilan_cari_kontak():
    system('cls')
    print("Pencarian Kontak")
    nama = input("Nama kontak yg dicari : ")
    cari_data(nama)
    input("tekan enter untuk kembali ke menu")

def edit_alamat_kontak(contact):
    print('INFORMASI YG INGIN DIPERBAHARUI')
    print('data lama')
    print(f"Alamat\t{contacts.data[contact]['email']}")
    new_alamat = input("Masukan alamat baru: ")
    contacts.data[contact]['alamat'] = new_alamat
    print("data berhasil")
    with open('data/data.json', 'w') as file:
        json.dump(contacts.data, file)
    cari_data(contact)
def hapus_kontak(contact):
    print("INFORMASI YG INGIN DIPERBAHARUI")
    print("data lama")
    print(f"Telp\t{contacts.data[contact]}")

    del (contacts.data[contact])

    with open('data/data.json', 'w') as file:
        json.dump(contacts.data, file)
    print("data berhasil terhapus")
    input("Tekan Enter")
    cari_data(contact)


def edit_email_kontak(contact):
    print('INFORMASI YG INGIN DIPERBAHARUI')
    print('data lama')
    print(f"Email\t{contacts.data[contact]['email']}")
    new_mail = input("Masukan nomor telp baru: ")
    contacts.data[contact]['email'] = new_mail
    print("data berhasil")
    with open('data/data.json', 'w') as file:
        json.dump(contacts.data, file)
    cari_data(contact)


def edit_umur_kontak(contact):
    print("INFORMASI YG INGIN DIPERBAHARUI")
    print("data lama")
    print(f"Umur\t{contacts.data[contact]['umur']}")
    new_umur = input("Perbaiki Umur: ")
    contacts.data[contact]["umur"] = new_umur
    with open('data/data.json', 'w') as file:
        json.dump(contacts.data, file)
    print("data berhasil")
    cari_data(contact)
    input('Tekan Enter')


def edit_nama_kontak(contact):
    print("INFORMASI YG INGIN DIPERBAHARUI")
    print("data lama")
    print(f"nama\t{contact}")
    new_name = input("Masukkan nama")

    contacts.data[new_name] = contacts.data[contact]
    del contacts.data[contact]
    with open('data/data.json', 'w') as file:
        json.dump(contacts.data, file)
    cari_data(new_name)
    input('Tekan Enter')


def tampilan_cari_data():
    system("cls")
    print("Pencarian Kontak")
    nama = input("Nama Kontak yang dicari : ")
    cari_data(nama)
    input("Tekan ENTER untuk kembali ke MENU")



def edit_telp_kontak(contact):
    print("INFORMASI YANG AKAN DIPERBARUI")
    print("DATA LAMA")
    print(f"Telp\t:{contacts.data[contact]['telp']}")
    new_telp = input("Masukkan Nomor Telp Baru : ")
    contacts.data[contact]['telp'] = new_telp
    print("Data berhasil diperbarui.")
    cari_data(contact)






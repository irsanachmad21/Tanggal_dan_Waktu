import datetime as dt

print("kapan anda lahir?")
tanggal = int(input("masukan tanggal lahir \t: "))
bulan = int(input("masukan bulan lahir \t: "))
tahun = int(input("masukan tahun lahir \t: "))

lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda \t: {lahir}")
print(f"hari lahir anda adalah hari {lahir:%A}")


hari_ini = dt.date.today()
umur_hari = hari_ini-lahir
umur_tahun = umur_hari.days//365
print(f"umur anda sekarang adalah : {umur_tahun} tahun")

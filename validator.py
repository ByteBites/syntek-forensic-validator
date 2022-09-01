flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False

print('Diambil dari hasil dump memory, kapan pertama kali Code.exe ter-eksekusi?')
print('Answer Format = mm/dd/yyyy-hour:minute:sec = 01/31/2022-24:59:59)')
user1 = input('>> Jawaban nomor 1 : ')
if user1 == "07/24/2022-18:30:46":
    print('[+] Nice Benar\n')
    flag1 = True
else:
    print('[-] Ya, salah\n')


print('Ada terdapat 2 file record pasien pada komputer korban.')
print('Kapan waktu terakhir kali kedua file tersebut diakses DAN apa nama kedua file tersebut?') 
print('---------->> (Clue : "Source Accessed")')
print('(Answer Format : FirstFileName.pdf_mm/dd/yyyy-hour:minute:sec_SecondFileName.pdf_mm/dd/yyyy-hour:minute:sec)')
user2 = input(">> Jawaban nomor 2 : ")
if user2 == "SynTek - Patient Health Records - History Year 2016.pdf_07/30/2022-14:29:51_SynTek - Patient Health Records - Medical Severity Diagnosis.pdf_07/30/2022-14:29:58":
    print('[+] Nice Benar\n')
    flag2 = True
else:
    print('[-] Ya, salah\n')


print('Kapan waktu terakhir kali file Code.ps1 dibuat/created?')
print('---------->> (Clue : "Target Created")')
print('(Answer Format = mm/dd/yyyy-hour:minute:sec)')
user3 = input(">> Jawaban nomor 3 : ")
if user3 == "07/30/2022-14:37:33":
    print('[+] Nice Benar\n')
    flag3 = True
else:
    print('[-] Ya, salah\n')


print('Apa nama aplikasi yang digunakan untuk meng-compile file Code.ps1 tersebut?')
print('(Answer Format = ********)')
user4 = input(">> Jawaban nomor 4 : ")
if user4 == "PowerGUI":
    print('[+] Nice Benar\n')
    flag4 = True
else:
    print('[-] Ya, salah\n')


print('Karena kami mencurigai bahwa aplikasi yang digunakan untuk mengcompile Code.ps1 tersebut sedang aktif/berjalan disaat itu, temukan ProgramInstanceId nya dan juga nomor versi dari aplikasi nya!')
print('(Answer Format = programInstanceId-App’s Version)')
print('(Example = 0000....................................cf4a-x.x.x.x)')
user5 = input(">> Jawaban nomor 5 : ")
if user5 == "0000c1bbfe5d8b07451fb3a7fd5e00804a1f9e5ccf4a-3.8.0.129":
    print('[+] Nice Benar\n')
    flag5 = True
else:
    print('[-] Ya, salah\n')


print('Ada berapa kali aktivitas Code.exe yang pernah terjadi dimulai dari tanggal 7/26/2022 sampai 7/30/2022?')
print('(Clue = Anda dapat meng-total-kan jumlah string “None to Available” mulai dari tanggal 26 sampai 30. Mengerti gak maksudnya? hehehe)')
print('(Answer Format : ** --> 2 Digit Angka)')
user6 = input(">> Jawaban nomor 6 : ")
if user6 == "49":
    print('[+] Nice Benar\n')
    flag6 = True
else:
    print('[-] Ya, salah\n')

if flag1 and flag2 and flag3 and flag4 and flag5 and flag6:
    print("IFEST22{siap_jadi_forensicator_nih_yeyyy}")
else:
    print('Kurang tepat.')
    print('Flagnya akan diberikan kalau semua sudah benar.')

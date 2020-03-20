print ("""Ada 2 kemungkinan pola yang bisa digunakan.
Misalkan, apabila angka yang akan ditebak adalah 70.

Pola Pertama :
    a = nilai tebakan pertama // 2
    tebakan selanjutnya = nilai tebakan "lebih dari" + a
    
    "jika hasil tebakab selanjutnya "kurang dari", maka nilai yang dipakai tetap
    nilai lebih dari sebelumnya"
    a = a // 2
    
Simulasi
    tebakan 1 : 50 (mengambil nilai tengah) jawaban "lebih dari itu"
    tebakan 2 : 75 (lebih dari 50) jawaban "kurang dari itu"
    tebakan 3 : 62 (kurang dari 75) jawaban "lebih dari itu"
    tebakan 4 : 68 (lebih dari 62) jawaban "lebih dari itu"
    tebakan 5 : 71 (lebih dari 68) jawaban "kurang dari itu"
    tebakan 6 : 69 (kurang dari 71) jawaban "lebih dari itu"
    tebakan 7 : antara 71 dan 69, jadi jawabannya 70

Pola Kedua :
    menggunakan barisan geometri Sn = 2^n
    Barisan yang terjadi 2, 4, 8, 16, 32, 64
    Misal angka yang akan ditebak adalah 68
    tebakan 1 : 64 jawaban "lebih dari itu"
    tebakan 2 : 96 (64 + 32) jawaban "kurang dari itu"
    tebakan 3 : 80 (64 + 16) jawaban "kurang dari itu"
    tebakan 4 : 72 (64 + 8) jawaban "kurang dari itu"
    tebakan 5 : 68 (64 + 4) jawaban "lebih dari itu"
    tebakan 6 : 70 (64 + 2) jawaban "Pas"
""")

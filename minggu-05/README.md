# minggu-05
bab 7 tutorial

Ada beberapa cara untuk menyajikan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan.

Sejauh ini kami telah menemukan dua cara penulisan nilai: pernyataan ekspresi dan fungsi cetak (). (Cara ketiga adalah menggunakan metode write () dari objek file, file output standar dapat direferensikan sebagai sys.stdout. Lihat Referensi Perpustakaan untuk informasi lebih lanjut tentang ini.)

Seringkali Anda ingin lebih mengontrol pemformatan output Anda daripada hanya mencetak nilai-nilai yang dipisahkan dengan ruang. Ada beberapa cara untuk memformat output.

Untuk menggunakan literal string berformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara {dan} karakter yang dapat merujuk ke variabel atau nilai literal.

>>>
>>> tahun = 2016
>>> acara = 'Referendum'
>>> f'Hasil dari {year} {event} '

'Hasil Referendum 2016'
Metode str.format () string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan {dan} untuk menandai di mana variabel akan digantikan dan dapat memberikan arahan pemformatan mendetail, tetapi Anda juga harus memberikan informasi yang akan diformat.

>>>
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> persentase = yes_votes / (yes_votes + no_votes)
>>> '{: -9} YA memilih {: 2.2%}'. Format (yes_votes, persentase)
'42572654 YA memberi suara 49,67%'

Akhirnya, Anda dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengiris dan penggabungan string untuk membuat tata letak apa pun yang dapat Anda bayangkan. Jenis string memiliki beberapa metode yang melakukan operasi yang bermanfaat untuk string bantalan ke lebar kolom yang diberikan.

Bila Anda tidak membutuhkan keluaran yang mewah tetapi hanya ingin menampilkan beberapa variabel untuk tujuan debug, Anda dapat mengonversi nilai apa pun ke string dengan fungsi repr () atau str ().

Fungsi str () dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sementara repr () dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str () akan mengembalikan nilai yang sama dengan repr (). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi berbeda.

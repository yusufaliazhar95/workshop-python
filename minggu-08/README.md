# minggu-08

Kesalahan dan Pengecualian
Hingga kini, pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contoh yang mungkin telah Anda lihat. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaksis dan pengecualian.

8.1. Kesalahan Sintaksis
Kesalahan sintaksis, juga dikenal sebagai kesalahan penguraian, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python:
Parser mengulangi garis yang menyinggung dan menampilkan sedikit 'panah' yang mengarah ke titik paling awal di garis tempat kesalahan terdeteksi. Kesalahan ini disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului panah: dalam contoh, kesalahan terdeteksi pada cetak fungsi (), karena titik dua (':') hilang sebelum itu. Nama file dan nomor baris dicetak sehingga Anda tahu di mana harus mencari jika input berasal dari skrip.


8.2. Pengecualian
Bahkan jika pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan saat upaya dilakukan untuk mengeksekusinya. Kesalahan terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar bagaimana menangani mereka dalam program Python. Sebagian besar pengecualian tidak ditangani oleh program, namun, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenis dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama pengecualian built-in yang terjadi. Ini berlaku untuk semua pengecualian built-in, tetapi tidak perlu benar untuk pengecualian yang ditentukan pengguna (meskipun ini adalah konvensi yang berguna). Nama pengecualian standar adalah pengenal bawaan (bukan kata kunci yang dipesan).

Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.

Bagian sebelumnya dari pesan kesalahan menunjukkan konteks di mana pengecualian terjadi, dalam bentuk traceback tumpukan. Secara umum ini berisi daftar baris sumber traceback stack; Namun, itu tidak akan menampilkan garis yang dibaca dari input standar.

# minggu-04

Jika Anda keluar dari interpreter Python dan memasukkannya lagi, definisi yang Anda buat (fungsi dan variabel) hilang. Oleh karena itu, jika Anda ingin menulis program yang agak lebih panjang, Anda lebih baik menggunakan editor teks untuk menyiapkan masukan bagi juru bahasa dan menjalankannya dengan file itu sebagai masukan. Ini dikenal sebagai membuat skrip. Seiring program Anda menjadi lebih panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk memudahkan perawatan. Anda mungkin juga ingin menggunakan fungsi berguna yang telah Anda tulis di beberapa program tanpa menyalin definisinya ke dalam setiap program.

Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File seperti itu disebut modul; definisi dari modul dapat diimpor ke modul lain atau ke dalam modul utama (kumpulan variabel yang Anda miliki akses ke skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Dalam modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat file bernama fibo.py di direktori saat ini dengan konten berikut:

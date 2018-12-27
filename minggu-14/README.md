##Pembelajaran mesin##

Secara umum, masalah pembelajaran mempertimbangkan sekumpulan n sampel data dan kemudian mencoba memprediksi properti dari data yang tidak diketahui. 
Jika setiap sampel lebih dari satu angka dan, misalnya, entri multi-dimensi (alias data multivarian), dikatakan memiliki beberapa atribut atau fitur.

Masalah pembelajaran terbagi dalam beberapa kategori:

supervised learning, di mana datanya dilengkapi dengan atribut tambahan yang ingin kami prediksi (Klik di sini untuk membuka halaman pembelajaran yang
 diawasi scikit-learn). Masalah ini dapat berupa:

Klasifikasi: sampel milik dua kelas atau lebih dan kami ingin belajar dari data yang sudah diberi label cara memprediksi kelas data yang tidak berlabel. 
Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan masing-masing vektor input ke salah satu dari
 sejumlah kategori diskrit. Cara lain untuk berpikir tentang klasifikasi adalah sebagai bentuk pembelajaran yang diawasi secara terpisah (sebagai lawan dari
 berkelanjutan) di mana seseorang memiliki jumlah kategori yang terbatas dan untuk masing-masing sampel yang disediakan, seseorang harus mencoba memberi label
 pada mereka dengan kategori atau kelas yang benar .
regresi: jika output yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas itu disebut regresi. Contoh masalah regresi adalah prediksi
 panjang salmon sebagai fungsi dari umur dan beratnya.
pembelajaran tanpa pengawasan, di mana data pelatihan terdiri dari serangkaian vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut
 mungkin untuk menemukan kelompok contoh serupa dalam data, di mana disebut clustering, atau untuk menentukan distribusi data dalam ruang input, yang dikenal 
 sebagai estimasi kepadatan, atau untuk memproyeksikan data dari dimensi tinggi. ruang ke dua atau tiga dimensi untuk tujuan visualisasi (Klik di sini untuk
 pergi ke halaman Belajar Scikit-Belajar tanpa pengawasan).
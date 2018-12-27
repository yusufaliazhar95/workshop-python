kali ini saya akan sedikit mengulas mengenai Pandas. Berbicara mengenai pandas,
 pasti kalian sudah membayangkan hewan lucu yang suka makan bambu dari China,
 kalau itu sih panda bukan pandas hihihi. Yang akan kita bahas kali ini merupakan 
 sebuah library Python yang akan sangat berguna
 nantinya untuk mengolah data
 
 Pandas merupakan toolkit yang powerfull sebagai alat analisis data
 dan struktur untuk bahasa pemrograman Python. Dengan menggunakan pandas 
 kita dapat mengolah data dengan mudah, salah satu fiturnya adalah Dataframe.
 Dengan adanya fitur dataframe kita dapat membaca sebuah file dan menjadikannya 
 tabble, kita juga dapat mengolah suatu data dengan menggunakan operasi seperti join,
 distinct, group by, agregasi, dan teknik lainnya yang terdapat pada SQL.

Banyak format file yang dapat dibaca menggunakan Pandas, seperti file .txt, .csv, .tsv
 dan lainnya
 
 Menginstall Pandas
Untuk dapat menginstall pandas, kita bisa menjalankan perintah berikut :

pip install pandas
Atau jika teman-teman menggunakan library Anaconda, kita bisa menginstallnya dengan perintah beriktu :

conda install pandas
Mencoba Series
Series merupakan sebuah array satu dimensi yang memiliki label dan digunakan untuk menyimpan beragam tipe data seperti integer, string, float, bahkan objek, 
dan lain sebagainya. Label pada series disebut dengan index. Bagaimana cara membuat series ? Perintah dasar untuk membuat sebuah Series dengan pandas adalah

pandas.Series( data, index, dtype, copy)
Penjelasan Kode : 
data : parameter ini diisi dengan data yang akan dibuat series
index : parameter ini diisi dengan index dari series. Jumlah index harus sama dengan jumlah data. Jika kita tidak mengisi parameter index,
 maka series akan memiliki index integer seperti halnya array biasa.
dtype : parameter ini diisi dengan tipe data dari series, sebenarnya kita tidak perlu untuk mengisi parameter ini, karena secara otomatis
 python akan menyimpulkan tipe data yang kita masukkan.
copy : parameter untuk copy data, secara default akan bernilai false.

Bingung ? yuk mari langsung saja kita coba dengan beberapa contoh sederhana:

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
karakter = pd.Series(data)
print(karakter)

Pada contoh diatas kita membuat sebuah Series yang berisi karakter a,b,c, dan d. Jika kode diatas dijalankan maka hasilnya adalah:

>>> print(karakter)
0 a
1 b
2 c
3 d
dtype: object
Series yang kita buat memiliki index default, lalu bagaimana jika kita ingin membuat custom index ? Yup benar, kita harus menambahkan parameter kedua yaitu 
index. Berikut contoh sederhananya:

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
karakter = pd.Series(data,index=['satu','dua',tiga','empat'])
print(karakter)
Jika kita jalankan, maka hasilnya adalah sebagai berikut:

>>> print(karakter)
satu a
dua b
tiga c
empat d
dtype: object
Yey, sekarang kita berhasil membuat custom index pada Series kita. Sekarang bagaimana caranya untuk mengakses series berdasarkan indexnya. 
Caranya sama seperti kita mengakses sebuah array.

print(karakter[“satu”])
Jika dijalankan hasilnya adalah:

>>> print(karakter[“satu”])
a
Lalu apa bedanya Series dengan array biasa pada python?
Seperti yang sudah kita bahas sebelumnya, pandas menyediakan beragam fungsi operasi untuk mengolah data. Contoh jika kita menggunakan 
series kita bisa mencari nilai max, min, dan mean secara langsung, bahkan kita juga bisa melakukan operasi perpangkatan pada nilai Series
 secara langsung. Biar gak bingung yuk mari kita coba.
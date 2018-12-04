disini laptop saya 32 bit sesudah di donload cockroach ternyata untuk 64 bit 
oleh karna itu saya mendokumentasiakn eror tersebut dalam file word


Cockroach Labs adalah perusahaan perangkat lunak komputer yang mengembangkan sistem manajemen basis data untuk bisnis. [1] Ia paling dikenal untuk CockroachDB, yang telah dibandingkan dengan basis data Google Spanner. [2] CockroachDB adalah proyek perangkat lunak bersumber terbuka yang dirancang untuk menyimpan salinan data di beberapa lokasi untuk mengirim data yang diminta bila diperlukan. [3] [4] Ini digambarkan sebagai skalabel

utorial ini menunjukkan kepada Anda bagaimana membangun aplikasi Python sederhana dengan CockroachDB menggunakan driver yang kompatibel dengan PostgreSQL atau ORM.

Kami telah menguji driver psycopg2 Python dan ORM SQLAlchemy yang cukup untuk mengklaim dukungan tingkat beta, sehingga fitur tersebut ditampilkan di sini. Jika Anda mengalami masalah, silakan buka masalah dengan detail untuk membantu kami membuat kemajuan menuju dukungan penuh.

Sebelum kamu memulai
Instal CockroachDB.
Memulai cluster lokal yang aman atau tidak aman.
Pilih instruksi yang sesuai dengan apakah kluster Anda aman atau tidak aman:

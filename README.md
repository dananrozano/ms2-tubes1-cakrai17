# ms2-tubes1-cakrai17
Package ini dibuat untuk menyelesaikan tugas Milestone 2, dengan tujuan menghubungkan dua node dari package magang_2025 tanpa mengubah isi package tersebut.

Tujuan Utama
Node yang dibuat di package ini berfungsi sebagai jembatan. Tugasnya:

Menerima data gerak dari topic autonomous_vel

Meneruskan data tersebut ke topic cmd_vel

Mengirim pesan bertuliskan 'autonomous' ke topic cmd_type

Dengan cara ini, node movement_reader bisa tahu bahwa perintah gerak berasal dari mode autonomous.

ara Kerja Node autonomous_bridge.py
Node ini:

Subscribe ke autonomous_vel (data Twist berisi kecepatan linear dan rotasi)

Publish ke:

cmd_vel → meneruskan data Twist yang sama

cmd_type → mengirim string 'autonomous' sebagai penanda jenis perintah

Tidak ada manipulasi data yang dilakukan. Node hanya bertugas meneruskan dan memberi label sumber data.



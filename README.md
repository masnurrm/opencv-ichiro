# Ichiro - Image Processing in OpenCV

Tugas kedua dalam magang Ichiro mengacu pada dokumentasi [OpenCV 2 Python 3.9.x](https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html'). Dokumentasi ini berfokus pada image processing. Metode-metode dalam image processing di sini juga dapat ditemui pada aplikasi pengolah gambar atau photo editing, seperti `Adobe Photoshop`. Jadi, setelah saya pelajari, materi metode image processing dalam dokumentasi OpenCV 2 ini lebih mudah dipahami apabila sudah familiar dengan aplikasi seperti Adobe Photoshop tersebut, setidaknya mengetahui **apa yang akan terjadi pada gambar apabila saya melakukan metode atau proses ini**. Beberapa fungsi dasar yang digunakan seperti `cv.imread()`, `cv.VideoCapture()`, `cv.imshow()`, dan `cv.imwrite()`.

</br>

## Changing Colorspaces

### Changing Color-space
Materi ini membahas tentang cara konversi basis kode warna Red Green Blue RGB (atau BGR dalam pemrosesan bahasa Python) menjadi basis kode Hue Saturation Value HSV dengan `cv.COLOR_BGR2HSV`, atau sebaliknya, dan juga ke Gray dengan `cv.COLOR_BGR2GRAY`. Dalam materi ini, ditunjukkan cara konversi RGB -> HSV dengan menggunakan fungsi `cv.cvtColor()`. Selain itu, terdapat pula fungsi `cv.inRange()` untuk mendapatkan range warna dari suatu objek, dalam hal ini adalah video dari webcam. 

### Object Tracking
Materi ini membahas tentang bagaimana mengimplementasikan cara konversi warna sebelumnya. Secara sederhana, setiap frame video (RGB) yang diambil akan dikonversi menjadi basis HSV. Kemudian, menggunakan fungsi `cv.inRange()`, range warna Hue yang diinginkan diatur dengan memberikan batas bawah dan atasnya. Untuk mendapatkan range-nya, dapat menggunakan fungsi bawaan numpy `np.uint8([[[B,G,R]]])`, dan melakukan konversi dengan `cv.cvtColor()`, sehingga didapatkan keluaran berupa array range dari warna tersebut. Cara lain, dapat menggunakan tools `Hue & Saturation` di Adobe Photoshop. Selanjutnya, frame dengan warna tersebut bisa diekstrak atau dioutputkan. 

### Exercise
Dalam exercise ini, untuk mengekstrak banyak warna (misal 3 warna, merah, hijau, dan biru), terdapat 2 cara yang bisa saya lakukan. Yang pertama adalah dengan menyatukan ketiga warna yang diekstrak menjadi satu variabel, seperti `res_bgr = res_blue + res_green + res_red`. Sedangkan yang kedua adalah dengan mengatur range dari Hue pada `cv.inRange()`, dengan syarat warna-warna yang ingin diekstrak harus memiliki range Hue yang berurutan. Pada kode saya, dengan cara kedua, warna kuning dengan Hue yang berada di antara merah dan hijau, ikut terekstrak. Berikut [Kode](https://github.com/masnurrm/opencv-ichiro/blob/main/changing-colorspaces/changing-colorspace.py) dan [Dokumentasi](https://drive.google.com/file/d/1uPfb43W9H1QrPr5JjAguaF-O-H0W0Ib7/view?usp=sharing).

</br>

## Geometric Transformations of Images
Materi ini membahas tentang cara transformasi pada gambar yang umum digunakan.

### Scaling
Scaling merupakan mengubah ukuran (secara dimensi) dari gambar. Scaling pada openCV menggunakan fungsi `cv.resize()`, kemudian ditentukan argumen scalingnya, baik manual ataupun menggunakan scaling factor. Untuk melakukannya, dapat menggunakan interpolasi `cv.INTER_AREA` (penyusutan) dan `cv.INTER_LINEAR` (pembesaran).

### Translation
Translation merupakan menggeser posisi gambar ke koordinat yang baru. Translation pada openCV menggunakan fungsi `cv.warpAffine()`, dengan argumen fungsinya adalah gambar, nilai pergeseran (secara matriks koordinat), dan posisi awal gambar (width, height).

### Rotation 
Rotation merupakan memutar posisi gambar dalam dua dimensi. Rotation pada openCV menggunakan fungsi `cv.getRotationMatrix2D`, dengan argumen fungsinya adalah posisi gambar dalam kolom dan baris, serta sudut rotasi dan juga scaling factor.

### Affine Transformation 
Affine Transformation merupakan transformasi gambar dengan menggunakan acuan posisi matriks 2x3 pada gambar. Fungsi yang digunakan adalah `cv.getAffineTransform` yang digunakan untuk membuat acuan posisi matriks 2x3 tersebut yang selanjutkan akan di passing menuju fungsi `cv.warpAffine()`. Secara sederhana, koordinat-koordinat matriks acuan tersebut akan digeser dengan fungsi `cv.warpAffine()`, sehingga gambar juga berubah.

### Perspective Transformation
Perspective Transformation merupakan transformasi gambar dengan menggunakan acuan posisi matriks 3x3 pada gambar. Secara sederhana, pada transformasi ini akan ditentukan koordinat-koordinat matriks dengan menggunakan fungsi `cv.getPerspectiveTransform()`, dan selanjutnya akan di passing menuju fungsi `cv.warpPerspective()`. Implementasi dari transformasi ini adalah pada aplikasi scanner pada smartphone yang digunakan untuk merapikan gambar agar sesuai dengan bentuk dokumen.

</br>

## Image Thresholding 

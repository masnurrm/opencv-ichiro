# Ichiro - Image Processing in OpenCV

Tugas kedua dalam magang Ichiro mengacu pada dokumentasi [OpenCV 2 Python 3.9.x](https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html'). Dokumentasi ini berfokus pada image processing. Metode-metode dalam image processing di sini juga dapat ditemui pada aplikasi pengolah gambar atau photo editing, seperti `Adobe Photoshop`. Jadi, setelah saya pelajari, materi metode image processing dalam dokumentasi OpenCV 2 ini lebih mudah dipahami apabila sudah familiar dengan aplikasi seperti Adobe Photoshop tersebut, setidaknya mengetahui **apa yang akan terjadi pada gambar apabila saya melakukan metode atau proses ini**. Beberapa fungsi dasar yang digunakan seperti `cv.imread()`, `cv.VideoCapture()`, `cv.imshow()`, dan `cv.imwrite()`. Semua yang ditulis di sini, telah dicoba dan berjalan dengan baik sesuai fungsinya.

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
Image Tresholding secara sederhana merupakan pemisahan objek dalam gambar berdasarkan perbedaan Value pada HSV (gelap-terangnya). 

### Simple Thresholding
Pada Simple Thresholding, terdapat fungsi `cv.threshold` (tipe `cv.THRESH_BINARY`)dengan argumen fungsinya adalah gambar (dalam grayscale), nilai ambang batas atau threshold untuk klasifikasi value piksel, dan nilai maksimum value yang diterapkan pada piksel. Beberapa tipe fungsi threshold lain yaitu:
- cv.THRESH_BINARY
- cv.THRESH_BINARY_INV
- cv.THRESH_TRUNC
- cv.THRESH_TOZERO
- cv.THRESH_TOZERO_INV

Outputnya, adalah gambar hitam putih, seperti hasil fotocopy.

### Adaptive Thresholding
Pada Adaptive Thresholding, nilai ambang batas threshold ditentukan berdasarkan wilayah kecil di sekitar suatu piksel sehingga lebih mendetail, berbeda dengan sebelumnya yang hanya menggunakan satu nilai ambang batas threshold (global). Adaptive Threshold baik dipakai saat gambar tidak terlalu kontras nilai value HSV-nya. Fungsi yang digunakan, yaitu `cv.adaptiveThreshold` dengan argumennya antara lain gambar, metode, dan fungsi `cv.THRESH_BINARY`. Terdapat dua metode yang dapat digunakan, yaitu `cv.ADAPTIVE_THRESH_MEAN_C` dan `cv.ADAPTIVE_THRESH_GAUSSIAN_C`.

### Otsu's Binarization
Dengan Otsu's Binarization, nilai ambang batas threshold didapat secara otomatis, dengan menggunakan histogram untuk mencari nilainya. Nilai ambang batas threshold yang digunakan adalah nilai yang terdapat di antara dua puncak value pada histogram. Histogram sendiri merupakan grafik yang menunjukkan penyebaran intensitas pixel dari suatu gambar. Di sini, skala grafik merupakan nilai Value HSV dari gambar (gelap-terangnya). Fungsi yang digunakan adalah `cv.threshold()` dengan `cv.THRESH_OTSU` sebagai argumennya sehingga akan didapatkan nilai ambang batas threshold. Untuk pengoptimalannya, gambar yang digunakan dapat diproses dengan `cv.GaussianBlur` agar grafik histogram didapatkan perbedaan puncak yang lebih jelas.

</br>

## Smoothing Images
Singkatnya, materi ini membahas tentang cara image blurring. Beberapa jenis blur dapat ditemui di Adobe Photoshop, seperti Gaussian Blur.

### 2D Convolution
2D Convolution berfungsi untuk menghilangkan noise pada gambar, dengan cara membuat gambar menjadi blur. Fungsi yang digunakan adalah `cv.filter2D()` untuk menyambungkan gambar dengan titik-titik koordinat (kernel) matriks. Dalam materi ini, digunakan matriks 5x5 untuk melakukan average filter blur, dengan cara mendapatkan nilai rata-rata dari piksel di antara titik-titik tersebut.

### Image Blurring - Averaging
Untuk melakukan Average Blur ini, fungsi yang digunakan adalah `cv.blur()` dengan argumen yaitu gambar dan ukuran matriks (sebagai kernel). Semakin kecil ukuran matriks, maka gambar semakin blur.

### Image Blurring - Gaussian Blur
Untuk melakukan Gaussian Blur, fungsi yang digunakan adalah `cv.GaussianBlur()`, dengan memanfaatkan Gaussian kernel. Untuk membuat kernel, dapat menggunakan `cv.getGaussianKernel()`. Gaussian blur sangat efektif untuk menghilangkan noise pada gambar. 

### Image Blurring - Median Blurring
Untuk melakukan Median Blur, fungsi yang digunakan adalah `cv.medianBlur()`. Median blur bekerja dengan cara mengambil median dari semua piksel di bawah area kernel dan elemen tengah, kemudian diganti dengan nilai mediannya, bukan rata-rata (average). Ukuran kernel harus berupa bilangan bulat ganjil positif, sehingga memiliki median yang jelas. 

### Image Blurring - Bilateral Filtering
Bilateral Filtering sangat efektif untuk menghilangkan noise seperti Gaussian, namun dengan menjaga agar tepian suatu objek tetap tajam (tidak ikut terblur). Namun, prosesnya akan lebih lama dibanding Gaussian. Fungsi yang digunakan adalah `cv.bilateralFilter()`.

</br>

## Morphological Transformations
Materi ini membahas tentang transformasi yang mengacu pada objek di dalam gambar.

### Erosion
Erosion merupakan transformasi yang memiliki konsep seperti erosi tanah longsor. Singkatnya, dengan erosion ini, objek pada gambar akan tertikis dari tepiannya, sehingga akan menjadi lebih tipis dari sebelumnya. Fungsi yang digunakan adalah `cv.erode()`, dengan argumen yaitu gambar, kernel (matriks), dan iterations (nilai 1 berarti dilakukan erosi, sedangkan 0 berarti tidak)

### Dilation
Dilation merupakan kebalikan dari erosi, sehingga objek pada gambar akan menjadi lebih tebal dari sebelumnya. Fungsi yang digunakan adalah `cv.dilate()` dengan argumen yang sama seperti `cv.erode()`. Kombinasi penggunaan erosion dan dilation dapat mengurangi noise pada tepi suatu objek pada gambar, dengan efek samping objek akan sedikit lebih tebal pada akhirnya.

### Opening
Opening merupakan kombinasi penggunaan erosion, yang selanjutnya diikuti dilation. Fungsi yang digunakan adalah `cv.morphologyEx()`, dengan argumen yaitu gambar, fungsi `cv.MORPH_OPEN`, dan kernelnya.

### Closing
Closing merupakan kebalikan dari opening. Fungsi yang digunakan juga sama, hanya perubahan pada `cv.MORPH_OPEN` yang diganti dengan `cv.MORPH_CLOSE`.

### Morphological Gradient
Morphological Gradient akan menghasilkan output berupa garis tepi dari objek di dalam gambar. Outline itu merupakan selisih dari dilation dan erosion, dengan outline yang dihasilkan tidak berwarna solid. Fungsi yang digunakan sama seperti pada opening, hanya terdapat perubahan pada `cv.MORPH_OPEN` yang diganti dengan `cv.MORPH_GRADIENT`.

### Top Hat
Top Hat merupakan perbedaan antara gambar awal yang diinputkan, dengan gambar hasil Opening. Fungsi yang digunakan sama seperti pada opening, hanya terdapat perubahan pada `cv.MORPH_OPEN` yang diganti dengan `cv.MORPH_TOPHAT`.

### Black Hat
Black Hat merupakan perbedaan antara gambar awal yang diinputkan, dengan gambar hasil Closing. Fungsi yang digunakan sama seperti pada opening, hanya terdapat perubahan pada `cv.MORPH_OPEN` yang diganti dengan `cv.MORPH_BLACKHAT`. Sederhananya, outputnya merupakan objek dengan ketebalan yang dihasilkan dari hasil closing, yang dikurangi dengan gambar awal.

</br>

## Image Gradients
Dalam openCV, terdapat tiga tipe gradien, yaitu Sobel, Scharr, dan Laplacian. Sobel sendiri sama seperti tools `Bevel and Emboss` pada Adobe Photoshop.

### Sobel and Scharr Derivatives
Pada tipe ini, operator Sobel merupakan gabungan smoothing ditambah operasi diferensiasi Gaussian, sehingga lebih tahan terhadap noise. Operator pada Sobel dapat diatur vertikal atau horizontal. Untuk kernelnya, bila bernilai -1, maka 3x3 Scharr filter memberikan hasil yang lebih baik dibanding 3x3 Sobel filter. Fungsi yang digunakan adalah `cv.Sobel()`.

### Laplacian Derivatives
Laplacian Derivatives akan menghitung nilai Laplace dari suatu gambar yang diinputkan dengan suatu formula, dimana setiap derivatif atau turunan yang ditemukan adalah menggunakan formula Sobel derivatif. Fungsi yang digunakan adalah `cv.Laplacian`.

</br>

## Canny Edge Detection
Terdapat beberapa kelebihan pada algoritma Canny Edge Detection ini, antara lain:
1. Merupakan algoritma dengan tahap-tahap, dan berkesinambungan.
2. Noise reduction, dengan menggunakan 5x5 kernel Gaussian filter blur.
3. Finding Intensity Gradient of the Image, dengan menggunakan Sobel kernel secara horizontal dan vertikal. Dengan ini, akan didapat `edge gradient` dan arah dari setiap piksel. Arah gradien selalu tegak lurus dengan `edge`.
4. Non-maximum Suppression.
5. Hysteresis Thresholding.
 
Pada openCV, untuk melakukan Canny Edge Detection, fungsi yang digunakan adalah `cv.Canny()` dengan argumen yaitu minVal, maxVal (pada thresholding), apartureSize (ukuran kernel untuk Gaussian), dan L2gradient untuk menentukan persamaan gradien. Pada dokumentasi openCV, contoh baris kode penggunaan fungsi tersebut sebagai berikut.

`edges = cv.Canny(img, 100, 200)`

</br>

## Image Pyramids
Secara sederhana, materi Image Pyramids membahas tentang cara menurunkan atau menaikkan resolusi dari gambar, dengan ukuran (dimensi) yang sama. Fungsi yang digunakan adalah `cv.pyrUp()` dan `cv.pyrDown()`.

### Image Pyramids - Image Blending
Salah satu implementasi Image Pyramids adalah image blending. Dengan menggunakan Image Pyramids, penggabungan gambar yang dihasilkan akan lebih halus. Proses dalam Image Blending dengan Image Pyramids adalah sebagai berikut (gambar apel dan jeruk):
1. Input dua gambar, yaitu apel dan jeruk.
2. Temukan Gaussian Pyramid untuk apel dan jeruk (dalam contoh khusus ini, jumlah level adalah 6).
3. Dari Gaussian Pyramid, temukan Laplacian Pyramid.
4. Sekarang gabungkan separuh kiri apel dan separuh kanan jeruk di setiap level Laplacian Pyramid.
5. Akhirnya dari gambar bersama piramida ini, rekonstruksi gambar aslinya.

Terdapat beberapa hal yang harus diperhatikan dalam melakukan Image Blending ini berdasarkan pengalaman saya, yaitu:
1. Gambar harus berada di satu direktori yang sama.
2. Ukuran (height x width) kedua gambar harus sama.
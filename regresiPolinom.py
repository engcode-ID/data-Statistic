# Dibuat oleh: Cahya Amalinadhi Putra
# 2 Mei 2019, 11:59
# Code ini dapat disebarluaskan untuk tujuan pendidikan


"""
============================================================================== 
                                Regresi Polinom
============================================================================== 
Banyak keterbatasan dalam pencarian suatu nilai yang dihadapi oleh seorang
engineer nantinya. Misal, dalam melakukan eksperimen, engineer belum tentu
mendapat kesempatan menjalankan eksperimen pada semua nilai yang ingin dicari
akibat keterbatasan alat, waktu, sumber-daya, dan sebagainya.

Namun, hal ini tidak menjadikan engineer berhenti untuk berkarya dan
melakukan analisis lebih lanjut. Regresi hadir sebagai alat bantu engineer
untuk mengaproksimasi nilai pada titik yang tidak diketahui nilainya.

Misalkan kita memiliki data
(x, y) = 
	[(x1, y1),
	(x2, y2),
	(x3, y3),
	...
	...
	(xn, yn)]

dan kita ingin mencari nilai dari (x_p, y_p)

dengan regresi polinom, kita akan aproksimasi data (x, y) kedalam suatu fungsi
polinom sebagai berikut:
y = F(x) = a_0 x^m + a_1 x^(m-1) + a_2 x^(m-2) + ... + a_(m-1) x^1 + a_m

dan dengan cara inilah kita akan cari y_p = F(x_p)
==============================================================================

"""


class polynomialRegresion:

    def __init__(self, arrayX, arrayY):
        self.X = arrayX
        self.Y = arrayY
        self.n = len(arrayX)		# n adalah jumlah data

    def calculate(self, method='normal_equation', order=2):
        """
        Menghitung konstan dari persamaan polinom
        -----------------------------------------

        Persamaan polinom yang akan dibentuk adalah sebagai berikut
                y = F(x) = a_0 x^m + a_1 x^(m-1) + a_2 x^(m-2) + ... + a_(m-1) x^1 + a_m


        Parameter
        ---------
                metode	: 
                        - 'normal_equation' : mencari berdasarkan penurunan langsung regresi polinom
                                                                  referensi:
                                                                  http://polynomialregression.drque.net/math.html

                order	: derajat dari fungsi polinom (nilai m pada persamaan F(x))


        Langkah penyelesaian
        --------------------
        Akan diselesaikan matrix c untuk mencari nilai konstan polinom melalui persamaan berikut
        A.c = B
        c = inverse A . B

        """
        self.order = order

        # Buat matriks A dan B
        self.matriksA()
        self.matriksB()

        # Hitung matriks C
        self.matriksC()

        # Tampilkan persamaannya
        persamaan = ''
        for i in range(self.order):
            persamaan = persamaan + str(self.c[i]) + ' '
            if (i == self.order - 2):
                persamaan = persamaan + 'x'
            elif (i == self.order - 1):
                pass
            else:
                persamaan = persamaan + 'x^' + str(self.order - i - 1)
            if (i != self.order - 1):
                persamaan = persamaan + ' + '
            else:
                pass

        print('Persamaan regresi polinomnya adalah: ')
        print('F(x) = ' + persamaan)

    def fBar(self, x):
        hasil = 0
        for i in range(self.order):
            hasil = hasil + self.c[i] * (x**(self.order - i - 1))
        return (hasil)

    def matriksA(self):
        self.A = []
        for i in range(self.order):
            self.A.append([])
            for j in range(self.order):
                self.A[i].append(0)

        for i in range(self.order):
            for j in range(self.order):
                for k in range(self.n):
                    self.A[j][i] = self.A[j][i] + self.X[k]**(i + j)

    def matriksB(self):
        self.B = []
        temp = []
        for i in range(self.order):
            self.B.append(0)

        for i in range(self.order):
            for j in range(self.n):
                self.B[i] = self.B[i] + self.Y[j] * (self.X[j]**i)

    def matriksC(self):
        import numpy as np
        from numpy.linalg import inv
        A = np.array(self.A)
        B = np.array(self.B)
        invA = inv(A)
        c = np.dot(invA, B)

        self.c = []
        for i in range(len(c)):
            index = len(c) - i - 1
            self.c.append(c[index])

    def periksaNilai(self, x):
        hasil = self.fBar(x)

        print('Nilai dari F(' + str(x) + ') adalah ')
        print('F(' + str(x) + ') = ' + str(hasil))
        return (hasil)

    def plotPerbandingan(self):
        import matplotlib.pyplot as plt 	# library untuk memvisualkan grafis 2D

        self.yBar = []
        for i in range(len(self.X)):
            self.yBar.append(self.fBar(self.X[i]))

        plt.plot(self.X, self.Y, label='Fungsi Asli')
        plt.plot(self.X, self.yBar, label='Fungsi Regresi Polinom derajat ' + str(self.order-1))
        plt.legend()
        plt.show()


# ----- Langkah 01: Membaca Dataset -----
# Siapkan dataset yang ingin di regresi.
# Dataset bisa dibuat sendiri atau di-import menggunakan bantuan pandas

X = []
Y = []


# --- Buat dataset sendiri
def f(x):
	# Buat fungsi f(x) = x^2 + 3x + 2 + 2/x^3
	return (x**2 + 3*x + 2 + 2/x**3)

n = 10			# jumlah data
delta = 0.1		# selisih nilai antar data
for i in range(n):
	X.append((i+1)*delta)
	Y.append(f(X[i]))

'''
# --- Import dataset dari external file
import pandas as pd 	# library pandas digunakan untuk membaca file .csv

dataset = pd.read_csv('goldPrice.csv')
X = []
for i in range(len(dataset)):
    X.append(i)
Y = dataset.iloc[:, 1].values
'''

# Hilangkan simbol pagar (#) apabila ingin melihat nilai array X dan array Y
# print(X)
# print(Y)

# ----- Langkah 02: Eksekusi program -----
# Eksekusi program dengan menjalankan class polynomialRegression
run = polynomialRegresion(X, Y)
run.calculate(method='normal_equation', order=5)

run.plotPerbandingan()
#xYangDicari = 1
#run.periksaNilai(xYangDicari)

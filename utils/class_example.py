class NameClass(object):
	
	def perhitungan(self, nilai_a=None,nilai_b=None):
		jumlah = 0
		if type(nilai_a) is int:
			jumlah = nilai_a + nilai_b

		if nilai_a != 0 and nilai_b !=0:
			jumlah = nilai_a + nilai_b
		else:
			print "tetot"

		if nilai_a==1:
			jumlah = nilai_a + nilai_b
		elif nilai_b==2:
			print "okeee"
		else:
			print "salah"

		if nilai_a=="a":
			jumlah = nilai_a + nilai_b

		# if nilai_a > 1 :
		# 	jumlah = nilai_a + nilai_b
		# if type(nilai_a) is int:
		# 	jumlah = nilai_a + nilai_b
		# elif nilai_b==2:
		# 	print "okeee"
		# else 
		# 	print "salah"

		return "Nilai {a} + {b} = {jml}".format(
			a=nilai_a, b=nilai_b, jml=jumlah)

	def cetak_data(self, data=None):
		
		for item in data:
			print "Nama: ", item.get("Nama")
			print "Umur: ", item["Umur"]
			print "Alamat: ", item.get("Alamat")
			print "==========================="
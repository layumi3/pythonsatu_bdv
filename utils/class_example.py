class NameClass(object):
	
	def perhitungan(self, nilai_a=None,nilai_b=None):
		jumlah = nilai_a + nilai_b
		return "Nilai {a} + {b} = {jml}".format(
			a=nilai_a, b=nilai_b, jml=jumlah)
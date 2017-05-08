from utils import method_satu
from utils.class_example import NameClass

nama_class = NameClass()

list_dict =[
			{
				"Nama":"Jujju",
				"Umur":12,
				"Alamat":"Bandung"
			},
			{
				"Nama":"Jujju",
				"Umur":12,
				"Alamat":"Bandung"
			},
			{
				"Nama":"Jujju",
				"Umur":12,
				"Alamat":"Bandung"
			},
		]

print nama_class.perhitungan(nilai_a=0,nilai_b=4)

print method_satu(nama="Kokom")

nama_class.cetak_data(data=list_dict)
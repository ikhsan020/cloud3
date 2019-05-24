# -*- coding: utf-8 -*-
#rachmat_sn

import sqlite3
import json

conn = sqlite3.connect('mobilBekasOLX.db')
c = conn.cursor()

data = {} #dictionary
brand = ['Suzuki', 'Hyundai', 'Toyota']

#7 kota/kabupaten dengan penjual merek honda, yahama, suzuki, kawasaki terbanyak
query = c.execute("SELECT city FROM mobilBekas WHERE (brand LIKE '%"+brand[0]+"%' or brand LIKE '%"+brand[1]+"%' or brand LIKE '%"+brand[2]+"%') GROUP BY city ORDER BY COUNT(city) DESC LIMIT 7")
ftch = c.fetchall()
kab_kota = []
for i in range (len(ftch)):
    kab_kota.append(ftch[i][0])
data['labels'] = kab_kota

#'Suzuki', 'Hyundai', 'Toyota'
for i in range(len(kab_kota)):
    result = []
    for j in range(len(brand)):
        query = c.execute("SELECT count(brand) FROM mobilBekas WHERE brand LIKE '%"+brand[j]+"%' and city LIKE '%"+kab_kota[i]+"%'")
        ftch = c.fetchall()
        result.append(int(ftch[0][0]))
    data["k"+str(i+1)] = result

print(data)

#simpan file
with open('visualisasi_dictionary.txt', 'w') as fp:
    json.dump(data, fp)
    
c.close()
conn.close()

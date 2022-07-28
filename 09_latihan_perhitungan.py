#perhitungan konversi temperatur

"""
print ("PROGRAM KONVERSI TEMPERATUR")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("suhu dalam celcius adalah",celcius,"Celcius")

#reamure
reamur = (4/5)*celcius
print("suhu dalam reamur adalah",reamur,"Reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

#kelvin
kelvin = celcius+273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")
"""

print("\nTUGAS DARI BANG PUKIS"
      "\nKONVERSI FAHRENHEIT KE KELVIN DAN SEBALIKNYA")

fah = float(input("Masukkan suhu dalam fahrenheit: "))
cel = (5/9)*(fah-32)
kel = cel+273
print("suhu dalam fahrenheit",fah,"Fahrenheit")
print("suhu dalam kelvin",kel,"Kelvin")

kel1 = float(input("Masukkan suhu dalam Kelvin: "))
cel1 = kel1-273
fah1 = ((9/5)*cel1)+32
print("suhu dalam kelvin",kel1,"Kelvin")
print("suhu dalam fahrenheit",fah1,"Fahrenheit")
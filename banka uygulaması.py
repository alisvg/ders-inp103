bakiye = float(input("bakiye: "))

while True:
  print("1.para yatır")
  print("2.para çek")
  print("3. çık")
  
  secim = input("Seçim yapın: 1/2/3 ")

  if secim == "1":
    miktar = float(input("ne kadar yatıracaksın: "))
    bakiye = bakiye + miktar
    print("yeni bakiyen", bakiye)

  elif secim == "2":
    miktar =float(input("ne kadar çekeceksin: "))
    if miktar > bakiye:
      print("bakiyen yetersiz", bakiye)
    else:
      bakiye = bakiye - miktar
      print("Para çektin yeni bakiye", bakiye)

  elif secim == "3":
    print("çıktın")
    break

else:
  print("geçersiz")


  
  



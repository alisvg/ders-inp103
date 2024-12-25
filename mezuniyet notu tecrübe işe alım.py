mezuniyet = int(input("Mezuniyet notunuz: "))
tecrube = int(input("tecrübe derecesi (1/5): "))

if mezuniyet >= 70:
  print("işe alındın")
if mezuniyet <= 70:
  print ("sonra ararız")
elif mezuniyet < 70 and tecrube < 4:
  print("biz seni ararız")
elif mezuniyet >= 90 and terube < 4:
  print ("gel konuşalım")


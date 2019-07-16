import threading
import time
c= 0
def di():
  while 1:
    print("robot çalışıyor")
    time.sleep(1)
    if i == 'q':
      print("HOOOOPPP")
      break

def dii():
  while 1:
    print("sensör çalışıyor")
    time.sleep(1)
    if i == 'q' :
      print("HOOOOPPP")
      break
threads=[]
dall = threading.Thread(target = di)
dalla = threading.Thread(target = dii)
def main():
 global c
 global i
 i = None
 while i != 'q': 
  try:
   i = str(input(" Hangi dal ? (durdurmak için q ya basın)"))
   if i == '1':
     if c == 0:
       threads.append(dall)
       threads[c].start()
     else :
      threads.append(dall)
      threads[c].join()
   if i == '2':
    dalla.start()
  except KeyboardInterrupt:
   print(" HOOOOOOOOPP")
   break
j = None
main()

if i == 'q' and j != 's' :
 try:
  time.sleep(0.5)
  j = str(input(" Ne yapalım ? R = reset S = Shut Down"))
  if j== 'r':
    c += 1
    i = None
    main()
 except:
   print("HATA")
   raise

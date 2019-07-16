import threading
import time
i = None
def di():
  while 1:
    print("robot çalışıyor")
    time.sleep(1)
    if i == 'q':  # Usin flag to stop loop
      print("HOOOOPPP")
      break

def dii():
  while 1:
    print("sensör çalışıyor")
    time.sleep(1)
    if i == 'q' :   # Usin flag to stop loop
      print("HOOOOPPP")
      break

dall = threading.Thread(target = di)
dalla = threading.Thread(target = dii)
while i != 'q': 
  i = str(input(" Hangi dal ? (durdurmak için q ya basın)"))
  if i == '1':
    dall.start()
  if i == '2':
    dalla.start()

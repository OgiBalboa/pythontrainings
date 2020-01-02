import sqlite3

class Database():
  def __init__(self,):
    self.load()
    self.hata = False

  def load(self,):
    with sqlite3.connect("yeni.sqlite") as self.db:
      self.im = self.db.cursor()
      self.im.execute("""CREATE TABLE IF NOT EXISTS urunler (isim,alimfiyat,kargo)""")
  def add(self,isim,fiyat,kargo):
    self.im.execute("""SELECT * FROM urunler WHERE isim =?""",
    (isim,))
    self.flag = self.im.fetchall()

    if self.flag:
      self.hata = True
      self.info = "Ürün zaten bulunmakta !"
    else:
      self.im.execute("""INSERT INTO urunler VALUES (?,?,?)"""
    ,(isim,fiyat,kargo,))
      self.db.commit()   
      self.info = "Ürün başarıyla eklendi"

  def listall(self,):
    self.im.execute("""SELECT * FROM urunler""")
    self.veriler = self.im.fetchall()
    print(self.veriler)

  def search(self,x):
        self.im.execute("""SELECT kargo FROM urunler WHERE isim = ?""" ,(x,) )
        self.veriler = str(self.im.fetchone()).replace("('", "").replace("',)","").capitalize()

        print(self.veriler)

vt = Database()
"""
vt.add("Bmw","10","yolda")
vt.add("Mercedes","120","yok")
vt.add("Fluence","120","var")
"""
vt.listall()

print("*" * 60)

vt.search("Fluence")

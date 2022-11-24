nick = "utkuablak"
sifre = 112233

g1 = input("Kullanıcı adınızı giriniz: ")
g2 = int(input("Şifrenizi giriniz: "))
anapara = 10000

if g1 == "utkuablak":
    print("Kullanıcı adınız doğru")
else:
    print("Kullanıcı adınızı yanlış girdiniz")
    exit()
if g2 == 112233:
    print("Şifreniz doğru giriş başarılı")
else:
    print("Şifrenizi yanlış girdiniz")
    exit()

print("Anaparanız: " + str(anapara) + "TL")

sor = input("Para yatırmak için 1'e, para çekmek için 2'ye basınız: ")
if sor == "1":
    yatır = int(input("Yatırmak istediğiniz tutarı giriniz: "))
    anapara = anapara + yatır
    print("Anaparanız: " + str(anapara) + "TL")
elif sor == "2":
    cek = int(input("Çekmek istediğiniz tutarı giriniz: "))
    anapara = anapara - cek
    print("Anaparanız: " + str(anapara) + "TL")
else:
    print("Hatalı giriş yaptınız")
    exit()

## Açıklama

Bu repo son 1 ayda aşağıdaki her kategoride en iyi performans gösteren ilk 5 fonu csv şeklinde export etmenizi sağlayacak bir script'i barındırıyor. Repo'yu oluşturmamın sebebi genelde yatırım yapacağım zaman fonların son 1 ay, 3 ay, 6 ay, 1 yıl, 3 yıl, 5 yıl performanslarına bakmam.

Kategoriler:

* Altın
* Borçlanma Araçları
* Değişken
* Endeks
* Eurobond
* Hisse Senedi
* Katılım

## Bağımlılıklar (Dependencies)

Sadece Selenium'a ihtiyacınız var.

```
pip3 install selenium
```

## Nasıl Çalıştırırım

```
python3 parse.py
```

Script default olarak her kategorinin son 1 ayda en iyi performans gösteren ilk 5 fonunu veriyor. Eğer daha fazla ya da daha azını çekmek isterseniz --best-k argümanıyla değiştirebilirsiniz.  
## Driver versiyonları

Default olarak repo'da bulunan Chrome versiyonu Linux, Windows ve Mac için 85.0.4183

Başka bir Chrome versiyonu kullanıyorsanız, gerekli driver'ı [Chrome websitesinden](https://sites.google.com/a/chromium.org/chromedriver/downloads) indirdikten sonra driver'ın olduğu path'ı --driver-path argümanı ile verebilirsiniz.

# Paraşüt KDV Web Bot
## [TR]

Paraşüt KDV Web Bot projesi Python dili ile Selenium kütüphanesi kullanılarak yazılmıştır. Projenin çalıştırılabilmesi için Chrome tarayıcınıza uygun bir Chrome Web Driver indirilmesi gerekmektedir. Chrome version kontrolü yapılması önemlidir. Çoğunlukla rastlanan hata versiyondan kaynaklı hatalardır.

Proje'nin amacı yeni kanunla değişen KDV oranlarını ürün bazlı manuel değişikliğini bir Web Bot ile daha kısa vakitte hatasız ve otomatik bir şekilde gerçekleştirebilmektir. 

Son kullanıcılar için ürün ve hizmetler sayfasındaki ürünlerin toplu olarak KDV oranlarının değiştirilemiyor olmasından yola çıkılmış bir projedir. Gerçek yaşanmış bir probleme çözüm olarak yazılmış ve gerçek bir firmanın Paraşüt Muhasebe programı üzerinde  kullanılmıştır.

KDV oranı 10% olarak kodlanmıştır fakat bu küçük bir değişikle farklı KDV oranlarına geçişi sağlanabilmektedir.

**File**
"user.py" dosyası üzerinden Paraşüt Muhasebe programı giriş bilgilerinizi yazmanız gerekmektedir.

"main.py" dosyası içerisinde ana fonksiyonların çalıştığı sistem bulunmaktadır.

| Name | Version |
| ------ | ------ |
| Selenium | 4.10.0  |
| Python | 3.11.4 |
| Google Chrome | 114.0.5735.198 |

## [ENG]

The Paraşüt KDV Web Bot project is written in the Python language using the Selenium library. To run the project, you need to download a compatible Chrome Web Driver for your Chrome browser. It is important to check the Chrome version as many errors are often due to version compatibility issues.

The project aims to automate the manual process of changing VAT rates based on product categories, which were affected by new legislation. It was developed to address the issue of not being able to change VAT rates in bulk for products and services on the user interface. It was implemented and used by a real company on the Paraşüt Accounting program.

The default VAT rate is set to 10%, but it can be easily modified to accommodate different VAT rates with a small adjustment.

**File**
In the "user.py" file, you need to input your login credentials for the Paraşüt Accounting program.

The "main.py" file contains the core functionality and main functions of the system.

| Name | Version |
| ------ | ------ |
| Selenium | 4.10.0  |
| Python | 3.11.4 |
| Google Chrome | 114.0.5735.198 |

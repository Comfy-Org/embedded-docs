> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/tr.md)

Case Converter düğümü, metin dizilerini farklı harf büyüklüğü formatlarına dönüştürür. Bir giriş dizisi alır ve seçilen moda göre dönüştürerek, belirtilen büyük/küçük harf biçimlendirmesi uygulanmış bir çıkış dizisi üretir. Düğüm, metninizin büyük/küçük harf kullanımını değiştirmek için dört farklı büyük/küçük harf dönüşüm seçeneğini destekler.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | String | - | - | Farklı bir büyük/küçük harf formatına dönüştürülecek metin dizisi |
| `mode` | STRING | Combo | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | Uygulanacak büyük/küçük harf dönüşüm modu: UPPERCASE tüm harfleri büyük harfe dönüştürür, lowercase tüm harfleri küçük harfe dönüştürür, Capitalize yalnızca ilk harfi büyük yapar, Title Case her kelimenin ilk harfini büyük yapar |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Belirtilen büyük/küçük harf formatına dönüştürülmüş giriş dizisi |
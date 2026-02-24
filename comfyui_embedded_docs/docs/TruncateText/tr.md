> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/tr.md)

Bu düğüm, metni belirtilen maksimum uzunlukta keserek kısaltır. Herhangi bir giriş metnini alır ve ayarladığınız karakter sayısına kadar olan ilk kısmını döndürür. Metnin belirli bir boyutu aşmamasını sağlamanın basit bir yoludur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | Yok | Kısaltılacak metin dizisi. |
| `max_length` | INT | Hayır | 1 - 10000 | Maksimum metin uzunluğu. Metin bu kadar karakterden sonra kesilecektir (varsayılan: 77). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `string` | STRING | Kısaltılmış metin, girişten yalnızca ilk `max_length` karakterini içerir. |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

PreviewAny düğümü, herhangi bir giriş veri türünün önizlemesini metin formatında görüntüler. Herhangi bir veri türünü giriş olarak kabul eder ve görüntülenmek üzere okunabilir bir string temsiline dönüştürür. Düğüm, stringler, sayılar, booleanlar ve karmaşık nesneler dahil olmak üzere farklı veri türlerini bunları JSON formatına serileştirmeye çalışarak otomatik olarak işler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `kaynak` | ANY | Evet | Herhangi bir veri türü | Önizleme görüntüsü için herhangi bir giriş veri türünü kabul eder |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| UI Metin Görüntüsü | TEXT | Kullanıcı arayüzünde metin formatına dönüştürülmüş giriş verilerini görüntüler |
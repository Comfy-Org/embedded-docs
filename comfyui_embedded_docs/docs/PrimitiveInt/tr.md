> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/tr.md)

PrimitiveInt düğümü, iş akışınızda tamsayı değerleriyle çalışmak için basit bir yol sağlar. Bir tamsayı girdisi alır ve aynı değeri çıktı olarak verir, bu da düğümler arasında tamsayı parametreleri aktarmak veya diğer işlemler için belirli sayısal değerler ayarlamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `değer` | INT | Evet | -9223372036854775807 ile 9223372036854775807 arası | Çıktılanacak tamsayı değeri |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | INT | Değiştirilmeden aktarılan girdi tamsayı değeri |
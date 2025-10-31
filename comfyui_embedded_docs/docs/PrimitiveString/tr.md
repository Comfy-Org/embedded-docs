> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveString/tr.md)

String düğümü, iş akışınızda metin verilerini girmek ve iletmek için basit bir yol sağlar. Bir metin dizesini girdi olarak alır ve aynı dizeyi değiştirmeden çıktı olarak verir, bu da metin dizesi parametrelerine ihtiyaç duyan diğer düğümlere metin girdisi sağlamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Evet | Herhangi bir metin | Düğüm üzerinden iletilmek üzere olan metin dizesi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Girdi olarak sağlanan aynı metin dizesi |
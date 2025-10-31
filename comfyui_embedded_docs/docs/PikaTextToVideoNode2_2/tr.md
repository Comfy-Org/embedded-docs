> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/tr.md)

Pika Text2Video v2.2 Düğümü, bir video oluşturmak için bir metin istemini Pika API sürüm 2.2'ye gönderir. Metin açıklamanızı Pika'nın AI video oluşturma hizmetini kullanarak bir videoya dönüştürür. Düğüm, en-boy oranı, süre ve çözünürlük dahil olmak üzere video oluşturma sürecinin çeşitli yönlerini özelleştirmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem_metni` | STRING | Evet | - | Videoda oluşturmak istediğiniz içeriği tanımlayan ana metin açıklaması |
| `negatif_istem` | STRING | Evet | - | Oluşturulan videoda görünmesini istemediğiniz unsurları tanımlayan metin |
| `tohum` | INT | Evet | - | Tekrarlanabilir sonuçlar için oluşturmanın rastgeleliğini kontrol eden bir sayı |
| `çözünürlük` | STRING | Evet | - | Çıktı videosu için çözünürlük ayarı |
| `süre` | INT | Evet | - | Videoyun saniye cinsinden uzunluğu |
| `en_boy_oranı` | FLOAT | Hayır | 0.4 - 2.5 | En-boy oranı (genişlik / yükseklik) (varsayılan: 1.7777777777777777) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Pika API'sinden döndürülen oluşturulmuş video dosyası |
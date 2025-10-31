> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/tr.md)

StringCompare düğümü, iki metin dizesini farklı karşılaştırma yöntemleri kullanarak karşılaştırır. Bir dizenin diğeriyle başlayıp başlamadığını, diğeriyle bitip bitmediğini veya her iki dizenin tam olarak eşit olup olmadığını kontrol edebilir. Karşılaştırma, harf büyüklüğü/küçüklüğü farklılıkları dikkate alınarak veya alınmayarak gerçekleştirilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Evet | - | Karşılaştırılacak ilk dize |
| `string_b` | STRING | Evet | - | Karşılaştırma yapılacak ikinci dize |
| `mode` | COMBO | Evet | "Starts With"<br>"Ends With"<br>"Equal" | Kullanılacak karşılaştırma yöntemi |
| `case_sensitive` | BOOLEAN | Hayır | - | Karşılaştırma sırasında harf büyüklüğünün/küçüklüğünün dikkate alınıp alınmayacağı (varsayılan: true) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Karşılaştırma koşulu sağlanıyorsa true, aksi takdirde false döndürür |
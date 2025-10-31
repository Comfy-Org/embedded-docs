> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/tr.md)

MiniMax Hailuo-02 modelini kullanarak metin istemlerinden video oluşturur. İsteğe bağlı olarak, videonun bu görüntüden devam etmesini sağlamak için ilk kare olarak kullanılmak üzere bir başlangıç görüntüsü sağlayabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin istemi. |
| `seed` | INT | Hayır | 0 ile 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). |
| `first_frame_image` | IMAGE | Hayır | - | Videoyu oluşturmak için ilk kare olarak kullanılacak isteğe bağlı görüntü. |
| `prompt_optimizer` | BOOLEAN | Hayır | - | Gerektiğinde oluşturma kalitesini artırmak için istemi optimize eder (varsayılan: True). |
| `duration` | COMBO | Hayır | `6`<br>`10` | Çıktı videosunun saniye cinsinden uzunluğu (varsayılan: 6). |
| `resolution` | COMBO | Hayır | `"768P"`<br>`"1080P"` | Video ekranının boyutları. 1080p 1920x1080, 768p ise 1366x768'dir (varsayılan: "768P"). |

**Not:** MiniMax-Hailuo-02 modeli 1080P çözünürlükte kullanıldığında, süre 6 saniye ile sınırlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
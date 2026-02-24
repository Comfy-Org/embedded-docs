> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/tr.md)

Bu düğüm, Kling 3.0 modelini kullanarak bir video oluşturur. Videoyu bir metin istemi, belirtilen bir süre ve sağlanan iki görüntü (başlangıç karesi ve bitiş karesi) temelinde üretir. Düğüm ayrıca video için eşlik eden ses de oluşturabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Video oluşturmayı yönlendiren metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. |
| `duration` | INT | Hayır | 3 ila 15 | Video uzunluğu saniye cinsinden (varsayılan: 5). |
| `first_frame` | IMAGE | Evet | Yok | Video için başlangıç görüntüsü. En az 300x300 piksel olmalı ve en boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |
| `end_frame` | IMAGE | Evet | Yok | Video için bitiş görüntüsü. En az 300x300 piksel olmalı ve en boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |
| `generate_audio` | BOOLEAN | Hayır | Yok | Video için ses oluşturulup oluşturulmayacağını kontrol eder (varsayılan: True). |
| `model` | COMBO | Hayır | `"kling-v3"` | Model ve oluşturma ayarları. Bu seçeneği belirlemek, iç içe bir `resolution` parametresini görünür kılar. |
| `model.resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Oluşturulan video için çözünürlük. Bu parametre yalnızca `model` `"kling-v3"` olarak ayarlandığında kullanılabilir. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için kullanılan bir sayı. Sonuçlar, seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). |

**Not:** `first_frame` ve `end_frame` görüntülerinin, düğümün doğru çalışması için belirtilen minimum boyut ve en boy oranı gereksinimlerini karşılaması gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

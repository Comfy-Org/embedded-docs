> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/en.md)

Grok Video Uzatma düğümü, mevcut bir videonun kesintisiz devamını oluşturmak için bir yapay zeka modeli kullanır. Kısa bir video ve bundan sonra ne olması gerektiğini açıklayan bir metin istemi sağlarsınız; düğüm, orijinal videoyu takip eden yeni bir video klibi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `prompt` | STRING | Evet | Yok | Videoda bundan sonra ne olması gerektiğine dair metin açıklaması. |
| `video` | VIDEO | Evet | Yok | Uzatılacak kaynak video. MP4 formatı, 2-15 saniye. |
| `model` | COMBO | Evet | `"grok-imagine-video"` | Video uzatma için kullanılacak model. Seçildiğinde, bir `duration` parametresini ortaya çıkarır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar, tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). |

**Parametre Kısıtlamaları:**
*   `video` girişi, 2 ila 15 saniye uzunluğunda bir MP4 dosyası olmalı ve dosya boyutu 50MB'ı geçemez.
*   `prompt` en az bir karakter içermelidir (boşluklar kırpılır).
*   `model` parametresi dinamik bir birleşik kutudur. "grok-imagine-video" seçeneğinin seçilmesi, uzatmanın saniye cinsinden uzunluğunu kontrol eden iç içe bir `duration` parametresini ortaya çıkarır (varsayılan: 8, aralık: 2 ila 10).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Yeni oluşturulan video uzantısı. |
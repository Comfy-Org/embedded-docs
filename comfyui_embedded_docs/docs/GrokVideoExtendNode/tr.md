> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/tr.md)

Bu, mevcut bir videonun kesintisiz devamını oluşturmak için bir yapay zeka modeli kullanan bir düğümdür. Kısa bir video ve ardından ne olması gerektiğini açıklayan bir metin istemi sağlarsınız; düğüm, orijinalin devamı niteliğinde yeni bir video klibi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Videoda daha sonra ne olması gerektiğine dair metin açıklaması. |
| `video` | VIDEO | Evet | Yok | Uzatılacak kaynak video. MP4 formatı, 2-15 saniye. |
| `model` | COMBO | Evet | `"grok-imagine-video"` | Video uzatma için kullanılacak model. Seçildiğinde, iç içe geçmiş bir `duration` parametresini ortaya çıkarır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar, tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). |

**Parametre Kısıtlamaları:**
*   `video` girişi, 2 ila 15 saniye uzunluğunda bir MP4 dosyası olmalı ve dosya boyutu 50MB'ı geçemez.
*   `prompt` en az bir karakter içermelidir (boşluklar kırpılır).
*   `model` parametresi dinamik bir kombinasyon kutusudur. "grok-imagine-video" seçeneğinin seçilmesi, uzatmanın saniye cinsinden uzunluğunu kontrol eden iç içe geçmiş bir `duration` parametresini ortaya çıkarır (varsayılan: 8, aralık: 2 ile 10).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Yeni oluşturulan video uzantısı. |

---
**Source fingerprint (SHA-256):** `a33383be0eb6857538a75e1b901ee58df0153dfeaf95a7ee19933d651b745b5f`

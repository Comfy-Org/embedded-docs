# VEED Remove Video Background

VEED ile bir videodaki özneyi kesip çıkarın ve kareleri bir alfa maskesiyle birlikte döndürün. İki çıktıyı kompozitleme için kullanın veya saydam bir video yazmak için bunları Join Image with Alpha ve Save WEBM düğümlerinden geçirin. Herhangi bir arka planda en iyi kenarlar için `"standard"`, hız önemli olduğunda `"fast"` veya yeşil bir perde önünde çekilmiş görüntüler için `"green screen"` seçeneğini seçin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak segmentasyon modeli: herhangi bir arka plan için en iyi kenarlarla ve 3840x2160'e kadar çıktıyla `"standard"`, 1920x1080'e kadar daha hızlı sonuç için `"fast"` veya 3840x2160'e kadar yeşil arka planı ayıklamak için `"green screen"`. Daha büyük videolar küçültülür. Bir seçenek seçildiğinde ilgili parametreler görünür. | DYNAMIC_COMBO | Evet | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | Öznenin kesilip çıkarılacağı video. En fazla 60 saniye. | VIDEO | Evet | En fazla 60 saniye |
| `refine_foreground_edges` | Saç, kürk ve ince ayrıntılarda daha temiz kenarlar. Kapatıldığında fiyat düşer. `"standard"` ve `"fast"` için kullanılabilir (varsayılan: True). | BOOLEAN | Evet | false<br>true |
| `subject_is_person` | Özne bir nesne veya hayvan olduğunda kapatın. `"standard"` ve `"fast"` için kullanılabilir (varsayılan: True). | BOOLEAN | Evet | false<br>true |
| `spill_suppression_strength` | Özneden yeşil renk taşmasının ne kadar güçlü kaldırılacağı. Yeşil lekeler kaldığında artırın; öznenin renkleri kaydığında azaltın. `"green screen"` için kullanılabilir (varsayılan: 0.8). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

Klip 60 saniyeyle sınırlıdır; daha uzun videolar hatayla reddedilir. Maske, arka planın kaldırıldığı yerlerde 1'dir; bu nedenle özneyi korumak istediğinizde Image Composite Masked öncesinde Invert Mask kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Arka planı kaldırılmış video kareleri. | IMAGE |
| `mask` | Her kare için arka planın kaldırıldığı yerlerde 1. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`

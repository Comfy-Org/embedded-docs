# Bria Guided Remove Background

Bu düğüm, Bria ile bir görüntünün arka planını kaldırır ve istemin tanımladığı şeyi korur. Orijinal pikseller yeniden oluşturulmak yerine yeni bir alfa kanalıyla tam çözünürlükte geri döner; böylece ince ayrıntılar ve kenarlar korunur. Hiçbir şeyle eşleşmeyen bir istem, tamamen saydam bir görüntü döndürür. Rehberlik olmadan düz bir kesme için Bria Remove Image Background daha düşük maliyetlidir.

## Girdiler

`moderation` seçicisi `"true"` olarak ayarlandığında ek moderasyon seçeneklerini ortaya çıkarır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Kesilecek görüntü. | IMAGE | Evet | - |
| `prompt` | Neyin tutulacağı ve isteğe bağlı olarak neyin çıkarılacağı veya neye daraltılacağı; örneğin 'the person with the mat and the plant', 'the woman at her desk without the lamp' ya da 'only the chair'. Boş olamaz. İstemle hiçbir şey eşleşmezse sonuç tamamen saydam olur. Varsayılan: `""` (boş dize). | STRING | Evet | 1 karakter veya daha fazla |
| `moderation` | Moderasyon ayarları. `"true"` olarak ayarlandığında aşağıdaki görsel moderasyon bayrakları kullanılabilir hale gelir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon "true" Girdileri

Bu parametreler yalnızca `moderation` `"true"` olarak ayarlandığında görünür. `"false"` seçeneği ek girdi eklemez.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: `False`. | BOOLEAN | Hayır | True / False |
| `visual_output_moderation` | Oluşturulan görüntüde içerik moderasyonunu etkinleştirir. Varsayılan: `False`. | BOOLEAN | Hayır | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Kesilmiş görüntü: yeni bir alfa kanalına sahip orijinal pikseller. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/tr.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`

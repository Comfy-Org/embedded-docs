# Koşullandırma (Maske Ayarla)

Bu düğüm, belirtilen bir güçle belirli alanlara maske uygulayarak üretken bir modelin koşullandırmasını değiştirmek için tasarlanmıştır. Koşullandırma içinde hedefli ayarlamalar yapılmasını sağlayarak üretim süreci üzerinde daha hassas kontrol imkanı sunar.

## Girişler

### Zorunlu

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Değiştirilecek koşullandırma verisi. Maske ve güç ayarlamalarının uygulanması için temel oluşturur. | CONDITIONING |
| `maske` | Koşullandırma içinde değiştirilecek alanları belirten bir maske tensörü. | `MASK` |
| `güç` | Maskenin koşullandırma üzerindeki etkisinin gücü; uygulanan değişikliklerin ince ayarının yapılmasına olanak tanır. | `FLOAT` |
| `koşul_alanı_ayarla` | Maskenin etkisinin varsayılan alana mı yoksa maskenin kendisiyle sınırlı bir alana mı uygulanacağını belirler; belirli bölgeleri hedeflemede esneklik sağlar. | COMBO[STRING] |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Maske ve güç ayarlamaları uygulanmış, değiştirilmiş koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/tr.md)

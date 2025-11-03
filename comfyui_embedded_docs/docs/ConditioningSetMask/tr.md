> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/tr.md)

Bu düğüm, bir üretken modelin koşullandırmasını, belirli alanlara belirli bir güçte maske uygulayarak değiştirmek için tasarlanmıştır. Koşullandırma içinde hedeflenen ayarlamalara olanak tanıyarak, üretim süreci üzerinde daha hassas kontrol sağlar.

## Girdiler

### Zorunlu

| Parametre     | Veri Tipi    | Açıklama |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma verisi. Maske ve güç ayarlamalarının uygulanması için temel oluşturur. |
| `maske`        | `MASK`       | Koşullandırmada değiştirilecek alanları belirten bir maske tensörü. |
| `güç`    | `FLOAT`      | Koşullandırma üzerindeki maskenin etki gücü; uygulanan değişikliklerin ince ayarına olanak tanır. |
| `koşul_alanı_ayarla` | COMBO[STRING] | Maskenin etkisinin varsayılan alana mı yoksa maskenin kendisi tarafından sınırlanan alana mı uygulanacağını belirler; belirli bölgeleri hedeflemede esneklik sunar. |

## Çıktılar

| Parametre     | Veri Tipi    | Açıklama |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Maske ve güç ayarlamaları uygulanmış, değiştirilmiş koşullandırma verisi. |
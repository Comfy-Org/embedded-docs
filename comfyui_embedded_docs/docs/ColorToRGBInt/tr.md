# Renkten RGB Tam Sayıya

**ColorToRGBInt** düğümü, onaltılık biçimde verilen bir rengi (örn. `#FF5733`) tek bir RGB tamsayı değerine dönüştürür. Renk dizesindeki kırmızı, yeşil ve mavi bileşenleri çıkarır, bunları tek bir tamsayıda birleştirir ve ayrıca orijinal onaltılık gösterimi ile alfa (opaklık) değerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `renk` | `#RRGGBB` veya `#RRGGBBAA` onaltılık biçiminde bir renk değeri. 7 veya 9 karakter uzunluğunda olmalı ve `#` ile başlamalıdır. | COLOR | Evet | `#RRGGBB`<br>`#RRGGBBAA` |

**Not:** Girdi `color` dizesi `#RRGGBB` veya `#RRGGBBAA` biçimini izlemelidir. 7 veya 9 karakter uzunluğunda değilse, `#` ile başlamıyorsa veya geçersiz onaltılık karakterler içeriyorsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `rgb_tam_sayı` | `(Kırmızı * 65536) + (Yeşil * 256) + Mavi` formülünden türetilen hesaplanmış RGB tamsayı değeri. | INT |
| `hex` | `#RRGGBB` biçimindeki onaltılık renk dizesi. Girdi bir alfa kanalı içeriyorsa, bu çıktıdan çıkarılır. | COLOR |
| `alpha` | 0.0 ile 1.0 arasındaki alfa (opaklık) değeri. Girdi `#RRGGBB` olduğunda 1.0'a eşittir; girdi `#RRGGBBAA` olduğunda alfa kanalı değerinin 255'e bölünmesiyle elde edilir. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/tr.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`

# Renkten RGB Tam Sayıya

**ColorToRGBInt** düğümü, onaltılık biçimde belirtilen bir rengi (ör. `#FF5733`) tek bir RGB tamsayı değerine dönüştürür. Renk dizesindeki kırmızı, yeşil ve mavi bileşenleri alır, bunları tek bir tamsayıda birleştirir ve onaltılık gösterimi döndürür. Alfa kanallı renkler (`#RRGGBBAA`) de desteklenir ve alfa değeri ayrı olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `color` | `#RRGGBB` veya `#RRGGBBAA` onaltılık biçiminde bir renk değeri. Tam olarak 7 veya 9 karakter uzunluğunda olmalı ve `#` ile başlamalıdır. | COLOR | Evet | `#RRGGBB`<br>`#RRGGBBAA` |

**Not:** `color` girdi dizesi tam olarak `#RRGGBB` veya `#RRGGBBAA` biçiminde olmalıdır. Dize 7 veya 9 karakter uzunluğunda değilse, `#` ile başlamıyorsa veya geçerli onaltılık basamaklar olmayan karakterler içeriyorsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `rgb_int` | `(Red * 65536) + (Green * 256) + Blue` formülüyle hesaplanan RGB tamsayı değeri. | INT |
| `hex` | `#RRGGBB` biçiminde onaltılık renk dizesi. Girdi bir alfa kanalı içeriyorsa, bu çıktıdan çıkarılır. | COLOR |
| `alpha` | 0.0 ile 1.0 arasında bir sayı olarak alfa (opaklık) değeri. Alfa kanallı (`#RRGGBBAA`) girdi renkleri için, iki basamaklı alfa değerinin 255'e bölünmesidir. Alfa kanalı olmayan renkler için 1.0'dır. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/tr.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`

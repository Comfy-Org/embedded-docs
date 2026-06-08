ColorToRGBInt düğümü, onaltılık (hexadecimal) formatta belirtilen bir rengi tek bir tamsayı değerine dönüştürür. `#FF5733` gibi bir renk dizesi alır ve kırmızı, yeşil ve mavi bileşenlerini birleştirerek karşılık gelen RGB tamsayısını hesaplar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `renk` | `#RRGGBB` onaltılık formatında bir renk değeri. | STRING | Evet | Yok |

**Not:** Giriş `color` dizesi tam olarak 7 karakter uzunluğunda olmalı ve bir `#` sembolü ile başlamalı, ardından altı onaltılık basamak gelmelidir (örneğin, kırmızı için `#FF0000`). Format hatalıysa düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `rgb_int` | Hesaplanan RGB tamsayı değeri. Bu değer şu formülden türetilir: `(Kırmızı * 65536) + (Yeşil * 256) + Mavi`. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/tr.md)

---
**Source fingerprint (SHA-256):** `5b8617d6b28caaa5f01dad1c6a302fa321f1bd53a0454451d468e36747e70e8f`

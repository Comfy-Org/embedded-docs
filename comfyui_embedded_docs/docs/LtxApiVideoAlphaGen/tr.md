# LTX Video AlphaGen

Ön planın beyaz olduğu, girdi videosuyla kare kare eşleşen gri tonlamalı bir alfa matı çıkarır. Matı bir maskeye dönüştürmek için Get Video Components ve Image To Mask düğümlerine besleyin. Ses korunmaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Matı çıkarılacak video; her iki yönde de en fazla 10 saniye ve 3840x2160 olabilir. | VIDEO | Evet | - |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `matte` | Video olarak alfa matı; her girdi karesi için bir kare içerir ve ses içermez. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/tr.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`

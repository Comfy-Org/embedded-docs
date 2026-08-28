# Anahtar

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar` | Hangi girdinin iletileceğini belirleyen bir boolean koşuldur. Etkin olduğunda (true), `on_true` girdisi seçilir. Devre dışı olduğunda (false), `on_false` girdisi seçilir. | BOOLEAN | Evet |  |
| `yanlışta` | `switch` devre dışıyken (false) çıktıya iletilecek veridir. Bu girdi yalnızca `switch` false olduğunda gereklidir. | MATCH_TYPE | Hayır |  |
| `doğruda` | `switch` etkinken (true) çıktıya iletilecek veridir. Bu girdi yalnızca `switch` true olduğunda gereklidir. | MATCH_TYPE | Hayır |  |

**Girdi Gereksinimleri Notu:** `on_false` ve `on_true` girdileri koşullu olarak gereklidir. Düğüm, `on_true` girdisini yalnızca `switch` true olduğunda, `on_false` girdisini ise yalnızca `switch` false olduğunda isteyecektir. Her iki girdi de aynı veri türünde olmalı ve çıktı veri türüyle eşleşmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `çıktı` | Seçilen veridir. `switch` true olduğunda `on_true` girdisinden, `switch` false olduğunda `on_false` girdisinden alınan değerdir. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`

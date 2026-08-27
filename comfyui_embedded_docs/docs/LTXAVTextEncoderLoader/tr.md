# LTXV Sesli Metin Kodlayıcı Yükleyici

This düğüm, LTXV ses modeli için özel bir metin kodlayıcı yükler. Ses üretiminde metin koşullandırma için kullanılan bir CLIP modeli oluşturmak üzere bir metin kodlayıcı dosyasını bir checkpoint dosyasıyla birleştirir. Düğüm açıklamasına göre metin kodlayıcı, Gemma 3 12B veya uyumlu bir Gemma 4 modeli olmalıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `text_encoder` | Yüklenecek LTXV metin kodlayıcı modelinin dosya adı. Kullanılabilir seçenekler `text_encoders` klasöründen yüklenir. | COMBO | Evet | Birden fazla seçenek mevcut |
| `ckpt_name` | Yüklenecek checkpoint dosyasının adı. Kullanılabilir seçenekler `checkpoints` klasöründen yüklenir. | COMBO | Evet | Birden fazla seçenek mevcut |
| `device` | Modelin yükleneceği cihazı belirtir. CPU'ya yüklemeyi zorunlu kılmak için `"cpu"` kullanın. Varsayılan davranış (`"default"`) sistemin otomatik cihaz yerleşimini kullanır (varsayılan: `"default"`). Bu gelişmiş bir parametredir. | COMBO | Hayır | `"default"`<br>`"cpu"` |

**Not:** `text_encoder` ve `ckpt_name` parametreleri birlikte çalışır. Düğüm, tek ve işlevsel bir CLIP modeli oluşturmak için belirtilen her iki dosyayı da yükler. Dosyalar LTXV mimarisiyle uyumlu olmalı ve metin kodlayıcı, Gemma 3 12B veya uyumlu bir Gemma 4 modeli olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Yüklenen LTXV CLIP modeli; ses üretimi için metin istemlerini kodlamak amacıyla kullanıma hazırdır. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/tr.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`

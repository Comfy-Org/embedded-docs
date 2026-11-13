# Split Image Channels

Bir görüntüyü kırmızı, yeşil ve mavi kanallarına ayırır ve alfa kanalını maske olarak döndürür. Her renk çıktısı üç kanallı gri tonlamalı bir görüntüdür; bu nedenle normal bir görüntü gibi önizlenebilir ve kaydedilebilir. Tek bir kanalı incelemek veya düzenlemek ya da bir görüntüden saydamlığı çıkarmak için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Bölünecek görüntü. Tek kanallı (gri tonlamalı) bir girdi, üç renk çıktısının da aynı veriyi taşıması için genişletilir. | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `red` | Kırmızı kanal, üç kanallı gri tonlamalı görüntü olarak. | IMAGE |
| `green` | Yeşil kanal, üç kanallı gri tonlamalı görüntü olarak. | IMAGE |
| `blue` | Mavi kanal, üç kanallı gri tonlamalı görüntü olarak. | IMAGE |
| `alpha` | Maske olarak alfa; Load Image ile aynı şekilde ters çevrilir, böylece 1 tamamen saydam pikselleri işaret eder. Alfa kanalı olmayan bir görüntü, tümü sıfır olan bir maske döndürür. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/tr.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`

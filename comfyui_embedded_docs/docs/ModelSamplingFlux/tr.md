# ModelÖrneklemeFlux

ModelSamplingFlux düğümü, görüntü boyutlarına dayalı olarak bir shift parametresi hesaplayarak belirli bir modele Flux model örneklemesi uygular. Belirtilen genişlik, yükseklik ve shift parametrelerine göre modelin davranışını ayarlayan özel bir örnekleme yapılandırması oluşturur ve ardından yeni örnekleme ayarları uygulanmış değiştirilmiş modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Flux örneklemesinin uygulanacağı model | MODEL | Evet | - |
| `maks_kaydırma` | Örnekleme hesaplaması için maksimum shift değeri (varsayılan: 1.15) | FLOAT | Evet | 0.0 - 100.0 (adım 0.01) |
| `temel_kaydırma` | Örnekleme hesaplaması için temel shift değeri (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 (adım 0.01) |
| `genişlik` | Hedef görüntünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION (adım 8) |
| `yükseklik` | Hedef görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION (adım 8) |

`max_shift` ve `base_shift` gelişmiş parametrelerdir. Örnekleme yapılandırmasına uygulanan shift, görüntü boyutlarından hesaplanır: latent çözünürlük `width × height / 256` olarak hesaplanır ve shift değeri, 256 latent çözünürlüğündeki `base_shift` ile 4096 latent çözünürlüğündeki `max_shift` arasında enterpole edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Flux örnekleme yapılandırması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/tr.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`

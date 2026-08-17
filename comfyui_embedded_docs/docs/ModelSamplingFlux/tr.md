# ModelÖrneklemeFlux

ModelSamplingFlux düğümü, görüntü boyutlarına dayalı olarak bir kaydırma (shift) parametresi hesaplayarak belirli bir modele Flux model örneklemesi uygular. Belirtilen genişlik, yükseklik ve kaydırma parametrelerine göre modelin davranışını ayarlayan özel bir örnekleme yapılandırması oluşturur ve yeni örnekleme ayarları uygulanmış değiştirilmiş modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Flux örneklemesinin uygulanacağı model | MODEL | Evet | - |
| `max_shift` | Örnekleme hesaplaması için maksimum kaydırma değeri (varsayılan: 1.15) | FLOAT | Evet | 0.0 - 100.0 |
| `base_shift` | Örnekleme hesaplaması için temel kaydırma değeri (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 |
| `width` | Hedef görüntünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |
| `height` | Hedef görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |

Etkin kaydırma değeri, `width` ve `height` değerlerinden türetilen latent boyuta göre `base_shift` ile `max_shift` arasında enterpolasyon yapılarak hesaplanır. `step` değeri `max_shift` ve `base_shift` için 0.01, `width` ve `height` için 8'dir. `max_shift` ve `base_shift` parametreleri kullanıcı arayüzünde gelişmiş seçenekler olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Flux örnekleme yapılandırması uygulanarak değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/tr.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`

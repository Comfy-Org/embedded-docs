ModelSamplingFlux düğümü, görüntü boyutlarına dayalı bir kaydırma parametresi hesaplayarak belirtilen modele Flux model örneklemesi uygular. Belirtilen genişlik, yükseklik ve kaydırma parametrelerine göre modelin davranışını ayarlayan özelleştirilmiş bir örnekleme yapılandırması oluşturur ve ardından yeni örnekleme ayarları uygulanmış değiştirilmiş modeli döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Flux örneklemesinin uygulanacağı model | MODEL | Evet | - |
| `maks_kaydırma` | Örnekleme hesaplaması için maksimum kaydırma değeri (varsayılan: 1.15) | FLOAT | Evet | 0.0 - 100.0 |
| `temel_kaydırma` | Örnekleme hesaplaması için temel kaydırma değeri (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 |
| `genişlik` | Hedef görüntünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Hedef görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 16 - MAX_RESOLUTION |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Flux örnekleme yapılandırması uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/tr.md)

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`

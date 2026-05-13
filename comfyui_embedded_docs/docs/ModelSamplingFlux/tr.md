> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/tr.md)

ModelSamplingFlux düğümü, görüntü boyutlarına dayalı bir kaydırma parametresi hesaplayarak belirtilen modele Flux model örneklemesi uygular. Belirtilen genişlik, yükseklik ve kaydırma parametrelerine göre modelin davranışını ayarlayan özelleştirilmiş bir örnekleme yapılandırması oluşturur ve ardından yeni örnekleme ayarları uygulanmış değiştirilmiş modeli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Flux örneklemesinin uygulanacağı model |
| `max_shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme hesaplaması için maksimum kaydırma değeri (varsayılan: 1.15) |
| `base_shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme hesaplaması için temel kaydırma değeri (varsayılan: 0.5) |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Hedef görüntünün piksel cinsinden genişliği (varsayılan: 1024) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Hedef görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Flux örnekleme yapılandırması uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`

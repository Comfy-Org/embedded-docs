> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/tr.md)

ModelSamplingFlux düğümü, görüntü boyutlarına dayalı olarak bir kaydırma parametresi hesaplayarak belirli bir modele Flux model örneklemesi uygular. Modelin davranışını belirtilen genişlik, yükseklik ve kaydırma parametrelerine göre ayarlayan özelleştirilmiş bir örnekleme yapılandırması oluşturur ve ardından yeni örnekleme ayarları uygulanmış şekilde değiştirilmiş modeli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Flux örneklemesi uygulanacak model |
| `max_shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme hesaplaması için maksimum kaydırma değeri (varsayılan: 1.15) |
| `base_shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme hesaplaması için temel kaydırma değeri (varsayılan: 0.5) |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Hedef görüntünün piksel cinsinden genişliği (varsayılan: 1024) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Hedef görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Flux örnekleme yapılandırması uygulanmış değiştirilmiş model |
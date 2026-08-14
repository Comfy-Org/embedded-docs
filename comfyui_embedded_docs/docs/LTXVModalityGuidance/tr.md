# LTXVModalityGuidance

Bu düğüm, bir LTXV-AV modeline çapraz mod (ses-video) yönlendirmesi uygular. Örnekleme sırasında, sesden videoya ve videodan sese çapraz dikkat bağlantıları devre dışı bırakılmış şekilde her adımda bir ekstra ileri geçiş çalıştırır ve sonucu birleşik tahmine doğru iter. Bu, dudak senkronizasyonu gibi görsel-işitsel senkronizasyonu güçlendirir. `modality_scale` için referans varsayılan değer 3.0'dır; 1.0 olarak ayarlamak ekstra geçişi devre dışı bırakır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üzerine modalite yönlendirmesi uygulanacak temel model. Dahili olarak klonlanır ve orijinal model değişmeden bırakılır. | MODEL | Evet | - |
| `modality_scale` | Ses-video birleştirme yönlendirmesinin gücü. Varsayılan 3.0'dır. Ekstra ileri geçişi devre dışı bırakmak için 1.0 olarak ayarlayın. | FLOAT | Evet | 1.0 ile 100.0 arası (default: 3.0) |
| `start_percent` | Modalite yönlendirmesinin başladığı örnekleme sürecindeki nokta (0.0 ile 1.0 arasında bir yüzde). Varsayılan 0.0'dır. | FLOAT | Evet | 0.0 ile 1.0 arası (default: 0.0) |
| `end_percent` | Modalite yönlendirmesinin sona erdiği örnekleme sürecindeki nokta (0.0 ile 1.0 arasında bir yüzde). Varsayılan 1.0'dır. | FLOAT | Evet | 0.0 ile 1.0 arası (default: 1.0) |

Yönlendirme yalnızca sigma değerleri `start_percent` ve `end_percent` tarafından tanımlanan aralığa giren örnekleme adımlarına uygulanır. Bu aralığın dışında, düğüm gürültüsü giderilmiş sonucu değiştirmeden döndürür. `modality_scale` değerinin 1.0 olması ayrıca ekstra ileri geçişi tamamen devre dışı bırakır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Üzerine CFG sonrası yönlendirme işlevi eklenmiş klonlanmış model. Bu değiştirilmiş model, örnekleme sırasında modalite yönlendirmesi uygular. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`

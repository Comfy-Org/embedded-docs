# Pixal3D Çoklu Görünüm Koşullandırma

Pixal3D Multi-View Conditioning düğümü, sabit bir yörünge kamera düzeneğinden koşullandırma verisi oluşturur: 90 derece arayla yerleştirilmiş ön, sol, arka ve sağ görünümler, tam olarak çerçevelendiği gibi kullanılır. Nesnenin en az bir kare görünümünü bağlayın; Pixal3D modelleri için eşleşen pozitif ve negatif koşullandırma hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision, paketlenmiş NAF ağırlıklarıyla birlikte. | CLIP_VISION | Evet | N/A |
| `fov` | Görünümlerin çerçevelendiği haliyle yatay FOV'si (derece cinsinden): rig render'ları ve çoğu çok görünümlü üretici için 20 veya fotoğraflar için görünümlerden birinde MoGeGeometryToFOV. Varsayılan: 20.0. | FLOAT | Evet | 1.0 - 170.0 |
| `front` | Nesnenin ön tarafının kare görünümü; alfa kanallı veya siyah arka plan üzerinde, rig gibi çerçevelenmiş: nesne en geniş yerinde çerçevenin yaklaşık 1/1.1'ini kaplar, her görünümde aynı ölçek. İlk bağlanan görünüm (ön, sol, arka, sağ sırasıyla), mesh'in önü olarak alınır ve mesh o görünüme göre yönlendirilir. | IMAGE | Hayır | N/A |
| `left` | Nesnenin sol tarafının kare görünümü; alfa kanallı veya siyah arka plan üzerinde, rig gibi çerçevelenmiş: nesne en geniş yerinde çerçevenin yaklaşık 1/1.1'ini kaplar, her görünümde aynı ölçek. İlk bağlanan görünüm (ön, sol, arka, sağ sırasıyla), mesh'in önü olarak alınır ve mesh o görünüme göre yönlendirilir. | IMAGE | Hayır | N/A |
| `back` | Nesnenin arka tarafının kare görünümü; alfa kanallı veya siyah arka plan üzerinde, rig gibi çerçevelenmiş: nesne en geniş yerinde çerçevenin yaklaşık 1/1.1'ini kaplar, her görünümde aynı ölçek. İlk bağlanan görünüm (ön, sol, arka, sağ sırasıyla), mesh'in önü olarak alınır ve mesh o görünüme göre yönlendirilir. | IMAGE | Hayır | N/A |
| `right` | Nesnenin sağ tarafının kare görünümü; alfa kanallı veya siyah arka plan üzerinde, rig gibi çerçevelenmiş: nesne en geniş yerinde çerçevenin yaklaşık 1/1.1'ini kaplar, her görünümde aynı ölçek. İlk bağlanan görünüm (ön, sol, arka, sağ sırasıyla), mesh'in önü olarak alınır ve mesh o görünüme göre yönlendirilir. | IMAGE | Hayır | N/A |

### Notlar

- En az bir görünüm bağlanmalıdır; dört görünüm girişinin tümü boşsa düğüm hata verir.
- İlk bağlanan görünüm, ön, sol, arka, sağ sırasına göre ön olarak kabul edilir ve mesh o görünüme göre yönlendirilir. İlk bağlanan görünüm `front` değilse, mesh'in önü olarak bu görünüm kullanılarak yönlendirileceğini belirten bir uyarı günlüğe kaydedilir.
- Görünümler ön, sol, arka, sağ sırasıyla okunur ve ilk bağlanan görünüme göre sabit azimutlarında yörüngeye yerleştirilir.
- Alfa kanalı olan giriş görünümlerinde alfa, siyah üzerine uygulanır. 1024 x 1024 olmayan görünümler 1024 x 1024 boyutuna yeniden boyutlandırılır.
- Toplu iş boyutu ilk bağlanan görünümden alınır. Bağlanan görünümlerin toplu iş boyutları farklıysa, daha küçük olanlar eşleşecek şekilde döngüye alınır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Pozitif koşullandırma çıktısı; kodlanmış görünümlerden ve bunların yansıtılmış özelliklerinden oluşturulur. | CONDITIONING |
| `negative` | Negatif koşullandırma çıktısı; aynı yansıtılmış özelliklerle sıfırlanmış gömme vektörlerinden oluşturulur. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`

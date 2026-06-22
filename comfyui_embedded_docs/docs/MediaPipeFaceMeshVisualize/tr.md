# MediaPipe Yüz Ağı Görselleştir

## Genel Bakış

Giriş görüntüsü üzerine yüz işaret noktaları ve bağlantı çizgileri (bir yüz ağı) çizer. Bu düğüm, bir yüz algılama düğümü tarafından üretilen işaret verilerini kullanarak gözler, burun, ağız ve yüz çevresi gibi algılanan yüz özelliklerini görselleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Bir algılama düğümünden gelen yüz işaret verisi. | FACE_LANDMARKS | Evet |  |
| `image` | Ağın çizileceği görüntü. Bağlı değilse, algılama sonucuyla aynı boyutta siyah bir tuval kullanılır. | IMAGE | Hayır |  |
| `connections` | Yüz ağının hangi bölümlerinin çizileceğini belirler. `"all"` tam ağı (oval, gözler, kaşlar, dudaklar, irisler, burun) çizer. `"fill"` yüz ovalinin dolu bir çokgenini (siluet maskesi) çizer. `"custom"` her özelliği ayrı ayrı açıp kapatmanızı sağlar. (varsayılan: `"all"`) | COMBO | Evet | `"all"`<br>`"fill"`<br>`"custom"` |
| `color` | Ağ çizgilerinin ve noktalarının rengi. (varsayılan: `#00ff00`) | COLOR | Evet |  |
| `thickness` | Ağ çizgilerinin piksel cinsinden kalınlığı. 0 olarak ayarlanması çizgi çizmeyi devre dışı bırakır. (varsayılan: 1) | INT | Evet | 0 ila 8 |
| `point_size` | İşaret noktalarının piksel cinsinden yarıçapı. 0 olarak ayarlanması nokta çizmeyi devre dışı bırakır. (varsayılan: 2) | INT | Evet | 0 ila 16 |

**`connections` parametresi hakkında not:** `"custom"` seçildiğinde, her yüz özelliği için ek boolean girişler görünür (örneğin, `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Yalnızca etkinleştirdiğiniz özellikler çizilecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Üzerine yüz işaret ağı çizilmiş giriş görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/tr.md)

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`

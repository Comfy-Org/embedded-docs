# MoGeGeometryToFOV

Bu düğüm, bir MoGe geometri nesnesinde saklanan kamera iç parametrelerinden görüş alanını ve odak uzunluğunu türetir. Dikey, yatay veya çapraz FOV değerini derece veya radyan cinsinden döndürebilir. Dikey FOV çıktısı, örneğin SAM3DBody_Predict düğümünü beslemek için kullanılabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe geometri nesnesi. Bir iç parametre matrisi ve odak uzunluğu dönüşümü için piksel yüksekliğini okumak amacıyla kullanılan görüntü, nokta veya derinlik verilerinden en az birini içermelidir. | MOGE_GEOMETRY | Evet | — |
| `axis` | FOV'nin hesaplandığı eksen: "vertical" (fov_y), "horizontal" (fov_x) veya "diagonal" (varsayılan: "vertical"). | COMBO | Evet | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | FOV için çıktı birimi (varsayılan: "degrees"). | COMBO | Evet | "degrees"<br>"radians" |

Not: `moge_geometry` iç parametre içermiyorsa (panorama geometrisinde hiç yoktur) veya görüntü, nokta ya da derinlik verisinden hiçbirini içermiyorsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `fov` | Seçilen eksen boyunca, seçilen birimle (derece veya radyan) görüş alanı. | FLOAT |
| `focal_pixels` | Dikey iç parametre ve piksel yüksekliğinden türetilen, piksel cinsinden mercek odak uzaklığı. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/tr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`

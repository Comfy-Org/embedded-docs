# MoGe Geometrisinden FoV Al

Bu düğüm, bir MoGe geometri nesnesinde saklanan kamera içsel parametrelerinden görüş alanını ve odak uzaklığını türetir. Dikey, yatay veya çapraz FOV'u derece veya radyan cinsinden döndürebilir. Dikey FOV çıktısı, örneğin SAM3DBody_Predict düğümünü beslemek için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe geometri nesnesi. Bir içsel parametreler matrisi ve odak uzaklığı dönüşümü için piksel yüksekliğini okumak üzere kullanılan `image`, `points` veya `depth` verilerinden en az birini içermelidir. | MOGE_GEOMETRY | Evet | — |
| `eksen` | FOV'un hesaplandığı eksen: "vertical" (fov_y), "horizontal" (fov_x) veya "diagonal" (varsayılan: "vertical"). | COMBO | Evet | "vertical"<br>"horizontal"<br>"diagonal" |
| `birim` | FOV için çıktı birimi (varsayılan: "degrees"). | COMBO | Evet | "degrees"<br>"radians" |

Not: Düğüm, `moge_geometry` hiç içsel parametre içermiyorsa (panorama geometrisinde hiç yoktur) veya ne `image`, ne `points`, ne de `depth` verisi içeriyorsa hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `fov` | Seçilen eksen boyunca, seçilen birimde (derece veya radyan) görüş alanı. | FLOAT |
| `focal_pixels` | Piksel cinsinden lens odak uzaklığı; dikey içsel parametreden ve piksel yüksekliğinden türetilir. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/tr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`

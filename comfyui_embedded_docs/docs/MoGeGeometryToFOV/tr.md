# MoGeGeometryToFOV

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe geometri nesnesi. İç parametre matrisi ve görüntü, nokta veya derinlik verisinden en az birini içermelidir; bu veri, odak uzaklığı dönüşümü için piksel yüksekliğini okumak amacıyla kullanılır. | MOGE_GEOMETRY | Evet | — |
| `eksen` | FOV'un hesaplandığı eksen: "vertical" (fov_y), "horizontal" (fov_x) veya "diagonal" (varsayılan: "vertical"). | COMBO | Evet | "vertical"<br>"horizontal"<br>"diagonal" |
| `birim` | FOV çıktı birimi (varsayılan: "degrees"). | COMBO | Evet | "degrees"<br>"radians" |

Not: `moge_geometry` iç parametre içermiyorsa (panorama geometrisinde iç parametre bulunmaz) veya görüntü, nokta ya da derinlik verisinden hiçbirini içermiyorsa düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `fov` | Seçilen eksen boyunca görüş alanı, seçilen birim cinsinden (derece veya radyan). | FLOAT |
| `focal_pixels` | Dikey iç parametre ve piksel yüksekliğinden türetilen, piksel cinsinden mercek odak uzaklığı. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/tr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`

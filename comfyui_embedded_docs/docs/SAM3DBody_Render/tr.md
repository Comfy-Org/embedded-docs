# 3D Vücut Pozunu Oluştur

Seçilebilir bir stil kullanarak 3B vücut poz verisini bir görüntüye dönüştürür. Düğüm; SAM3D vücut izleyicisinden (MHR) veya Kimodo gibi harici bir Y-up riginden poz verisi kabul eder ve sonucu isteğe bağlı bir arka plan görüntüsü üzerine (veya arka plan sağlanmadığında siyah bir tuval üzerine) yerleştirebilir. Mevcut render stilleri arasında gölgeli bir 3B mesh, ikili silüet, 2B ve 3B OpenPose tarzı iskeletler ve SCAIL tarzı vücut kapsülleri bulunur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `render_style` | Render modu. 'mesh' = kamera aracılığıyla rasterleştirilen 3B MHR mesh'i. 'silhouette' = mesh'in ikili maskesi. 'openpose_2d' = düz 2B iskelet. 'openpose_3d' = düz gölgeli 3B model olarak OpenPose iskeleti. 'scail' = SCAIL 3B kapsülleri. (varsayılan: "mesh") | DYNAMIC_COMBO | Evet | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | MHR poz verisi veya harici Y-up rig poz verisi (KimodoSample). `_skeleton_override` alanında OpenPose eklem haritaları taşıyan harici rigler için tüm render stilleri çalışır (KimodoSample bunu yapar). | MHR_POSE_DATA veya KIMODO_POSE_DATA | Evet | — |
| `arka plan` | Kare başına arka plan. Belirtilmezse = siyah tuval. | IMAGE | Hayır | — |
| `genişlik` | Piksel cinsinden çıktı genişliği. 0 = poz verisinin yerel image_size değerini kullan. Genişlik/yükseklik değerlerinden yalnızca biri ayarlanırsa, diğeri orijinal en-boy oranı korunarak türetilir. (varsayılan: 0) | INT | Hayır | 0 ile 16384, adım 8 |
| `yükseklik` | Piksel cinsinden çıktı yüksekliği. 0 = poz verisinin yerel image_size değerini kullan. Genişlik/yükseklik değerlerinden yalnızca biri ayarlanırsa, diğeri orijinal en-boy oranı korunarak türetilir. (varsayılan: 0) | INT | Hayır | 0 ile 16384, adım 8 |
| `camera_info` | Serbest 6DOF kamera geçersiz kılma. Bağlandığında poz, tahmin edilen kamera yerine bu kamera üzerinden yeniden izdüşümü yapılır (konum/hedef/zoom/dönüş/FoV). | LOAD_3D_CAMERA | Hayır | — |

### Mesh Girdileri

Bu parametreler `render_style` "mesh" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `shader` | Hazır gölgelendirici. 'normals' = kamera uzayındaki mevcut yüzey normali (OpenGL Y+ normal haritası kuralı: +X→R, +Y→G, +Z→B). 'rainbow' = RealisDance tarzı body-Y jet; 'rainbow_face_*' varyantları yüz vertexlerini normal/bölge renkleriyle geçersiz kılar; 'depth' = doğrusal gri. (varsayılan: "default") | DYNAMIC_COMBO | Hayır | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Gökkuşağı jet eksenini Z (ileri) etrafında döndürür. Sol/sağ ayrımını sağlar. Yalnızca `shader` değeri "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olduğunda kullanılabilir. (varsayılan: -35.0) | FLOAT | Hayır | -90.0 ile 90.0, adım 0.5 |
| `rainbow_tilt_x` | Gökkuşağı jet eksenini X (sağ) etrafında döndürür. Ön/arka ayrımını sağlar. Yalnızca `shader` değeri "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olduğunda kullanılabilir. (varsayılan: 0.0) | FLOAT | Hayır | -90.0 ile 90.0, adım 0.5 |
| `opacity` | Arka plan görüntüsü üzerindeki mesh alfa değeri; hiçbir şey bağlı değilse siyah üzerinde. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0, adım 0.01 |
| `person_palette_falloff` | Kişi başına beyaza doğru doygunluk azaltma: k izi, (1 - falloff^k) pastel karışımı alır (SCAIL 'daha yumuşak ikinci kişi'). 1.0 = kapalı. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 ile 1.0, adım 0.05 |
| `region` | 'hands_only', önceden hesaplanmış `hand_vert_mask` (kanonik el anahtar noktalarına göre LBS ağırlıkları) aracılığıyla çokgen yüzlerini filtreler — hata ayıklama için el mesh'ini izole eder. Maske yoksa tam mesh render edilir. (varsayılan: "full_body") | COMBO | Hayır | "full_body"<br>"hands_only" |

### Silhouette Girdileri

`render_style` "silhouette" olduğunda, düğüm 3B mesh'in ikili maskesini render eder. Bu modun ek parametresi yoktur.

### OpenPose 2D Girdileri

Bu parametreler `render_style` "openpose_2d" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | Vücut anahtar noktası nokta yarıçapı (px). (varsayılan: 4) | INT | Hayır | 1 ile 32, adım 1 |
| `stick_width_px` | Vücut uzuv elipsinin yarı genişliği (px). DWPose varsayılanı = 4. (varsayılan: 4) | INT | Hayır | 1 ile 32, adım 1 |
| `limb_alpha` | Uzuv başına alfa. DWPose varsayılanı = 0.6. (varsayılan: 0.6) | FLOAT | Hayır | 0.0 ile 1.0, adım 0.05 |
| `face_style` | 'full' = tüm yüz işaret noktaları (varsa sapiens-238, aksi takdirde rig yedeği ~30). 'eyes_mouth' = rig yedeği alt kümesi (~12 nokta: yalnızca gözler + dış dudaklar). 'disabled' = yüz noktası yok. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | 21+21 el anahtar noktası + çubukları çizer. 'disabled' = el yok. 'dwpose' = düz mavi noktalar; 'openpose' = gökkuşağı noktaları. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi, 1 - falloff^k oranında beyaza karışır. 0. iz canlı kalır; 1.0 azaltmayı devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 ile 1.0, adım 0.05 |

### OpenPose 3D Girdileri

Bu parametreler `render_style` "openpose_3d" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Uzuv kapsülünün metre cinsinden yarıçapı (ince = çubuk benzeri). (varsayılan: 0.015) | FLOAT | Hayır | 0.004 ile 0.1, adım 0.001 |
| `include_hands` | 21+21 el anahtar noktasını 3B kapsüller olarak çizer. (varsayılan: True) | BOOLEAN | Hayır | True or False |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi, 1 - falloff^k oranında beyaza karışır. 0. iz canlı kalır; 1.0 azaltmayı devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 ile 1.0, adım 0.05 |

### SCAIL Girdileri

Bu parametreler `render_style` "scail" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Metre cinsinden kapsül yarıçapı (SCAIL referansı: ~0.022 m). (varsayılan: 0.022) | FLOAT | Hayır | 0.005 ile 0.2, adım 0.001 |
| `hand_style` | 3B kapsül gövdesinin üzerine 2B OpenPose elleri bindirir (SCAIL ile uyumludur — 3B el kapsülü yoktur). 'disabled' = el yok. 'dwpose' = düz mavi el noktaları; 'openpose' = gökkuşağı noktaları. Çubuklar her iki durumda da parmak başına gökkuşağı renginde kalır. (varsayılan: "dwpose") | COMBO | Hayır | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = tüm yüz işaret noktaları (varsa sapiens-238, aksi takdirde rig yedeği ~30). 'eyes_mouth' = rig yedeği alt kümesi (~12 nokta: yalnızca gözler + dış dudaklar). 'disabled' = yüz noktası yok. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi, 1 - falloff^k oranında beyaza karışır. 0. iz canlı kalır; 1.0 azaltmayı devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 ile 1.0, adım 0.05 |

### Notlar

- `width` ve `height` değerlerinin ikisi de 0 ise çıktı, poz verisinin yerel görüntü boyutunu kullanır. Yalnızca biri ayarlanmışsa, diğeri orijinal en-boy oranı korunarak türetilir. Bağlı bir `background`, render çözünürlüğüne uyacak şekilde yeniden boyutlandırılır.
- `camera_info` bağlandığında, poz tahmin edilen kamera yerine bu kamera üzerinden yeniden izdüşümü yapılır.
- Mesh modunda, `rainbow_tilt_z` ve `rainbow_tilt_x` yalnızca `shader` değeri "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olarak ayarlandığında kullanılabilir.
- Mesh modunda, `region` "hands_only" olduğunda, el bölgesi filtresi poz verisinin bir el vertex maskesi içermesini gerektirir; maske yoksa bunun yerine tam mesh render edilir.
- SCAIL modunda eller her zaman 2B kaplama olarak çizilir; 3B el kapsülü yoktur.
- Çıktı çözünürlüğü, poz verisinin yerel çözünürlüğünden farklı olduğunda, openpose_2d işaretleyici ve çubuk boyutları orantılı olarak ölçeklenir.
- Arka planda poz verisinden daha az kare varsa, son arka plan karesi kalan kareler için yeniden kullanılır.
- Çıktı, girdi poz karesi başına bir kare içerir. Poz verisi hiç kare içermiyorsa, tek bir siyah görüntü döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntü` | Render edilmiş kareler: poz verisi seçilen render stilinde çizilir; bir arka plan bağlıysa arka plan üzerine, aksi takdirde siyah üzerine yerleştirilir. Girdi poz karesi başına bir kare olacak şekilde tek bir toplu görüntü olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/tr.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`

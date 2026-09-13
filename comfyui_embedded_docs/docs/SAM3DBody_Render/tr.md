# 3D Vücut Pozunu Oluştur

3B vücut poz verilerini seçilebilir bir stil kullanarak görüntüye dönüştürür. Düğüm, SAM3D vücut izleyicisinden (MHR) veya Kimodo gibi harici bir Y-up rig'den poz verilerini kabul eder ve sonucu isteğe bağlı bir arka plan görüntüsü üzerine (veya hiçbiri sağlanmadığında siyah bir tuval üzerine) birleştirebilir. Kullanılabilir render stilleri arasında gölgeli 3B mesh, ikili siluet, 2B ve 3B OpenPose tarzı iskeletler ve SCAIL tarzı vücut kapsülleri bulunur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `render_style` | Render modu. 'mesh' = kamera aracılığıyla rasterleştirilen 3B MHR mesh. 'silhouette' = meshin ikili maskesi. 'openpose_2d' = düz 2B iskelet. 'openpose_3d' = düz gölgeli 3B model olarak OpenPose iskeleti. 'scail' = SCAIL 3B kapsülleri. (varsayılan: "mesh") | DYNAMIC_COMBO | Evet | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | MHR poz verileri veya harici Y-up rig poz verileri (KimodoSample). Tüm render stilleri, `_skeleton_override` içinde OpenPose eklem haritaları taşıyan harici rig'ler için çalışır (KimodoSample taşır). | MHR_POSE_DATA or KIMODO_POSE_DATA | Evet | — |
| `background` | Kare başına arka plan. Atlanırsa = siyah tuval. | IMAGE | Hayır | — |
| `width` | Çıktı genişliği piksel cinsinden. 0 = poz verilerinin yerel image_size değerini kullan. Genişlik/yükseklikten yalnızca biri ayarlanırsa, diğeri orijinal en-boy oranı korunarak türetilir. (varsayılan: 0) | INT | Hayır | 0 - 16384, adım 8 |
| `height` | Çıktı yüksekliği piksel cinsinden. 0 = poz verilerinin yerel image_size değerini kullan. Genişlik/yükseklikten yalnızca biri ayarlanırsa, diğeri orijinal en-boy oranı korunarak türetilir. (varsayılan: 0) | INT | Hayır | 0 - 16384, adım 8 |
| `camera_info` | Serbest 6DOF kamera geçersiz kılma. Bağlandığında, poz öngörülen kamera yerine bu kamera (konum/hedef/yakınlaştırma/döndürme/FoV) aracılığıyla yeniden yansıtılır. | LOAD_3D_CAMERA | Hayır | — |

### Mesh Girdileri

Bu parametreler `render_style` "mesh" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `shader` | Ön ayarlı shader. 'normals' = kamera uzayındaki mevcut yüzey normali (OpenGL Y+ normal-map kuralı: +X→R, +Y→G, +Z→B). 'rainbow' = RealisDance tarzı gövde-Y jeti; 'rainbow_face_*' varyantları yüz köşelerini normal/bölge başına renklerle geçersiz kılar; 'depth' = doğrusal gri. (varsayılan: "default") | DYNAMIC_COMBO | Hayır | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Rainbow jet eksenini Z (ileri) etrafında döndürür. Sol/sağı ayırt eder. Yalnızca `shader` "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olduğunda kullanılabilir. (varsayılan: -35.0) | FLOAT | Hayır | -90.0 - 90.0, adım 0.5 |
| `rainbow_tilt_x` | Rainbow jet eksenini X (sağ) etrafında döndürür. Ön/arkayı ayırt eder. Yalnızca `shader` "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olduğunda kullanılabilir. (varsayılan: 0.0) | FLOAT | Hayır | -90.0 - 90.0, adım 0.5 |
| `opacity` | Arka plan görüntüsü üzerinde veya hiçbiri bağlı değilse siyah üzerinde mesh alfa değeri. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0, adım 0.01 |
| `person_palette_falloff` | Kişi başına beyaza doğru doygunluk azaltma: k izi (1 - falloff^k) pastel karışım alır (SCAIL 'daha yumuşak ikinci kişi'). 1.0 = kapalı. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 - 1.0, adım 0.05 |
| `region` | 'hands_only' yüzleri önceden hesaplanmış `hand_vert_mask` (kanonik el KP'lerine karşı LBS ağırlıkları) aracılığıyla filtreler — hata ayıklama için el mesh'ini izole eder. Maske eksikse tam mesh'e geri döner. (varsayılan: "full_body") | COMBO | Hayır | "full_body"<br>"hands_only" |

### Silhouette Girdileri

`render_style` "silhouette" olduğunda, düğüm 3B mesh'in ikili maskesini render eder. Bu modun ek parametresi yoktur.

### OpenPose 2D Girdileri

Bu parametreler `render_style` "openpose_2d" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | Vücut anahtar noktası nokta yarıçapı (px). (varsayılan: 4) | INT | Hayır | 1 - 32, adım 1 |
| `stick_width_px` | Vücut uzvu elips yarı genişliği (px). DWPose varsayılanı = 4. (varsayılan: 4) | INT | Hayır | 1 - 32, adım 1 |
| `limb_alpha` | Uzuv başına alfa. DWPose varsayılanı = 0.6. (varsayılan: 0.6) | FLOAT | Hayır | 0.0 - 1.0, adım 0.05 |
| `face_style` | 'full' = tüm yüz öznitelik noktaları (varsa sapiens-238, yoksa rig-fallback ~30). 'eyes_mouth' = rig-fallback alt kümesi (~12 nokta: yalnızca gözler + dış dudaklar). 'disabled' = yüz noktası yok. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | 21+21 el anahtar noktası + çubukları çizer. 'disabled' = el yok. 'dwpose' = düz mavi noktalar; 'openpose' = gökkuşağı noktaları. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi 1 - falloff^k ile beyaza doğru karışır. 0. iz canlı kalır; 1.0 falloff'u devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 - 1.0, adım 0.05 |

### OpenPose 3D Girdileri

Bu parametreler `render_style` "openpose_3d" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Uzuv kapsülü yarıçapı metre cinsinden (ince = çubuk benzeri). (varsayılan: 0.015) | FLOAT | Hayır | 0.004 - 0.1, adım 0.001 |
| `include_hands` | 21+21 el anahtar noktasını 3B kapsüller olarak çizer. (varsayılan: True) | BOOLEAN | Hayır | True or False |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi 1 - falloff^k ile beyaza doğru karışır. 0. iz canlı kalır; 1.0 falloff'u devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 - 1.0, adım 0.05 |

### SCAIL Girdileri

Bu parametreler `render_style` "scail" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Kapsül yarıçapı metre cinsinden (SCAIL referansı: ~0.022 m). (varsayılan: 0.022) | FLOAT | Hayır | 0.005 - 0.2, adım 0.001 |
| `hand_style` | 3B kapsül gövdesinin üzerine 2B OpenPose elleri bindirir (SCAIL ile eşleşir — 3B el kapsülü yok). 'disabled' = el yok. 'dwpose' = düz mavi el noktaları; 'openpose' = gökkuşağı noktaları. Çubuklar her iki durumda da parmak başına gökkuşağı kalır. (varsayılan: "dwpose") | COMBO | Hayır | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = tüm yüz öznitelik noktaları (varsa sapiens-238, yoksa rig-fallback ~30). 'eyes_mouth' = rig-fallback alt kümesi (~12 nokta: yalnızca gözler + dış dudaklar). 'disabled' = yüz noktası yok. (varsayılan: "disabled") | COMBO | Hayır | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Kişi başına doygunluk azaltma: k izi 1 - falloff^k ile beyaza doğru karışır. 0. iz canlı kalır; 1.0 falloff'u devre dışı bırakır. (varsayılan: 0.6) | FLOAT | Hayır | 0.1 - 1.0, adım 0.05 |

### Notlar

- Hem `width` hem de `height` 0 ise, çıktı poz verilerinin yerel görüntü boyutunu kullanır. Yalnızca biri ayarlanırsa, diğeri orijinal en-boy oranı korunarak türetilir. Bağlı bir `background`, render çözünürlüğüyle eşleşecek şekilde yeniden boyutlandırılır.
- `camera_info` bağlandığında, poz öngörülen kamera yerine o kamera aracılığıyla yeniden yansıtılır.
- Mesh modunda, `rainbow_tilt_z` ve `rainbow_tilt_x` yalnızca `shader` "rainbow", "rainbow_face_normal" veya "rainbow_face_semantic" olarak ayarlandığında kullanılabilir.
- Mesh modunda, `region` "hands_only" olduğunda, el bölgesi filtresi poz verilerinin bir el tepe noktası maskesi içermesini gerektirir; maske eksikse bunun yerine tam mesh render edilir.
- SCAIL modunda, eller 3B kapsüller yerine 3B kapsül gövdesinin üzerine 2B OpenPose katmanları olarak çizilir; `hand_style` "disabled" olarak ayarlanması onları tamamen kaldırır.
- Çıktı çözünürlüğü poz verilerinin yerel çözünürlüğünden farklı olduğunda, openpose_2d işaretçi ve çubuk boyutları orantılı olarak ölçeklenir.
- Arka plan, poz verilerinden daha az kareye sahipse, kalan kareler için son arka plan karesi yeniden kullanılır.
- Çıktı, her giriş poz karesi için bir kare içerir. Poz verileri hiç kare içermiyorsa, tek bir siyah görüntü döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Render edilen kareler: seçilen render stilinde çizilen poz verileri, bir arka plan bağlıysa onun üzerine, aksi halde siyah üzerine birleştirilir. Her giriş poz karesi için bir kare, tek bir toplu görüntü olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/tr.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`

# 3B Animasyon Dosyası Oluştur

Bu düğüm, poz verilerinden kaydedilmeye hazır bir 3D animasyon dosyası oluşturur. Animated GLB'yi birkaç görsel stilde dışa aktarabilirsiniz — tam vücut ağı, yalnızca eklemler önizlemesi, OpenPose iskeleti veya SCAIL kapsül rig'i — veya bunun yerine bir BVH motion-capture klibi kaydedebilirsiniz. Çıktı, dosyayı diske yazmak için Save 3D Model gibi bir dosya kaydetme düğümüne bağlanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pose_data` | 3B poz verileri. MHR poz verilerini (model/şekil/ifade parametreleri, MHR70 anahtar noktaları, kanonik renkler, el köşe maskesi) veya Kimodo poz verilerini (her kare için tahmin edilen köşelere ve kameraya sahip harici Y-up rig) kabul eder. | MHR_POSE_DATA / KIMODO_POSE_DATA | Evet | — |
| `format` | Çıktı biçimi; diske yazmak için Save 3D Model'e beslenir. 'glb' = animasyonlu GLB (mesh / bones / openpose / scail). 'bvh' = BVH mocap klibi (tek iskelet; model gerektirir). (varsayılan: glb) | DYNAMIC_COMBO | Evet | "glb"<br>"bvh" |
| `sam3d_body_model` | İsteğe bağlı SAM3D vücut modeli. Poz verileri bir iskelet geçersiz kılma içermiyorsa 'bvh', 'body_mesh' ve 'bones_only' biçimleri için gereklidir. | SAM3D_BODY_MODEL | Hayır | — |
| `fps` | Animasyon kare hızı. (varsayılan: 24.0) | FLOAT | Evet | 1.0-240.0 |
| `camera_translation` | pred_cam_t'yi kökün konumuna işleyin: 'off' = bağlama konumu; 'centered' = 0. kareye göre fark; 'absolute' = ham (Z, kamera derinliğidir — genellikle metre cinsinden uzaklık). (varsayılan: off) | COMBO | Evet | "off"<br>"centered"<br>"absolute" |
| `track_index` | Parça seçimi: -1 = tüm parçalar; ≥0 = tek parça. (varsayılan: -1) | INT | Evet | -1 ila 15 |

### GLB Girdileri

Bu girdiler `format` "glb" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh_style` | GLB'nin görsel stili: 'body_mesh' = gerçek Armature (127 kemik, skinning, TRS anahtar kareleri, 72 yüz morph'u; model gerektirir). 'bones_only' = her eklemde kemik şeklindeki ilkeller (önizleme armature'ı). 'openpose' = anahtar noktalardan OpenPose-18 3B iskeleti. 'scail' = SCAIL 3B kapsül rig'i (eklem küreleriyle uçları aynı hizada kapatılmış açık silindirler). (varsayılan: body_mesh) | DYNAMIC_COMBO | Evet | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | Kemik başına dönüş anahtar kareleri / anahtar nokta parçaları üzerinde Gauss yumuşatma penceresi. 0 = kapalı. 7-15, yukarı akıştaki Smooth'un sivri uçları kaçırdığı yerlerde dönüşleri/titreşimleri sakinleştirir. (varsayılan: 0) | INT | Evet | 0-51, adım 2 |

#### Body Mesh Girdileri

`mesh_style` "body_mesh" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Her ekleme rijit şekilde bağlanmış kemik görselleştirme şekli. 'off' = kemik görselleştirmesi yok; 'octahedrons' = Blender tarzı yönlü kemikler. (varsayılan: off) | DYNAMIC_COMBO | Evet | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | `bone_vis` = "octahedrons" olduğunda görünür. Metre cinsinden yarıçap (küre yarıçapı / oktahedron yarı genişliği). (varsayılan: 0.02) | FLOAT | Evet | 0.005-0.5 |
| `bone_vis_color` | `bone_vis` = "octahedrons" olduğunda görünür. Kemik başına köşe renkleri (ışıksız malzeme). 'white' = yok, 'rainbow_y' = baştan ayağa jet renk skalası. (varsayılan: rainbow_y) | COMBO | Evet | "white"<br>"rainbow_y" |
| `shader` | Render düğümünün shader'larıyla eşleşen köşe başına renkleri işleyin (COLOR_0 + KHR_materials_unlit). 'default' = renk yok. (varsayılan: default) | DYNAMIC_COMBO | Evet | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | `shader` bir rainbow varyantı olduğunda görünür. Rainbow jet eksenini Z (ileri) etrafında döndürür. Sol/sağ ayrımını sağlar. (varsayılan: -35.0) | FLOAT | Evet | -90.0 ila 90.0 |
| `rainbow_tilt_x` | `shader` bir rainbow varyantı olduğunda görünür. Rainbow jet eksenini X (sağ) etrafında döndürür. Ön/arka ayrımını sağlar. (varsayılan: 0.0) | FLOAT | Evet | -90.0 ila 90.0 |
| `person_palette_falloff` | `shader` bir rainbow varyantı olduğunda görünür. Kişi başına doygunluk azaltma: her parça (1 - falloff^k) pastel karışımı alır. (varsayılan: 0.6) | FLOAT | Evet | 0.1-1.0 |

#### Bones Only Girdileri

`mesh_style` "bones_only" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Her ekleme rijit şekilde bağlanmış kemik görselleştirme şekli. 'octahedrons' = Blender tarzı yönlü kemikler (eklem → birincil alt öğe). | DYNAMIC_COMBO | Evet | "octahedrons" |
| `bone_vis_radius_m` | Metre cinsinden yarıçap (küre yarıçapı / oktahedron yarı genişliği). (varsayılan: 0.02) | FLOAT | Evet | 0.005-0.5 |
| `bone_vis_color` | Kemik başına köşe renkleri (ışıksız malzeme). 'white' = yok, 'rainbow_y' = baştan ayağa jet renk skalası. (varsayılan: rainbow_y) | COMBO | Evet | "white"<br>"rainbow_y" |

#### OpenPose Girdileri

`mesh_style` "openpose" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_m` | Metre cinsinden küre yarıçapı. (varsayılan: 0.010) | FLOAT | Evet | 0.005-0.1 |
| `stick_radius_m` | Metre cinsinden uzuv yarı genişliği. Otomatik olarak bone_length x 0.1 değerine sınırlanır. (varsayılan: 0.008) | FLOAT | Evet | 0.002-0.05 |
| `include_hands` | pred_keypoints_3d kaynaklı 21+21 OpenPose elini ekleyin (bilek + 5 parmak x 4 eklem, taban→uç). (varsayılan: False) | BOOLEAN | Evet | True / False |
| `hand_marker_radius_m` | Metre cinsinden el küresi yarıçapı. (varsayılan: 0.005) | FLOAT | Evet | 0.001-0.1 |
| `hand_stick_radius_m` | Metre cinsinden el uzvu yarı genişliği. (varsayılan: 0.003) | FLOAT | Evet | 0.001-0.05 |
| `face_style` | Sabit kafa ağı köşe kimliklerinde pred_vertices'ten örneklenen yüz konturu işaret noktaları (pose_data üzerinde canonical_colors gerektirir). 'full' = yaklaşık 30 noktanın tümü; 'eyes_mouth' = yalnızca gözler + dış dudaklar. (varsayılan: disabled) | COMBO | Evet | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | Yüz noktası yarıçapı. 0 = otomatik = 0.3 x marker_radius_m. (varsayılan: 0.0) | FLOAT | Evet | 0.0-0.05 |

#### SCAIL Girdileri

`mesh_style` "scail" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `stick_radius_m` | Metre cinsinden silindir yarıçapı. Kemikler sabit yarıçaplı açık silindirlerdir; eklem küreleri (eşleşecek şekilde otomatik boyutlandırılır) açık uçları kapatır. SCAIL referansı = 0.0215 m. (varsayılan: 0.022) | FLOAT | Evet | 0.002-0.1 |
| `marker_radius_m` | Eklem küresi yarıçapı. 0 = otomatik = stick_radius_m (aynı hizada kapak). (varsayılan: 0.0) | FLOAT | Evet | 0.0-0.1 |
| `material_roughness` | PBR pürüzlülüğü. SCAIL ref = 0.3. 1 = mat; 0 = krom. (varsayılan: 0.3) | FLOAT | Evet | 0.0-1.0 |
| `include_hands` | Parça başına 21+21 el anahtar noktası + kapsül çubukları ekleyin. (varsayılan: False) | BOOLEAN | Evet | True / False |
| `hand_marker_radius_m` | Metre cinsinden el küresi yarıçapı. (varsayılan: 0.005) | FLOAT | Evet | 0.001-0.05 |
| `hand_stick_radius_m` | Metre cinsinden el silindiri yarıçapı. (varsayılan: 0.003) | FLOAT | Evet | 0.001-0.05 |
| `face_style` | pred_vertices'ten örneklenen yüz konturu işaret noktaları (pose_data üzerinde canonical_colors gerektirir). 'full' = yaklaşık 30 noktanın tümü; 'eyes_mouth' = yalnızca gözler + dış dudaklar. (varsayılan: disabled) | COMBO | Evet | "disabled"<br>"full"<br>"eyes_mouth" |

### BVH Girdileri

`format` "bvh" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `units` | BVH OFFSET/konum birimleri. 'cm' mocap standardıdır. (varsayılan: cm) | COMBO | Evet | "cm"<br>"m" |

**Notlar:**

- `bvh` biçimi ile `body_mesh` ve `bones_only` ağ stilleri, `pose_data` bir iskelet geçersiz kılma içermiyorsa (`_skeleton_override` sözlüğü, örneğin bir KimodoSample düğümünden) `sam3d_body_model` girdisini gerektirir. Hiçbiri mevcut değilse düğüm bir hata verir. `openpose` ve `scail` stilleri rig'den bağımsızdır ve vücut modeli olmadan doğrudan anahtar noktalardan çalışır.
- `bvh` biçiminde çıktı tek bir iskelet içerir. `track_index` -1 olduğunda (tüm parçalar), ilk parça kullanılır.
- `full` ve `eyes_mouth` `face_style` seçenekleri, poz verilerinde `canonical_colors` gerektirir; bu veri, poz verileri vücut modeliyle birlikte MHR hattından geldiğinde mevcuttur.
- `bone_smooth_window` 0 ile 51 arasında 2'şer adımlarla ilerler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Oluşturulan animasyon dosyası: Save 3D Model gibi bir düğümle diske kaydedilmeye hazır, animasyonlu bir GLB veya bir BVH mocap klibi. | 3D_FILE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/tr.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`

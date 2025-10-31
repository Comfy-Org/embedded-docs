> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/tr.md)

Preview3DAnimation düğümü öncelikle 3D model çıktılarını önizlemek için kullanılır. Bu düğüm iki girdi alır: biri Load3D düğümünden gelen `camera_info`, diğeri ise 3D model dosyasının yoludur. Model dosya yolu `ComfyUI/output` klasörü altında bulunmalıdır.

**Desteklenen Formatlar**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden fazla 3D dosya formatını desteklemektedir.

**3D Düğüm Tercihleri**
3D düğümlerle ilgili bazı tercihler ComfyUI'nin ayarlar menüsünde yapılandırılabilir. Lütfen ilgili ayarlar için aşağıdaki belgelere başvurun:
[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

## Girdiler

| Parametre Adı | Tür           | Açıklama                                  |
| -------------- | -------------- | -------------------------------------------- |
| camera_info    | LOAD3D_CAMERA  | Kamera bilgisi                           |
| model_file     | STRING  | `ComfyUI/output/` altındaki model dosya yolu      |

## Tuval Alanı Açıklaması

Şu anda, ComfyUI ön yüzündeki 3D ile ilgili düğümler aynı tuval bileşenini paylaşır, bu nedenle bazı işlevsel farklılıklar dışında temel işlemleri büyük ölçüde tutarlıdır.

> Aşağıdaki içerik ve arayüz esas olarak Load3D düğümüne dayanmaktadır. Lütfen belirli özellikler için gerçek düğüm arayüzüne başvurun.

Tuval alanı çeşitli görünüm işlemlerini içerir, örneğin:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanı (FOV), kamera türü
- Genel aydınlatma yoğunluğu: ışık ayarı
- Model dışa aktarma: `GLB`, `OBJ`, `STL` formatlarını destekler
- vb.

![Load 3D Node UI](../Preview3D/asset/preview3d_canvas.jpg)

1. Load 3D düğümünün birden fazla menüsünü ve gizli menülerini içerir
2. 3D görünüm işlem ekseni

### 1. Görünüm İşlemleri

<video controls width="640" height="360">
  <source src="../Load3D/asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Görünüm kontrol işlemleri:

- Sol tıklama + sürükleme: Görünümü döndür
- Sağ tıklama + sürükleme: Görünümü kaydır
- Orta tekerlek kaydırma veya orta tıklama + sürükleme: Yakınlaştır/Uzaklaştır
- Koordinat ekseni: Görünümleri değiştir

### 2. Sol Menü İşlevleri

![Menu](../Load3D/asset/menu.webp)

Önizleme alanında, bazı görünüm işlem menüleri menü içinde gizlidir. Menü düğmesine tıklayarak farklı menüleri genişletebilirsiniz.

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, küçük resim ayarlarını içerir
- 2. Model: Model işleme modu, doku malzemesi, yukarı yön ayarları
- 3. Kamera: Ortografik ve perspektif görünümler arasında geçiş yap, perspektif açısını ayarla
- 4. Işık: Sahne genel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer formatlara dışa aktar (GLB, OBJ, STL)

#### Sahne

![scene menu](../Load3D/asset/menu_scene.webp)

Sahne menüsü bazı temel sahne ayar işlevleri sağlar:

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarla
3. Arka plan resmi yüklemek için tıkla
4. Önizleme küçük resmini gizle

#### Model

![Menu_Scene](../Load3D/asset/menu_model.webp)

Model menüsü bazı modelle ilgili işlevler sağlar:

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirle
2. **Malzeme modu**: Model işleme modlarını değiştir - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menu_modelmenu_camera](../Load3D/asset/menu_camera.webp)

Bu menü, ortografik ve perspektif görünümler arasında geçiş yapma ve perspektif açısı boyutu ayarları sağlar:

1. **Kamera**: Ortografik ve perspektif görünümler arasında hızlıca geçiş yap
2. **Görüş Alanı (FOV)**: Görüş Alanı açısını ayarla

#### Işık

![menu_modelmenu_camera](../Load3D/asset/menu_light.webp)

Bu menü aracılığıyla, sahnenin genel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz

#### Dışa Aktar

![menu_export](../Load3D/asset/menu_export.webp)

Bu menü, model formatlarını hızlıca dönüştürme ve dışa aktarma yeteneği sağlar
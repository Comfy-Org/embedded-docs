> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/tr.md)

Preview3D düğümü, 3B model çıktılarını önizlemek için kullanılır. Bu düğüm iki girdi alır: biri Load3D düğümünden gelen `camera_info` bilgisi, diğeri ise 3B model dosyasının yolu. Model dosya yolu, `ComfyUI/output` klasörü altında bulunmalıdır.

**Desteklenen Formatlar**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` gibi birden fazla 3B dosya formatını desteklemektedir.

**3B Düğüm Tercihleri**
3B düğümlerle ilgili bazı tercihler, ComfyUI'nın ayarlar menüsünde yapılandırılabilir. Lütfen ilgili ayarlar için aşağıdaki belgelere başvurun:
[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

## Girdiler

| Parametre Adı | Tür            | Açıklama                                      |
| ------------- | -------------- | --------------------------------------------- |
| camera_info   | LOAD3D_CAMERA  | Kamera bilgisi                                |
| model_file    | LOAD3D_CAMERA  | `ComfyUI/output/` altındaki model dosya yolu  |

## Tuval Alanı Açıklaması

Şu anda ComfyUI ön yüzündeki 3B ile ilgili düğümler aynı tuval bileşenini paylaştığından, bazı işlevsel farklılıklar dışında temel işlemleri büyük ölçüde tutarlıdır.

> Aşağıdaki içerik ve arayüz esas olarak Load3D düğümüne dayanmaktadır. Lütfen belirli özellikler için gerçek düğüm arayüzüne başvurun.

Tuval alanı, çeşitli görünüm işlemlerini içerir, örneğin:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanı (FOV), kamera türü
- Genel aydınlatma yoğunluğu: ışıklandırmayı ayarlama
- Model dışa aktarma: `GLB`, `OBJ`, `STL` formatlarını destekler
- vb.

![Load 3D Düğüm Arayüzü](./asset/preview3d_canvas.jpg)

1. Load 3D düğümünün birden fazla menüsünü ve gizli menülerini içerir
2. 3B görünüm işlem ekseni

### 1. Görünüm İşlemleri

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Görünüm kontrol işlemleri:

- Sol tıklama + sürükleme: Görünümü döndürme
- Sağ tıklama + sürükleme: Görünümü kaydırma
- Orta tekerlek kaydırma veya orta tıklama + sürükleme: Yakınlaştırma/Uzaklaştırma
- Koordinat ekseni: Görünümleri değiştirme

### 2. Sol Menü İşlevleri

![Menü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Önizleme alanında, bazı görünüm işlem menüleri menü içinde gizlidir. Menü düğmesine tıklayarak farklı menüleri genişletebilirsiniz.

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, küçük resim ayarlarını içerir
- 2. Model: Model işleme modu, doku malzemesi, yukarı yön ayarları
- 3. Kamera: Ortografik ve perspektif görünümler arasında geçiş yapma, perspektif açısını ayarlama
- 4. Işık: Sahne genel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer formatlara (GLB, OBJ, STL) dışa aktarma

#### Sahne

![sahne menüsü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Sahne menüsü, bazı temel sahne ayar işlevleri sağlar:

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarla
3. Arka plan görseli yüklemek için tıklayın
4. Önizleme küçük resmini gizle

#### Model

![Menü_Sahne](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar:

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirleme
2. **Malzeme modu**: Model işleme modlarını değiştirme - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Bu menü, ortografik ve perspektif görünümler arasında geçiş yapma ve perspektif açısı boyutu ayarları sağlar:

1. **Kamera**: Ortografik ve perspektif görünümler arasında hızlı geçiş
2. **Görüş Alanı (FOV)**: Görüş Alanı açısını ayarlama

#### Işık

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Bu menü aracılığıyla, sahnenin genel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz

#### Dışa Aktar

![menu_export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Bu menü, model formatlarını hızlıca dönüştürme ve dışa aktarma yeteneği sağlar
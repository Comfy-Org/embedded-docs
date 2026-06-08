Preview3DAnimation düğümü, temel olarak 3B model çıktılarını önizlemek için kullanılır. Bu düğüm iki girdi alır: biri Load3D düğümünden gelen `camera_info`, diğeri ise 3B model dosyasının yoludur. Model dosya yolu `ComfyUI/output` klasöründe bulunmalıdır.

**Desteklenen Formatlar**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden çok 3B dosya formatını destekler.

**3B Düğüm Tercihleri**
3B düğümleriyle ilgili bazı tercihler, ComfyUI'nin ayarlar menüsünden yapılandırılabilir. İlgili ayarlar için lütfen aşağıdaki belgelere bakın:
[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

## Girdiler

| Parametre Adı | Açıklama | Tür |
| --- | --- | --- |
| camera_info | Kamera bilgisi | LOAD3D_CAMERA |
| model_file | `ComfyUI/output/` altındaki model dosya yolu | STRING |

## Tuval Alanı Açıklaması

Şu anda, ComfyUI ön yüzündeki 3B ile ilgili düğümler aynı tuval bileşenini paylaşır, bu nedenle bazı işlevsel farklılıklar dışında temel işlemleri büyük ölçüde tutarlıdır.

> Aşağıdaki içerik ve arayüz temel olarak Load3D düğümüne dayanmaktadır. Belirli özellikler için lütfen gerçek düğüm arayüzüne bakın.

Tuval alanı, aşağıdakiler gibi çeşitli görünüm işlemlerini içerir:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş alanı (FOV), kamera türü
- Küresel aydınlatma yoğunluğu: aydınlatmayı ayarlama
- Model dışa aktarma: `GLB`, `OBJ`, `STL` formatlarını destekler
- vb.

![Load 3D Düğümü Arayüzü](../Preview3D/asset/preview3d_canvas.jpg)

1. Load 3D düğümünün birden çok menüsünü ve gizli menülerini içerir
2. 3B görünüm işlem ekseni

### 1. Görünüm İşlemleri

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Görünüm kontrol işlemleri:

- Sol tık + sürükle: Görünümü döndürme
- Sağ tık + sürükle: Görünümü kaydırma
- Orta tekerlek kaydırma veya orta tık + sürükle: Yakınlaştırma/uzaklaştırma
- Koordinat ekseni: Görünümleri değiştirme

### 2. Sol Menü İşlevleri

![Menü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Önizleme alanında, bazı görünüm işlem menüleri menüde gizlidir. Farklı menüleri genişletmek için menü düğmesine tıklayın.

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, küçük resim ayarlarını içerir
- 2. Model: Model oluşturma modu, doku malzemesi, yukarı yön ayarları
- 3. Kamera: Dik ve perspektif görünümler arasında geçiş yapma, perspektif açısını ayarlama
- 4. Işık: Sahne küresel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer formatlara dışa aktarma (GLB, OBJ, STL)

#### Sahne

![sahne menüsü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Sahne menüsü, bazı temel sahne ayarlama işlevleri sağlar:

1. Izgarayı göster/gizle
2. Arka plan rengini ayarlama
3. Arka plan resmi yüklemek için tıklama
4. Önizleme küçük resmini gizleme

#### Model

![Menü_Sahne](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar:

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirleme
2. **Malzeme modu**: Model oluşturma modlarını değiştirme - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menü_modelmenü_kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Bu menü, dik ve perspektif görünümler arasında geçiş ve perspektif açısı boyutu ayarları sağlar:

1. **Kamera**: Dik ve perspektif görünümler arasında hızlı geçiş
2. **FOV**: Görüş alanı (FOV) açısını ayarlama

#### Işık

![menü_modelmenü_kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Bu menü aracılığıyla sahnenin küresel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz

#### Dışa Aktar

![menü_dışa_aktar](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Bu menü, model formatlarını hızlıca dönüştürme ve dışa aktarma olanağı sağlar

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/tr.md)

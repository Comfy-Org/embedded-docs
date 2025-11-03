> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/tr.md)

Load3D düğümü, 3B model dosyalarını yüklemek ve işlemek için temel bir düğümdür. Düğüm yüklendiğinde, `ComfyUI/input/3d/` dizininden mevcut 3B kaynakları otomatik olarak alır. Ayrıca, yükleme işlevini kullanarak desteklenen 3B dosyalarını önizleme amacıyla yükleyebilirsiniz.

**Desteklenen Biçimler**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden fazla 3B dosya biçimini desteklemektedir.

**3B Düğüm Tercihleri**
3B düğümlerle ilgili bazı tercihler ComfyUI'nin ayarlar menüsünden yapılandırılabilir. İlgili ayarlar için lütfen aşağıdaki belgelere başvurun:

[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

Normal düğüm çıktılarının yanı sıra, Load3D'nin tuval menüsünde birçok 3B görünümle ilgili ayar bulunur.

## Girdiler

| Parametre Adı | Tür     | Açıklama                     | Varsayılan | Aralık        |
|---------------|----------|---------------------------------|---------|--------------|
| model_file    | Dosya Seçimi | 3B model dosya yolu, yüklemeyi destekler, varsayılan olarak model dosyalarını `ComfyUI/input/3d/` dizininden okur | - | Desteklenen biçimler |
| width         | INT      | Tuval işleme genişliği          | 1024    | 1-4096      |
| height        | INT      | Tuval işleme yüksekliği         | 1024    | 1-4096      |

## Çıktılar

| Parametre Adı   | Veri Türü      | Açıklama                        |
|-----------------|----------------|------------------------------------|
| image           | IMAGE          | Tuvalde işlenmiş görüntü              |
| mask            | MASK           | Mevcut model konumunu içeren maske |
| mesh_path       | STRING         | Model dosya yolu                   |
| normal          | IMAGE          | Normal harita                         |
| lineart         | IMAGE          | Çizgi sanatı görüntü çıktısı, karşılık gelen `edge_threshold` tuval model menüsünden ayarlanabilir |
| camera_info     | LOAD3D_CAMERA  | Kamera bilgisi                 |
| recording_video | VIDEO          | Kaydedilmiş video (sadece kayıt mevcut olduğunda) |

Tüm çıktıların önizlemesi:
![Görünüm İşlemleri Demosu](./asset/load3d_outputs.webp)

## Tuval Alanı Açıklaması

Load3D düğümünün Tuval alanı, aşağıdakiler de dahil olmak üzere çok sayıda görünüm işlemi içerir:

- Önizleme görünüm ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanını (FOV), kamera türünü kontrol etme
- Genel aydınlatma yoğunluğu: Işık şiddetini ayarlama
- Video kaydı: Video kaydetme ve dışa aktarma
- Model dışa aktarma: `GLB`, `OBJ`, `STL` biçimlerini destekler
- Ve daha fazlası

![Load 3D Düğümü Kullanıcı Arayüzü](./asset/load3d_ui.jpg)

1. Load 3D düğümünün birden fazla menüsünü ve gizli menülerini içerir
2. `Önizleme penceresini yeniden boyutlandırma` ve `tuval video kaydı` menüsü
3. 3B görünüm işlem ekseni
4. Önizleme küçük resmi
5. Önizleme boyutu ayarları, boyutları ayarlayıp ardından pencereyi yeniden boyutlandırarak önizleme görünümünün ölçeğini belirleme

### 1. Görünüm İşlemleri

<video controls width="640" height="360">
  <source src="./asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Görünüm kontrol işlemleri:

- Sol tıklama + sürükleme: Görünümü döndürme
- Sağ tıklama + sürükleme: Görünümü kaydırma
- Orta tekerlek kaydırma veya orta tıklama + sürükleme: Yakınlaştırma/Uzaklaştırma
- Koordinat ekseni: Görünümleri değiştirme

### 2. Sol Menü İşlevleri

![Menü](./asset/menu.webp)

Tuvalde, bazı ayarlar menü içinde gizlidir. Menü düğmesine tıklayarak farklı menüleri genişletebilirsiniz

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, önizleme ayarlarını içerir
- 2. Model: Model işleme modu, doku malzemeleri, yukarı yön ayarları
- 3. Kamera: Paralel (Orthographic) ve perspektif (Perspective) görünümler arasında geçiş yapma ve perspektif açı boyutunu ayarlama
- 4. Işık: Sahne genel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer biçimlere dışa aktarma (GLB, OBJ, STL)

#### Sahne

![sahne menüsü](./asset/menu_scene.webp)

Sahne menüsü, bazı temel sahne ayar işlevleri sağlar

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarla
3. Bir arka plan görüntüsü yüklemek için tıklayın
4. Önizlemeyi gizle

#### Model

![Menu_Scene](./asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirleme
2. **Malzeme modu**: Model işleme modlarını değiştirme - Orijinal, Normal, Tel Kafes (Wireframe), Çizgi Sanatı (Lineart)

#### Kamera

![menu_modelmenu_camera](./asset/menu_camera.webp)

Bu menü, paralel ve perspektif görünümler arasında geçiş yapma ve perspektif açı boyutu ayarları sağlar

1. **Kamera**: Paralel (Orthographic) ve perspektif (Perspective) görünümler arasında hızlıca geçiş yapma
2. **Görüş Alanı (FOV)**: FOV açısını ayarlama

#### Işık

![menu_modelmenu_camera](./asset/menu_light.webp)

Bu menü aracılığıyla, sahnenin genel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz

#### Dışa Aktar

![menu_export](./asset/menu_export.webp)

Bu menü, model biçimlerini hızlıca dönüştürme ve dışa aktarma yeteneği sağlar

### 3. Sağ Menü İşlevleri

<video controls width="640" height="360">
  <source src="./asset/recording.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Sağ menünün iki ana işlevi vardır:

1. **Görünüm oranını sıfırla**: Düğmeye tıklandıktan sonra, görünüm ayarlanan genişlik ve yüksekliğe göre tuval işleme alanı oranını ayarlayacaktır
2. **Video kaydı**: Mevcut 3B görünüm işlemlerini video olarak kaydetmenize olanak tanır, içe aktarmaya izin verir ve `recording_video` olarak sonraki düğümlere çıktı verebilir
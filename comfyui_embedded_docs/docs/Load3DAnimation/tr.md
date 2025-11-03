> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAnimation/tr.md)

Load3DAnimation düğümü, 3D model dosyalarını yüklemek ve işlemek için temel bir düğümdür. Düğüm yüklendiğinde, otomatik olarak `ComfyUI/input/3d/` dizininden mevcut 3D kaynaklarını getirir. Ayrıca, yükleme işlevini kullanarak desteklenen 3D dosyalarını önizleme için yükleyebilirsiniz.

> - Bu düğümün işlevlerinin çoğu Load 3D düğümü ile aynıdır, ancak bu düğüm animasyonlu modelleri yüklemeyi destekler ve düğüm içinde ilgili animasyonları önizleyebilirsiniz.
> - Bu belgenin içeriği Load3D düğümü ile aynıdır, çünkü animasyon önizleme ve oynatma dışında yetenekleri aynıdır.

**Desteklenen Biçimler**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden fazla 3D dosya biçimini desteklemektedir.

**3D Düğüm Tercihleri**
3D düğümlerle ilgili bazı tercihler ComfyUI'nin ayarlar menüsünden yapılandırılabilir. İlgili ayarlar için lütfen aşağıdaki belgelere bakın:

[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

Düzenli düğüm çıktılarının yanı sıra, Load3D'nin tuval menüsünde birçok 3D görünümle ilgili ayarı bulunur.

## Girdiler

| Parametre Adı | Tür     | Açıklama                     | Varsayılan | Aralık        |
|---------------|----------|---------------------------------|---------|--------------|
| model_file    | Dosya Seçimi | 3D model dosya yolu, yüklemeyi destekler, varsayılan olarak model dosyalarını `ComfyUI/input/3d/` dizininden okur | - | Desteklenen biçimler |
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
| recording_video | VIDEO          | Kaydedilmiş video (yalnızca kayıt mevcut olduğunda) |

Tüm çıktıların önizlemesi:
![Görünüm İşlemi Demosu](../Load3D/asset/load3d_outputs.webp)

## Tuval Alanı Açıklaması

Load3D düğümünün Tuval alanı, aşağıdakiler dahil olmak üzere çok sayıda görünüm işlemi içerir:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanını (FOV), kamera türünü kontrol etme
- Genel aydınlatma yoğunluğu: Işık şiddetini ayarlama
- Video kaydı: Video kaydetme ve dışa aktarma
- Model dışa aktarma: `GLB`, `OBJ`, `STL` biçimlerini destekler
- Ve daha fazlası

![Load 3D Düğümü Kullanıcı Arayüzü](../Load3D/asset/load3d_ui.jpg)

1. Load 3D düğümünün birden fazla menüsünü ve gizli menülerini içerir
2. `Önizleme penceresini yeniden boyutlandırma` ve `tuval video kaydı` menüsü
3. 3D görünüm işleme ekseni
4. Önizleme küçük resmi
5. Önizleme boyutu ayarları, boyutları ayarlayıp ardından pencereyi yeniden boyutlandırarak önizleme görünümü görüntüsünü ölçeklendirme

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

Tuvalde, bazı ayarlar menüde gizlidir. Menü düğmesine tıklayarak farklı menüleri genişletebilirsiniz

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, önizleme ayarlarını içerir
- 2. Model: Model işleme modu, doku malzemeleri, yukarı yön ayarları
- 3. Kamera: Ortografik ve perspektif görünümler arasında geçiş yapma ve perspektif açı boyutunu ayarlama
- 4. Işık: Sahne genel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer biçimlere dışa aktarma (GLB, OBJ, STL)

#### Sahne

![sahne menüsü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Sahne menüsü, bazı temel sahne ayarlama işlevleri sağlar

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarla
3. Bir arka plan görüntüsü yüklemek için tıklayın
4. Önizlemeyi gizle

#### Model

![Menü_Sahne](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirleme
2. **Malzeme modu**: Model işleme modlarını değiştirme - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Bu menü, ortografik ve perspektif görünümler arasında geçiş yapma ve perspektif açı boyutu ayarları sağlar

1. **Kamera**: Ortografik ve perspektif görünümler arasında hızlıca geçiş yapma
2. **Görüş Alanı (FOV)**: FOV açısını ayarlama

#### Işık

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Bu menü aracılığıyla, sahnenin genel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz

#### Dışa Aktar

![menu_export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Bu menü, model biçimlerini hızlıca dönüştürme ve dışa aktarma yeteneği sağlar

### 3. Sağ Menü İşlevleri

<video controls width="640" height="360">
  <source src="../Load3D/asset/recording.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Sağ menünün iki ana işlevi vardır:

1. **Görünüm oranını sıfırla**: Düğmeye tıklandıktan sonra, görünüm ayarlanmış genişlik ve yüksekliğe göre tuval işleme alanı oranını ayarlayacaktır
2. **Video kaydı**: Mevcut 3D görünüm işlemlerini video olarak kaydetmenize izin verir, içe aktarmaya izin verir ve `recording_video` olarak sonraki düğümlere çıktı verebilir
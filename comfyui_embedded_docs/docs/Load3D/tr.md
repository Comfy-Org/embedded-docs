Load3D düğümü, 3B model dosyalarını yüklemek ve işlemek için kullanılan temel bir düğümdür. Düğüm yüklendiğinde, kullanılabilir 3B kaynakları otomatik olarak `ComfyUI/input/3d/` dizininden alır. Ayrıca, yükleme işlevini kullanarak desteklenen 3B dosyalarını önizleme için yükleyebilirsiniz.

**Desteklenen Formatlar**
Bu düğüm şu anda `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden çok 3B dosya formatını desteklemektedir.

**3B Düğüm Tercihleri**
3B düğümleriyle ilgili bazı tercihler, ComfyUI'nin ayarlar menüsünden yapılandırılabilir. İlgili ayarlar için lütfen aşağıdaki belgelere bakın:

[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

Normal düğüm çıktılarının yanı sıra, Load3D'nin tuval menüsünde 3B görünümle ilgili birçok ayarı bulunur.

## Girişler

| Parametre Adı | Açıklama | Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- |
| model_file | 3B model dosya yolu, yüklemeyi destekler, varsayılan olarak `ComfyUI/input/3d/` dizinindeki model dosyalarını okur | Dosya Seçimi | - | Desteklenen formatlar |
| width | Tuval işleme genişliği | INT | 1024 | 1-4096 |
| height | Tuval işleme yüksekliği | INT | 1024 | 1-4096 |

## Çıktılar

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| image | Tuvalde işlenmiş görüntü | IMAGE |
| mask | Geçerli model konumunu içeren maske | MASK |
| mesh_path | Model dosya yolu | STRING |
| normal | Normal harita | IMAGE |
| lineart | Çizgi sanatı görüntü çıktısı, ilgili `edge_threshold` tuval model menüsünden ayarlanabilir | IMAGE |
| camera_info | Kamera bilgisi | LOAD3D_CAMERA |
| recording_video | Kaydedilmiş video (yalnızca kayıt mevcut olduğunda) | VIDEO |

Tüm çıktıların önizlemesi:
![İşlem Demosunu Görüntüle](./asset/load3d_outputs.webp)

## Tuval Alanı Açıklaması

Load3D düğümünün Tuval alanı, aşağıdakiler de dahil olmak üzere çok sayıda görünüm işlemi içerir:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanı (FOV), kamera türü kontrolü
- Küresel aydınlatma yoğunluğu: Işık yoğunluğunu ayarlama
- Video kaydı: Videoları kaydetme ve dışa aktarma
- Model dışa aktarma: `GLB`, `OBJ`, `STL` formatlarını destekler
- Ve daha fazlası

![Load 3D Düğümü Arayüzü](./asset/load3d_ui.jpg)

1. Load 3D düğümünün birden çok menüsünü ve gizli menüsünü içerir
2. `Önizleme penceresini yeniden boyutlandırma` ve `tuval video kaydı` menüsü
3. 3B görünüm işlem ekseni
4. Önizleme küçük resmi
5. Önizleme boyutu ayarları, boyutları ayarlayıp ardından pencereyi yeniden boyutlandırarak önizleme görünümü ekranını ölçekleyin

### 1. Görünüm İşlemleri

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Görünüm kontrol işlemleri:

- Sol tık + sürükle: Görünümü döndürme
- Sağ tık + sürükle: Görünümü kaydırma
- Orta tekerlek kaydırma veya orta tık + sürükle: Yakınlaştırma/Uzaklaştırma
- Koordinat ekseni: Görünümleri değiştirme

### 2. Sol Menü İşlevleri

![Menü](./asset/menu.webp)

Tuvalde bazı ayarlar menüde gizlidir. Farklı menüleri genişletmek için menü düğmesine tıklayın

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, önizleme ayarlarını içerir
- 2. Model: Model oluşturma modu, doku malzemeleri, yukarı yönü ayarları
- 3. Kamera: Dik ve perspektif görünümler arasında geçiş yapma ve perspektif açısı boyutunu ayarlama
- 4. Işık: Sahne küresel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer formatlara (GLB, OBJ, STL) dışa aktarma

#### Sahne

![sahne menüsü](./asset/menu_scene.webp)

Sahne menüsü bazı temel sahne ayarlama işlevleri sağlar

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarlama
3. Arka plan resmi yüklemek için tıklayın
4. Önizlemeyi gizleme

#### Model

![Menu_Scene](./asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar

1. **Yukarı yönü**: Model için hangi eksenin yukarı yönü olduğunu belirleyin
2. **Malzeme modu**: Model oluşturma modlarını değiştirin - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menu_modelmenu_camera](./asset/menu_camera.webp)

Bu menü, dik ve perspektif görünümler arasında geçiş ve perspektif açısı boyutu ayarları sağlar

1. **Kamera**: Dik ve dik görünümler arasında hızlı geçiş yapın
2. **FOV**: Görüş Alanı (FOV) açısını ayarlayın

#### Işık

![menu_modelmenu_camera](./asset/menu_light.webp)

Bu menü aracılığıyla sahnenin küresel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz.

#### Dışa Aktar

![menu_export](./asset/menu_export.webp)

Bu menü, model formatlarını hızlı bir şekilde dönüştürme ve dışa aktarma olanağı sağlar

### 3. Sağ Menü İşlevleri

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Sağ menünün iki ana işlevi vardır:

1. **Görünüm oranını sıfırlama**: Düğmeye tıkladıktan sonra görünüm, ayarlanan genişlik ve yüksekliğe göre tuval işleme alanı oranını ayarlayacaktır
2. **Video kaydı**: Geçerli 3B görünüm işlemlerini video olarak kaydetmenize olanak tanır, içe aktarmaya izin verir ve sonraki düğümlere `recording_video` olarak çıktı verilebilir

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/tr.md)

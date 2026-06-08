Harika, işte uzmanlık alanınıza uygun olarak hazırlanmış Türkçe çeviri:

Load3DAnimation düğümü, 3B model dosyalarını yüklemek ve işlemek için kullanılan temel bir düğümdür. Düğüm yüklendiğinde, `ComfyUI/input/3d/` klasöründeki mevcut 3B kaynakları otomatik olarak alır. Ayrıca, yükleme işlevini kullanarak desteklenen 3B dosyalarını önizleme için yükleyebilirsiniz.

> - Bu düğümün işlevlerinin çoğu, Load 3D düğümüyle aynıdır, ancak bu düğüm, animasyonlu modellerin yüklenmesini destekler ve düğüm içinde ilgili animasyonları önizleyebilirsiniz.
> - Bu dokümantasyonun içeriği, Load3D düğümüyle aynıdır çünkü animasyon önizleme ve oynatma dışında yetenekleri aynıdır.

**Desteklenen Formatlar**
Şu anda bu düğüm, `.gltf`, `.glb`, `.obj`, `.fbx` ve `.stl` dahil olmak üzere birden çok 3B dosya formatını destekler.

**3B Düğüm Tercihleri**
3B düğümleriyle ilgili bazı tercihler, ComfyUI'nin ayarlar menüsünde yapılandırılabilir. İlgili ayarlar için aşağıdaki belgelere bakın:

[Ayarlar Menüsü](https://docs.comfy.org/interface/settings/3d)

Normal düğüm çıktılarının yanı sıra, Load3D, tuval menüsünde 3B görünümle ilgili birçok ayara sahiptir.

## Girişler

| Parametre Adı | Açıklama | Tür | Varsayılan | Aralık |
| --- | --- | --- | --- | --- |
| model_file | 3B model dosya yolu, yüklemeyi destekler, varsayılan olarak `ComfyUI/input/3d/` klasöründeki model dosyalarını okur | Dosya Seçimi | - | Desteklenen formatlar |
| width | Tuval oluşturma genişliği | INT | 1024 | 1-4096 |
| height | Tuval oluşturma yüksekliği | INT | 1024 | 1-4096 |

## Çıktılar

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| image | Oluşturulan tuval görüntüsü | IMAGE |
| mask | Geçerli model konumunu içeren maske | MASK |
| mesh_path | Model dosya yolu | STRING |
| normal | Normal harita | IMAGE |
| lineart | Çizgi sanatı görüntü çıktısı, ilgili `edge_threshold` tuval model menüsünde ayarlanabilir | IMAGE |
| camera_info | Kamera bilgileri | LOAD3D_CAMERA |
| recording_video | Kaydedilen video (yalnızca kayıt mevcutsa) | VIDEO |

Tüm çıktıların önizlemesi:
![Görünüm İşlem Demosu](../Load3D/asset/load3d_outputs.webp)

## Tuval Alanı Açıklaması

Load3D düğümünün Tuval alanı, aşağıdakiler de dahil olmak üzere çok sayıda görünüm işlemi içerir:

- Önizleme görünümü ayarları (ızgara, arka plan rengi, önizleme görünümü)
- Kamera kontrolü: Görüş Alanı (FOV), kamera türü kontrolü
- Küresel aydınlatma yoğunluğu: Aydınlatma yoğunluğunu ayarlama
- Video kaydı: Videoları kaydetme ve dışa aktarma
- Model dışa aktarma: `GLB`, `OBJ`, `STL` formatlarını destekler
- Ve daha fazlası

![Load 3D Düğümü Arayüzü](../Load3D/asset/load3d_ui.jpg)

1. Load 3D düğümünün birden çok menüsünü ve gizli menüsünü içerir
2. `Önizleme penceresini yeniden boyutlandırma` ve `tuval video kaydı` menüsü
3. 3B görünüm işlem ekseni
4. Önizleme küçük resmi
5. Önizleme boyutu ayarları, boyutları ayarlayıp ardından pencereyi yeniden boyutlandırarak önizleme görünümünü ölçeklendirin

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

Tuvalde, bazı ayarlar menüde gizlidir. Farklı menüleri genişletmek için menü düğmesine tıklayın

- 1. Sahne: Önizleme penceresi ızgarası, arka plan rengi, önizleme ayarlarını içerir
- 2. Model: Model oluşturma modu, doku malzemeleri, yukarı yön ayarları
- 3. Kamera: Dik ve perspektif görünümler arasında geçiş yapma ve perspektif açısı boyutunu ayarlama
- 4. Işık: Sahne küresel aydınlatma yoğunluğu
- 5. Dışa Aktar: Modeli diğer formatlara (GLB, OBJ, STL) dışa aktarma

#### Sahne

![sahne menüsü](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Sahne menüsü, bazı temel sahne ayarlama işlevleri sağlar

1. Izgarayı Göster/Gizle
2. Arka plan rengini ayarlama
3. Arka plan resmi yüklemek için tıklayın
4. Önizlemeyi gizle

#### Model

![Menü_Sahne](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Model menüsü, modelle ilgili bazı işlevler sağlar

1. **Yukarı yön**: Model için hangi eksenin yukarı yön olduğunu belirleyin
2. **Malzeme modu**: Model oluşturma modlarını değiştirin - Orijinal, Normal, Tel Kafes, Çizgi Sanatı

#### Kamera

![menü_modelmenü_kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Bu menü, dik ve perspektif görünümler arasında geçiş ve perspektif açısı boyutu ayarları sağlar

1. **Kamera**: Dik ve dik görünümler arasında hızlı geçiş yapın
2. **FOV**: Görüş Alanı (FOV) açısını ayarlayın

#### Işık

![menü_modelmenü_kamera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Bu menü aracılığıyla sahnenin küresel aydınlatma yoğunluğunu hızlıca ayarlayabilirsiniz.

#### Dışa Aktar

![menü_dışa_aktar](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Bu menü, model formatlarını hızlı bir şekilde dönüştürme ve dışa aktarma olanağı sağlar.

### 3. Sağ Menü İşlevleri

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/recording.mp4" type="video/mp4">
  Tarayıcınız video oynatmayı desteklemiyor.
</video>

Sağ menünün iki ana işlevi vardır:

1. **Görünüm oranını sıfırla**: Düğmeye tıkladıktan sonra görünüm, ayarlanan genişlik ve yüksekliğe göre tuval oluşturma alanı oranını ayarlar.
2. **Video kaydı**: Geçerli 3B görünüm işlemlerini video olarak kaydetmenize olanak tanır, içe aktarmaya izin verir ve sonraki düğümlere `recording_video` olarak çıktı verilebilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAnimation/tr.md)

# Load3DAdvanced

Bu düğüm, ComfyUI giriş dizininizden bir 3B model dosyası yükler ve model verilerini kamera ve görünüm alanı bilgileriyle birlikte sağlar. Yaygın 3B dosya biçimlerini destekler ve işleme için çıktı görüntü boyutlarını belirlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Yüklenecek 3B model dosyası. Model yüklemeyi atlamak için "none" seçeneğini belirleyin. | STRING | Evet | `"none"`<br>input/3d dizinindeki mevcut 3B dosyaların listesi |
| `viewport_state` | 3B görüntüleyiciden kamera ve model bilgilerini içeren mevcut görünüm alanı durumu. | LOAD3D | Evet | - |
| `width` | Çıktı görüntüsünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | Min: 1<br>Maks: 4096<br>Adım: 1 |
| `height` | Çıktı görüntüsünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | Min: 1<br>Maks: 4096<br>Adım: 1 |

**Parametrelerle İlgili Notlar:**
- `model_file` parametresi yalnızca şu uzantılara sahip dosyaları gösterir: .gltf, .glb, .obj, .fbx, .stl
- Dosyalar, ComfyUI kurulumunuzun `input/3d` dizinine yerleştirilmelidir
- `model_file` "none" olarak ayarlanırsa, hiçbir 3B model verisi yüklenmez (`model_3d` çıktısı boş olur)

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Yüklenen 3B model verisi veya hiçbir model dosyası seçilmediyse boş | FILE3DANY |
| `model_3d_info` | Görünüm alanı durumundan yüklenen 3B model hakkında bilgi | LOAD3DMODELINFO |
| `camera_info` | Görünüm alanı durumundan kamera bilgisi | LOAD3DCAMERA |
| `width` | Belirtilen çıktı görüntü genişliği | INT |
| `height` | Belirtilen çıktı görüntü yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `fdacea8abf627621150e1196743e36f61534333837c33cc9a7416a6d11700c4d`

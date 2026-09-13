# 3D Yükle (Gelişmiş)

Load 3D (Advanced) düğümü, ComfyUI'nin `input/3d` dizininden bir 3D model dosyası yükler ve model verilerini, 3D görüntüleyicinin görünüm alanı durumunda yakalanan model yerleşimi ve kamera bilgileriyle birlikte sağlar. Yaygın 3D dosya biçimlerini destekler ve görünüm alanının işleme genişliği ile yüksekliğini piksel cinsinden ayarlamanıza olanak tanır. Bu düğüm deneyseldir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Yüklenecek 3D model dosyası. Bir model dosyası yüklemeyi atlamak için "none" seçin. Dosyalar widget aracılığıyla da yüklenebilir. | COMBO | Evet | `"none"`<br>`input/3d` dizinindeki kullanılabilir 3D model dosyaları |
| `viewport_state` | 3D görüntüleyiciden alınan kamera ve model bilgilerini içeren geçerli görünüm alanı durumu. | LOAD3D | Evet | - |
| `width` | Görünüm alanının piksel cinsinden işleme genişliği (varsayılan: 1024). | INT | Evet | Minimum: 1<br>Maksimum: 4096<br>Varsayılan: 1024<br>Adım: 1 |
| `height` | Görünüm alanının piksel cinsinden işleme yüksekliği (varsayılan: 1024). | INT | Evet | Minimum: 1<br>Maksimum: 4096<br>Varsayılan: 1024<br>Adım: 1 |

**Parametre Notları:**
- `model_file` parametresi yalnızca şu uzantılara sahip dosyaları listeler: .gltf, .glb, .obj, .fbx, .stl
- Dosyalar ComfyUI kurulumunuzun `input/3d` dizinine yerleştirilmelidir; alt klasörler de taranır ve dosya yolları girdi dizinine göre gösterilir
- `model_file` "none" ise hiçbir model verisi yüklenmez ve `model_3d` çıktısı boş olur
- `model_file` var olmayan bir dosyaya ayarlanırsa düğüm bir doğrulama hatası döndürür: "Invalid 3D model file: {model_file}"
- `viewport_state` geçerli bir görünüm alanı durumu nesnesi değilse boş olarak değerlendirilir, böylece `model_3d_info` boş bir liste olur ve `camera_info` boş döndürülür

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Yüklenen 3D model dosyası (glb/obj/stl/vb.). Hiçbir model dosyası seçilmediyse boş. | FILE3DANY |
| `model_3d_info` | Sahnede her modelin yerleşimi: konum, dönüş ve ölçek (Y-yukarı dünya uzayı). | LOAD3DMODELINFO |
| `camera_info` | Görünüm alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. | LOAD3DCAMERA |
| `width` | Görünüm alanının piksel cinsinden işleme genişliği. | INT |
| `height` | Görünüm alanının piksel cinsinden işleme yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`

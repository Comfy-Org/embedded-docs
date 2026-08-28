# 3D Önizleme (Gelişmiş)

Bu düğüm, dosyayı ComfyUI çıktı dizinine kaydetmeden 3B model önizlemesini kullanıcı arayüzünde görüntüler. Modeli geçici bir dosyaya kaydeder ve model verilerini, model bilgilerini, kamera bilgilerini ve önizleme boyutlarını aşağı akıştaki işlemler için iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Yukarı akıştaki bir 3B düğümden alınan 3B model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ veya desteklenen herhangi bir 3B formatı |
| `model_3d_bilgisi` | İsteğe bağlı model bilgisi meta verileri. Gelişmiş seçenek. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgilerini içeren geçerli görünüm alanı durumu. | LOAD3D | Evet | - |
| `kamera_bilgisi` | 3B görünümü için isteğe bağlı kamera yapılandırması. Gelişmiş seçenek. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizlemenin piksel cinsinden genişliği. Varsayılan: 1024. | INT | Evet | 1 ila 4096 |
| `yükseklik` | Önizlemenin piksel cinsinden yüksekliği. Varsayılan: 1024. | INT | Evet | 1 ila 4096 |

Not: `camera_info` veya `model_3d_info` bağlı değilse, değerleri mevcutsa `viewport_state`'den alınır. `viewport_state` model bilgisi içermiyorsa, `model_3d_info` varsayılan olarak boş bir listedir. `viewport_state` bir sözlük değilse, boş olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Girdiden geçirilen 3B model dosyası. | FILE3D |
| `kamera_bilgisi` | Model bilgisi meta verileri; girdiden veya görünüm alanı durumundan alınır. | LOAD3DMODELINFO |
| `model_3d_bilgisi` | Kamera yapılandırması; girdiden veya görünüm alanı durumundan alınır. | LOAD3DCAMERA |
| `genişlik` | Önizlemenin piksel cinsinden genişliği. | INT |
| `yükseklik` | Önizlemenin piksel cinsinden yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`

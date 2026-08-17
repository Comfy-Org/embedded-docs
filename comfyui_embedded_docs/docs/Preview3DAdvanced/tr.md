# 3D Önizleme (Gelişmiş)

Bu düğüm, kamera ve model bilgisi çıktısıyla gelişmiş bir 3D model önizlemesi sağlar. 3D model dosyasını ComfyUI çıktı dizinine kaydetmeden önizler; modeli, kullanıcı arayüzünde görüntülenmek üzere geçici bir dosyaya yazar. Model verileri, model bilgisi, kamera bilgisi ve görünüm alanı boyutları da daha sonraki işlemler için aşağı akışa iletilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir önceki 3D düğümünden gelen 3D model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format |
| `model_3d_info` | İsteğe bağlı model bilgisi meta verisi. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgisini içeren geçerli görünüm alanı durumu. | LOAD3D | Evet | - |
| `camera_info` | 3D görünüm için isteğe bağlı kamera yapılandırması. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizlemenin piksel cinsinden genişliği. | INT | Evet | 1 to 4096 (default: 1024) |
| `height` | Önizlemenin piksel cinsinden yüksekliği. | INT | Evet | 1 to 4096 (default: 1024) |

Not: `camera_info` bağlı olmadığında düğüm, `viewport_state` içindeki `camera_info` değerini kullanır. `model_3d_info` bağlı olmadığında düğüm, `viewport_state` içindeki `model_3d_info` değerini; görünüm alanı durumu bunu içermiyorsa boş bir liste kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Girişten geçirilen 3D model dosyası. | FILE3D |
| `model_3d_info` | Girişten veya görünüm alanı durumundan alınan model bilgisi meta verisi. | LOAD3DMODELINFO |
| `camera_info` | Girişten veya görünüm alanı durumundan alınan kamera yapılandırması. | LOAD3DCAMERA |
| `width` | Önizlemenin piksel cinsinden genişliği. | INT |
| `height` | Önizlemenin piksel cinsinden yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`

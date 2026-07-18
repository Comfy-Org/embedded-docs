# Save3DAdvanced

Bu düğüm, bir 3B modeli ComfyUI çıktı dizininize kaydeder ve gelişmiş önizleme özellikleri sunar. Çıktı dosya adını, önizleme boyutlarını ve isteğe bağlı olarak gelişmiş bir 3B görüntüleyici deneyimi için kamera ve model bilgilerini belirlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir üst akış 3B düğümünden gelen 3B model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ veya herhangi bir 3B formatı |
| `filename_prefix` | Kaydedilen dosya adı için ön ek. Otomatik olarak bir sayaç ve dosya uzantısı eklenecektir. (varsayılan: "3d/ComfyUI") | STRING | Evet | Herhangi bir geçerli dosya adı dizesi |
| `viewport_state` | Genellikle bir 3B görüntüleyici düğümünden gelen mevcut görüntü alanı durumu. | LOAD3D | Evet | - |
| `model_3d_info` | Önizleme için isteğe bağlı 3B model bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizlemenin piksel cinsinden genişliği. (varsayılan: 1024) | INT | Evet | 1 ila 4096 |
| `height` | Önizlemenin piksel cinsinden yüksekliği. (varsayılan: 1024) | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Kaydedilen 3B model dosyası. | FILE3D |
| `model_3d_info` | Alt akış düğümleri için iletilen 3B model bilgisi. | LOAD3DMODELINFO |
| `camera_info` | Alt akış düğümleri için iletilen kamera bilgisi. | LOAD3DCAMERA |
| `width` | Alt akış düğümleri için iletilen genişlik değeri. | INT |
| `height` | Alt akış düğümleri için iletilen yükseklik değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`

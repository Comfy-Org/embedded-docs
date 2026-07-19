# Save3DAdvanced

Bu düğüm, ComfyUI çıktı dizininde bir 3B modeli dosyaya kaydeder ve çıktı boyutları ile kamera/görüntü alanı ayarları üzerinde gelişmiş kontrol sağlar. Ayrıca 3B modeli, model bilgilerini, kamera bilgilerini ve boyutları alt akış düğümlerine iletir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `model_3d` | Bir üst akış 3B düğümünden gelen 3B model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ, Herhangi |
| `filename_prefix` | Kaydedilen dosya adı için ön ek (varsayılan: "3d/ComfyUI"). | STRING | Evet | Serbest metin |
| `viewport_state` | Bir 3B Yükle düğümünden gelen, kamera ve model bilgilerini içeren görüntü alanı durumu. | LOAD3D | Evet | - |
| `model_3d_info` | Görüntü alanı durumunu geçersiz kılmak için isteğe bağlı 3B model bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Görüntü alanı durumunu geçersiz kılmak için isteğe bağlı kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `width` | Çıktı ön izlemesinin piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |
| `height` | Çıktı ön izlemesinin piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_3d` | Girişten iletilen 3B model dosyası. | FILE3D |
| `model_3d_info` | Görüntü alanı durumundan veya isteğe bağlı girişten alınan model bilgisi. | LOAD3DMODELINFO |
| `camera_info` | Görüntü alanı durumundan veya isteğe bağlı girişten alınan kamera bilgisi. | LOAD3DCAMERA |
| `width` | Girişten iletilen genişlik değeri. | INT |
| `height` | Girişten iletilen yükseklik değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`

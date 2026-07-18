# 3B Önizleme (Gelişmiş)

Bu düğüm, kamera ve model bilgisi çıktısı ile gelişmiş bir 3B model önizlemesi sağlar. 3B modeli geçici bir dosyaya kaydeder ve kullanıcı arayüzünde görüntüler; ayrıca model verilerini, kamera bilgilerini ve görüntü alanı boyutlarını aşağı akışta daha ileri işleme için iletir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model_3d` | Yukarı akıştaki bir 3B düğümden gelen 3B model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ veya desteklenen herhangi bir 3B formatı |
| `model_3d_bilgisi` | İsteğe bağlı model bilgisi meta verileri. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgilerini içeren mevcut görüntü alanı durumu. | LOAD3D | Evet | - |
| `kamera_bilgisi` | 3B görünüm için isteğe bağlı kamera yapılandırması. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizlemenin piksel cinsinden genişliği. | INT | Evet | 1 ila 4096 (varsayılan: 1024) |
| `yükseklik` | Önizlemenin piksel cinsinden yüksekliği. | INT | Evet | 1 ila 4096 (varsayılan: 1024) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_dosyası` | Girişten iletilen 3B model dosyası. | FILE3D |
| `kamera_bilgisi` | Girişten veya görüntü alanı durumundan gelen model bilgisi meta verileri. | LOAD3DMODELINFO |
| `model_3d_bilgisi` | Girişten veya görüntü alanı durumundan gelen kamera yapılandırması. | LOAD3DCAMERA |
| `genişlik` | Önizlemenin piksel cinsinden genişliği. | INT |
| `yükseklik` | Önizlemenin piksel cinsinden yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `7efe8720f88f7d6234387cd633ea629cbf43a0abea1a9aca6c5dcd43bf7f2145`

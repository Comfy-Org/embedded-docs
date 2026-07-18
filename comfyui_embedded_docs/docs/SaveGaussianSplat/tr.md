# SaveGaussianSplat

Bu düğüm, bir Gaussian splat 3D dosyasını ComfyUI çıktı dizinine kaydeder ve 3D görüntüleyici için önizleme verileri sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|--------|
| `model_3d` | Bir Gaussian splat 3D dosyası. | FILE3D | Evet | - |
| `filename_prefix` | Kaydedilen dosya adı için ön ek (varsayılan: "3d/ComfyUI") | STRING | Evet | - |
| `viewport_state` | Bir 3D yükleyici düğümünden gelen mevcut görüntü alanı durumu. | LOAD3D | Evet | - |
| `model_3d_info` | Önizleme için ek 3D model bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Önizleme için kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizlemenin piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | min: 1, max: 4096, step: 1 |
| `height` | Önizlemenin piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | min: 1, max: 4096, step: 1 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Kaydedilen Gaussian splat 3D dosyası. | FILE3D |
| `model_3d_info` | Önizleme için 3D model bilgisi. | LOAD3DMODELINFO |
| `camera_info` | Önizleme için kamera bilgisi. | LOAD3DCAMERA |
| `width` | Önizlemenin genişliği. | INT |
| `height` | Önizlemenin yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`

# SaveGaussianSplat

Bu düğüm, bir Gaussian splat 3B dosyasını çıktı dizinine kaydeder. Dosya kaydetme işlemini yönetir ve 3B görünüm alanı için önizleme verileri sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir Gaussian splat 3B dosyası. | FILE3D | Evet | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | Kaydedilen dosya adı için ön ek (varsayılan: "3d/ComfyUI"). | STRING | Evet | Geçerli herhangi bir dosya adı ön eki |
| `viewport_state` | Kamera ve model bilgilerini içeren mevcut görünüm alanı durumu. | LOAD3D | Evet | - |
| `model_3d_info` | Görünüm alanı için ek model 3B bilgisi. | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Görünüm alanı önizlemesi için kamera bilgisi. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizlemenin genişliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |
| `height` | Önizlemenin yüksekliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Kaydedilen Gaussian splat 3B dosyası. | FILE3D |
| `model_3d_info` | Görünüm alanı için model 3B bilgisi. | LOAD3DMODELINFO |
| `camera_info` | Görünüm alanı önizlemesi için kamera bilgisi. | LOAD3DCAMERA |
| `width` | Önizlemenin genişliği. | INT |
| `height` | Önizlemenin yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`

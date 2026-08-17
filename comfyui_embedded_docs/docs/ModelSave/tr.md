# ModelKaydet

ModelSave düğümü, eğitilmiş veya değiştirilmiş modelleri bilgisayarınızın depolama alanına kaydeder. Bir modeli girdi olarak alır ve belirttiğiniz dosya adı önekini kullanarak çıktı klasörüne bir safetensors kontrol noktası dosyası olarak yazar. Kullanılabilir olduğunda iş akışı komut istemi ve meta veri bilgileri kaydedilen dosyaya gömülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Diske kaydedilecek model | MODEL | Evet | - |
| `filename_prefix` | Kaydedilen model dosyası için dosya adı ve yol öneki (varsayılan: "diffusion_models/ComfyUI"). Kaydetme sırasında ada bir sayaç eklenir (örneğin, `ComfyUI_00000_.safetensors`). | STRING | Evet | - |
| `prompt` | İş akışı komut istemi bilgisi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek iş akışı meta verileri (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *None* | Bu düğüm herhangi bir çıktı değeri döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`

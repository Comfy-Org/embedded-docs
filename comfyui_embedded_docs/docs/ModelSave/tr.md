# ModelKaydet

ModelSave düğümü, bir modeli bilgisayarınızın depolama alanına `.safetensors` checkpoint dosyası olarak kaydeder. Bir modeli girdi olarak alır ve belirttiğiniz dosya adı ön ekiyle çıktı dizinine yazar. Mevcut olduğunda, iş akışı prompt bilgilerini ve ek meta verileri kaydedilen dosyaya gömer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Diske kaydedilecek model | MODEL | Evet | - |
| `dosyaadı_öneki` | Kaydedilen model dosyası için dosya adı ve yol ön eki (varsayılan: "diffusion_models/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı prompt bilgileri (otomatik sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek iş akışı meta verileri (otomatik sağlanır) | EXTRA_PNGINFO | Hayır | - |

Not: Kaydedilen dosya adı, `filename_prefix` değerinin ardından beş haneli bir sayaç eklenerek oluşturulur (örneğin, `diffusion_models/ComfyUI_00001_.safetensors`). Aynı ön eke sahip bir dosya zaten mevcutsa, yeni dosyanın benzersiz bir ad alması için sayaç artırılır. Mevcut olduğunda, iş akışı promptu, ek meta veriler ve model mimarisi bilgileri kaydedilen dosyaya gömülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *None* | Bu düğüm herhangi bir çıktı değeri döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`

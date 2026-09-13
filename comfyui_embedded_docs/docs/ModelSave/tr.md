# ModelKaydet

ModelSave düğümü, bir MODEL'i bilgisayarınızın depolama alanına `.safetensors` checkpoint dosyası olarak kaydeder. Dosyayı, sağladığınız dosya adı önekini kullanarak ComfyUI'nin çıktı dizinine yazar ve mevcut olduğunda iş akışı istem bilgilerini ve model meta verilerini kaydedilen dosyaya gömer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Diske kaydedilecek model | MODEL | Evet | - |
| `dosyaadı_öneki` | Kaydedilen model dosyası için dosya adı ve yol öneki (varsayılan: "diffusion_models/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı istem bilgisi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek iş akışı meta verileri (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

Not: Kaydedilen dosya adı, `filename_prefix` değerinin ardından beş haneli bir sayaç gelerek oluşturulur (örneğin, `diffusion_models/ComfyUI_00001_.safetensors`). Aynı öneke sahip bir dosya zaten varsa, yeni dosyanın benzersiz bir ad alması için sayaç artırılır. Mevcut olduğunda, iş akışı istemi, ek meta veriler ve model mimarisi bilgileri (örneğin Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion veya Stable Diffusion 3) kaydedilen dosyaya gömülür. Meta veri kaydetme, ComfyUI'nin komut satırı ayarları aracılığıyla devre dışı bırakılmışsa, istem ve ek meta veriler dosyaya yazılmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *None* | Bu düğüm herhangi bir çıktı değeri döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`

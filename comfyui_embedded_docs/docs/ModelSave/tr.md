ModelSave düğümü, eğitilmiş veya değiştirilmiş modelleri bilgisayarınızın depolama alanına kaydeder. Giriş olarak bir model alır ve belirttiğiniz dosya adıyla bir dosyaya yazar. Bu, çalışmalarınızı korumanıza ve modelleri gelecekteki projelerde yeniden kullanmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Diske kaydedilecek model | MODEL | Evet | - |
| `dosyaadı_öneki` | Kaydedilen model dosyası için dosya adı ve yol öneki (varsayılan: "diffusion_models/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı bilgi istemi (otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek iş akışı meta verileri (otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Yok* | Bu düğüm herhangi bir çıktı değeri döndürmez | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`

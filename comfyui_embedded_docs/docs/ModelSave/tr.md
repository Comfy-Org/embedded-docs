> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

ModelSave düğümü, eğitilmiş veya değiştirilmiş modelleri bilgisayarınızın depolama alanına kaydeder. Giriş olarak bir model alır ve belirttiğiniz dosya adıyla bir dosyaya yazar. Bu, çalışmalarınızı korumanıza ve modelleri gelecekteki projelerde yeniden kullanmanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Diske kaydedilecek model |
| `dosyaadı_öneki` | STRING | Evet | - | Kaydedilen model dosyası için dosya adı ve yol öneki (varsayılan: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | İş akışı bilgi istemi (otomatik olarak sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek iş akışı meta verileri (otomatik olarak sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | - | Bu düğüm herhangi bir çıktı değeri döndürmez |

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`

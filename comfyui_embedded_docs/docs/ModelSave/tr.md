> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/tr.md)

ModelSave düğümü, eğitilmiş veya değiştirilmiş modelleri bilgisayarınızın depolama birimine kaydeder. Bir modeli girdi olarak alır ve belirttiğiniz dosya adıyla bir dosyaya yazar. Bu, çalışmanızı korumanıza ve modelleri gelecekteki projelerde yeniden kullanmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Diske kaydedilecek model |
| `filename_prefix` | STRING | Evet | - | Kaydedilen model dosyası için dosya adı ve yol öneki (varsayılan: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | İş akışı istem bilgileri (otomatik olarak sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek iş akışı üst verisi (otomatik olarak sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | - | Bu düğüm herhangi bir çıktı değeri döndürmez |
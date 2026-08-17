# GizliDeğişkeniKaydet

SaveLatent düğümü, latent örnekleri daha sonra kullanmak veya paylaşmak üzere .latent dosyaları olarak diske kaydeder. Belirtilen dosya adı önekini kullanarak latent tensör verilerini çıktı klasörüne yazar ve istem bilgisi gibi isteğe bağlı meta verileri gömer. Düğüm ayrıca orijinal latent örnekleri değiştirilmeden döndürür, böylece iş akışı bunları kullanmaya devam edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Diske kaydedilecek latent örnekler | LATENT | Evet | - |
| `filename_prefix` | Çıktı dosya adını ve alt klasör yolunu oluşturmak için kullanılan önek (varsayılan: "latents/ComfyUI") | STRING | Evet | - |
| `prompt` | İş akışı istem verisi; kaydedilen dosyada JSON meta verisi olarak saklanır (gizli girdi, otomatik olarak sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek iş akışı meta verileri; kaydedilen dosyada JSON olarak saklanır (gizli girdi, otomatik olarak sağlanır) | EXTRA_PNGINFO | Hayır | - |

Not: Meta veriler, ComfyUI `--disable-metadata` bağımsız değişkeniyle başlatılmadığı sürece kaydedilen .latent dosyasına yazılır. Kaydedilen dosya `{filename}_{5 basamaklı sayaç}_.latent` deseni kullanılarak adlandırılır, örneğin `ComfyUI_00001_.latent`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Orijinal latent örnekler, değiştirilmeden döndürülür | LATENT |
| `ui` | Kaydedilen latent dosyası için dosya konumu ayrıntıları (dosya adı, alt klasör ve çıktı türü) | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/tr.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`

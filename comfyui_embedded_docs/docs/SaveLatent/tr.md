# GizliDeğişkeniKaydet

SaveLatent, latent tensörleri `.latent` dosyaları olarak diske kaydeder; böylece daha sonra yeniden kullanılabilir veya paylaşılabilirler. Latent örneklerini alır, otomatik oluşturulan bir adla çıktı klasörüne yazar ve kaydedilen dosyaya prompt gibi iş akışı meta verilerini gömmek mümkündür. Aynı latent örnekler, daha sonraki işlemler için değiştirilmeden iletilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Diske kaydedilecek latent örnekler. | LATENT | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adını oluşturmak için kullanılan önek. Alt klasörler içerebilir, örneğin `latents/ComfyUI` (varsayılan: `latents/ComfyUI`). | STRING | Evet | - |
| `prompt` | JSON olarak serileştirilmiş ve kaydedilen dosya meta verilerinde saklanan iş akışı promptu (gizli parametre, otomatik olarak sağlanır). | PROMPT | Hayır | - |
| `extra_pnginfo` | JSON olarak serileştirilmiş ve kaydedilen dosya meta verilerinde saklanan ek iş akışı bilgisi (gizli parametre, otomatik olarak sağlanır). | EXTRA_PNGINFO | Hayır | - |

Not: Kaydedilen her dosya, önek ve 5 haneli bir sayaç kullanılarak adlandırılır, örneğin `ComfyUI_00001_.latent` ve çıktı dizinine yerleştirilir. Dosya, latent tensörünü ve latent format sürüm işaretçisini içerir. Meta veriler, yalnızca meta veri desteği etkinleştirildiğinde, yani ComfyUI `--disable-metadata` seçeneğiyle başlatılmadığında kaydedilen dosyaya gömülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Girdi olarak sağlanan aynı latent örnekler, değiştirilmeden geçirilir. | LATENT |
| `ui` | Kaydedilen dosyayı tanımlayan arayüz görüntüleme verileri: dosya adı, alt klasör ve çıktı türü (`output`). | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/tr.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`

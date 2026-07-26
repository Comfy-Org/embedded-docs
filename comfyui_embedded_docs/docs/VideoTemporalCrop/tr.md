# Video Kırp (Zamansal)

Bu düğüm, videodan sürekli bir kare aralığı kırpar. Tamamen tembel bir şekilde çalışır; yani, videonun yalnızca seçilen kısmını, iş akışında daha sonra ihtiyaç duyulduğunda işler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|--------|
| `video` | Girdi videosu. | VIDEO | Evet | – |
| `başlangıç_kare` | Başlangıç kare indeksi (varsayılan: 0). | INT | Evet | 0 ile 99999 arası |
| `uzunluk` | Korunacak kare sayısı (varsayılan: 16). | INT | Evet | 1 ile 99999 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Kırpılmış video (tembel). | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/tr.md)

---
**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`

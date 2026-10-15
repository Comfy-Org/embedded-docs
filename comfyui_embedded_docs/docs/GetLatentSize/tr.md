# Get Image/Video Latent Size

Bir görüntü veya video latenti okur ve genişliğini, yüksekliğini, kare sayısını ve toplu iş boyutunu döndürür; böylece geometri, latentin kod çözümü yapılmadan yeniden kullanılabilir. Gürültü maskelerini boyutlandırmak, çözünürlükleri hizalamak veya bir örnekleyiciyi döşerken örtüşmeleri hesaplamak için kullanın. Ölçülen değerler düğümün kendi üzerinde de yazdırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İncelenecek görüntü veya video latenti. Latent birden çok akış içerdiğinde ilk akış ölçülür. | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `width` | Latentin genişliği; piksel cinsinden değil, latent hücreleri cinsindendir. | INT |
| `height` | Latentin yüksekliği; piksel cinsinden değil, latent hücreleri cinsindendir. | INT |
| `frames` | Latentteki kare sayısı. Görüntü latentleri tek bir kareye sahiptir. | INT |
| `batch_size` | Toplu işteki latent sayısı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/tr.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`

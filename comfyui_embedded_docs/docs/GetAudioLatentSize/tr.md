# Get Audio Latent Size

Ses latentini okur ve uzunluğunu, ses kanalı sayısını ve toplu iş boyutunu döndürür; böylece bu değerler sesin kodunu çözmeden yeniden kullanılabilir. Gürültü maskelerini boyutlandırmak veya örnekleme öncesinde ses ve video uzunluklarını eşleştirmek için kullanın. Ölçülen değerler düğümün kendisinde de yazdırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | İncelenecek ses veya ses/video latenti. Latent birden çok akış içerdiğinde ses akışı ölçülür. | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `length` | Ses latenti uzunluğu; ses örnekleri yerine latent hücreleri cinsindendir. | INT |
| `audio_channels` | Ses kanalı sayısı. Ses kanalı boyutu olmayan latentler bir kanal bildirir. | INT |
| `batch_size` | Toplu işteki latent sayısı. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/tr.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`

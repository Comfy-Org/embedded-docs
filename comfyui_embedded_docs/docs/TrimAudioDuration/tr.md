TrimAudioDuration düğümü, bir ses dosyasından belirli bir zaman dilimini kesmenizi sağlar. Kırpmanın ne zaman başlayacağını ve ortaya çıkan ses klibinin ne kadar süreceğini belirleyebilirsiniz. Düğüm, zaman değerlerini ses karesi konumlarına dönüştürerek ve ses dalga formunun ilgili kısmını çıkararak çalışır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Kırpılacak ses girişi | AUDIO | Evet | - |
| `başlangıç_indeksi` | Saniye cinsinden başlangıç zamanı; sondan saymak için negatif olabilir (saniyenin altındaki değerleri destekler). Varsayılan: 0.0 | FLOAT | Evet | -0xffffffffffffffff ile 0xffffffffffffffff arası |
| `süre` | Saniye cinsinden süre. Varsayılan: 60.0 | FLOAT | Evet | 0.0 ile 0xffffffffffffffff arası |

**Not:** Başlangıç zamanı, bitiş zamanından küçük ve ses uzunluğu dahilinde olmalıdır. Negatif başlangıç değerleri, sesin sonundan geriye doğru sayar. Başlangıç zamanı negatifse, sesin sonundan itibaren sayılarak bir kare konumuna dönüştürülür. Başlangıç ve bitiş kareleri, ses sınırlarına kırpılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ses` | Belirtilen başlangıç zamanı ve süre ile kırpılmış ses segmenti | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/tr.md)

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`

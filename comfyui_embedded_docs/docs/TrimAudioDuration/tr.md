> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/tr.md)

TrimAudioDuration düğümü, bir ses dosyasından belirli bir zaman dilimini kesmenizi sağlar. Kırpmanın ne zaman başlayacağını ve ortaya çıkan ses klibinin ne kadar süreceğini belirleyebilirsiniz. Düğüm, zaman değerlerini ses karesi konumlarına dönüştürerek ve ses dalga formunun ilgili kısmını çıkararak çalışır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `audio` | AUDIO | Evet | - | Kırpılacak ses girişi |
| `start_index` | FLOAT | Evet | -0xffffffffffffffff ile 0xffffffffffffffff arası | Saniye cinsinden başlangıç zamanı; sondan saymak için negatif olabilir (saniyenin altındaki değerleri destekler). Varsayılan: 0.0 |
| `duration` | FLOAT | Evet | 0.0 ile 0xffffffffffffffff arası | Saniye cinsinden süre. Varsayılan: 60.0 |

**Not:** Başlangıç zamanı, bitiş zamanından küçük ve ses uzunluğu dahilinde olmalıdır. Negatif başlangıç değerleri, sesin sonundan geriye doğru sayar. Başlangıç zamanı negatifse, sesin sonundan itibaren sayılarak bir kare konumuna dönüştürülür. Başlangıç ve bitiş kareleri, ses sınırlarına kırpılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `audio` | AUDIO | Belirtilen başlangıç zamanı ve süre ile kırpılmış ses segmenti |

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`

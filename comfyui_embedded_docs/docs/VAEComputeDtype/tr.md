# VAE Compute Dtype

Bu düğüm, bir VAE kodlama veya kod çözme gerçekleştirirken kullanılan hesaplama veri türünü ayarlar; model grafiğinin geri kalanını değiştirmez. Giriş VAE'sinin istenen hassasiyete sahip bir kopyasını döndürür; böylece bir iş akışı, bir dalı daha yüksek hassasiyette çalıştırırken diğerleri değişmeden kalabilir. "default", giriş VAE'sinin hâlihazırda kullandığı hesaplama veri türünü korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Ayarlanacak VAE. Düğüm bir kopya üzerinde çalışır, bu nedenle bağlı VAE değiştirilmez. | VAE | Evet | - |
| `dtype` | VAE kodlama ve kod çözme için hesaplama veri türü. "default", giriş VAE'sinin hesaplama veri türünü korur (varsayılan: "default"). | COMBO | Evet | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `vae` | Seçilen hesaplama veri türü uygulanmış VAE kopyası. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/tr.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`

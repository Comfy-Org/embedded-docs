# Wan22FunControlToVideo

Wan22FunControlToVideo düğümü, Wan video model mimarisini kullanarak video üretimi için conditioning ve latent temsilleri hazırlar. Pozitif ve negatif conditioning girdilerini, isteğe bağlı referans görüntüleri ve kontrol videolarıyla birlikte işleyerek video sentezi için gerekli latent uzay temsillerini oluşturur. Düğüm, video modelleri için uygun conditioning verileri üretmek amacıyla uzamsal ölçekleme ve zamansal boyutları yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negative` | Video üretimini yönlendirmek için negatif conditioning girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosu genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı videosu yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Üretilecek video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `ref_image` | Görsel rehberlik sağlamak için isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Üretim sürecini yönlendirmek için isteğe bağlı kontrol videosu | IMAGE | Hayır | - |

**Not:** `length` parametresi 4 karelik bloklar halinde işlenir ve düğüm latent uzay için zamansal ölçeklemeyi otomatik olarak yönetir. `ref_image` sağlandığında, referans latentler aracılığıyla conditioning'i etkiler. `control_video` sağlandığında, conditioning'de kullanılan concat latent temsilini doğrudan etkiler. `start_image` parametresi bu düğümün şemasında bir girdi olarak sunulmaz ancak yürütme mantığında referans verilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | concat latent, mask ve isteğe bağlı referans latentler dahil videoya özgü latent verilerle değiştirilmiş pozitif conditioning | CONDITIONING |
| `negative` | concat latent, mask ve isteğe bağlı referans latentler dahil videoya özgü latent verilerle değiştirilmiş negatif conditioning | CONDITIONING |
| `latent` | Parti boyutu, latent kanalları ve uzamsal/zamansal ölçeklemeye dayalı olarak video üretimi için uygun boyutlara sahip boş latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`

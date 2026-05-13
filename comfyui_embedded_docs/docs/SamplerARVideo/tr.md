> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/en.md)

Sampler AR Video düğümü, Nedensel Zorlama (Causal Forcing) veya Kendi Kendini Zorlama (Self-Forcing) tekniklerini kullananlar gibi otoregresif video modelleri için özel bir örnekleme yöntemi sağlar. Otoregresif (AR) döngüyle ilgili tüm parametreleri doğrudan iş akışı içinde yöneterek, modelin video karelerini adım adım nasıl oluşturacağını yapılandırmayı kolaylaştırır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `num_frame_per_block` | INT | Evet | 1 ila 64 | Otoregresif blok başına kare sayısı. 1 değeri, modelin her seferinde bir kare oluşturduğu anlamına gelir (kare kare), 3 değeri ise üç kareyi birlikte oluşturduğu anlamına gelir (parça parça). Bu ayar, kontrol noktasının eğitim moduyla eşleşmelidir. Varsayılan: 1. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `SAMPLER` | SAMPLER | Belirtilen otoregresif parametrelerle "ar_video" örnekleme işlevini kullanan yapılandırılmış bir örnekleyici nesnesi. |

---
**Source fingerprint (SHA-256):** `5b735f98fdde074ee9483503fee0e2322d510aed846336b382a8ea89a363c9e4`

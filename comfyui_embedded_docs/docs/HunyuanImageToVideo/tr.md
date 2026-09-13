# HunyuanGörüntüdenVideoya

HunyuanImageToVideo düğümü, görüntüleri Hunyuan video modelini kullanarak video latent temsillerine dönüştürür. Video üretim modelleri tarafından daha fazla işlenebilecek video latentleri oluşturmak için koşullandırma girdileri ve isteğe bağlı başlangıç görüntüleri alır. Düğüm, başlangıç görüntüsünün video üretim sürecini nasıl etkileyeceğini kontrol etmek için farklı rehberlik türlerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Çıktı videosundaki kare sayısı (varsayılan: 53, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `guidance_type` | Başlangıç görüntüsünü video üretimine dahil etme yöntemi (varsayılan: "v1 (concat)"). Gelişmiş seçenek | COMBO | Evet | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Video üretimini başlatmak için isteğe bağlı başlangıç görüntüsü (veya görüntü dizisi). Yalnızca ilk `length` kare ve ilk 3 renk kanalı kullanılır | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm seçilen `guidance_type` değerine göre farklı rehberlik yöntemleri kullanır:

- "v1 (concat)": Görüntü latentini video latentine birleştirir ve görüntüyü videoya karıştırmak için bir maske uygular
- "v2 (replace)": İlk video karelerini görüntü latentıyla değiştirir ve bir gürültü maskesi uygular
- "custom": Görüntüyü rehberlik için referans latent olarak kullanır

Eğer `start_image` sağlanmazsa, herhangi bir rehberlik koşullandırması eklenmez ve latent düz bir sıfır bloğu olarak döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | start_image sağlandığında görüntü rehberliği uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `latent` | Video üretim modelleri tarafından daha fazla işlenmeye hazır video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

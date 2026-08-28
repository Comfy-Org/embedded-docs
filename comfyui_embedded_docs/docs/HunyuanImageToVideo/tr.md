# HunyuanGörüntüdenVideoya

HunyuanImageToVideo düğümü, Hunyuan video modelini kullanarak görüntüleri video latent temsillerine dönüştürür. Video oluşturmayı başlatmak için koşullandırma girdileri ve isteğe bağlı başlangıç görüntüleri alır; böylece video üretim modelleri tarafından daha fazla işlenebilecek video latentleri üretir. Düğüm, başlangıç görüntüsünün video oluşturma sürecini nasıl etkileyeceğini kontrol etmek için farklı rehberlik türlerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Çıktı videosundaki kare sayısı (varsayılan: 53, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `rehberlik_türü` | Başlangıç görüntüsünün video oluşturmaya dahil edilme yöntemi (varsayılan: "v1 (concat)"). Gelişmiş seçenek | COMBO | Evet | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `başlangıç_görüntüsü` | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü (veya görüntü dizisi). Yalnızca ilk `length` kare ve ilk 3 renk kanalı kullanılır | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm seçilen `guidance_type` değerine göre farklı rehberlik yöntemleri kullanır:

- "v1 (concat)": Görüntü latentini video latentiyle birleştirir ve görüntüyü videoya harmanlamak için bir maske uygular
- "v2 (replace)": İlk video karelerini görüntü latentiyle değiştirir ve bir gürültü maskesi uygular
- "custom": Görüntüyü rehberlik için referans latent olarak kullanır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | `start_image` sağlandığında görüntü rehberliği uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `gizli` | Video üretim modelleri tarafından daha fazla işlenmeye hazır video latent gösterimi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

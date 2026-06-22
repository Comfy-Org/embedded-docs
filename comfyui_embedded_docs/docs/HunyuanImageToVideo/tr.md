# HunyuanGörüntüdenVideoya

HunyuanImageToVideo düğümü, Hunyuan video modelini kullanarak görüntüleri video gizil (latent) temsillerine dönüştürür. Video oluşturma modelleri tarafından daha fazla işlenebilecek video gizilleri üretmek için koşullandırma girdilerini ve isteğe bağlı başlangıç görüntülerini alır. Düğüm, başlangıç görüntüsünün video oluşturma sürecini nasıl etkileyeceğini kontrol etmek için farklı yönlendirme türlerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, adım: 16) | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK |
| `uzunluk` | Çıktı videosundaki kare sayısı (varsayılan: 53, adım: 4) | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK |
| `toplu_boyut` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `rehberlik_türü` | Başlangıç görüntüsünün video oluşturmaya dahil edilme yöntemi (varsayılan: "v1 (concat)") | COMBO | Evet | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `başlangıç_görüntüsü` | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm seçilen `guidance_type` değerine göre farklı yönlendirme yöntemleri kullanır:

- "v1 (concat)": Görüntü gizilini video giziliyle birleştirir ve görüntüyü videoya harmanlamak için bir maske uygular
- "v2 (replace)": İlk video karelerini görüntü giziliyle değiştirir ve bir gürültü maskesi uygular
- "custom": Görüntüyü yönlendirme için referans gizil olarak kullanır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `gizli` | start_image sağlandığında görüntü yönlendirmesi uygulanmış, değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `latent` | Video oluşturma modelleri tarafından daha fazla işlenmeye hazır video gizil temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`

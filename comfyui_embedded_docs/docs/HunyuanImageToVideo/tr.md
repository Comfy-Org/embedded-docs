> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/tr.md)

HunyuanImageToVideo düğümü, Hunyuan video modelini kullanarak görüntüleri video gizil (latent) temsillerine dönüştürür. Video oluşturma modelleri tarafından daha fazla işlenebilecek video gizilleri üretmek için koşullandırma girdilerini ve isteğe bağlı başlangıç görüntülerini alır. Düğüm, başlangıç görüntüsünün video oluşturma sürecini nasıl etkileyeceğini kontrol etmek için farklı yönlendirme türlerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, adım: 16) |
| `yükseklik` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK | Çıktı videosundaki kare sayısı (varsayılan: 53, adım: 4) |
| `toplu_boyut` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `rehberlik_türü` | COMBO | Evet | "v1 (concat)"<br>"v2 (replace)"<br>"custom" | Başlangıç görüntüsünün video oluşturmaya dahil edilme yöntemi (varsayılan: "v1 (concat)") |
| `başlangıç_görüntüsü` | IMAGE | Hayır | - | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü |

**Not:** `start_image` sağlandığında, düğüm seçilen `guidance_type` değerine göre farklı yönlendirme yöntemleri kullanır:

- "v1 (concat)": Görüntü gizilini video giziliyle birleştirir ve görüntüyü videoya harmanlamak için bir maske uygular
- "v2 (replace)": İlk video karelerini görüntü giziliyle değiştirir ve bir gürültü maskesi uygular
- "custom": Görüntüyü yönlendirme için referans gizil olarak kullanır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `gizli` | CONDITIONING | start_image sağlandığında görüntü yönlendirmesi uygulanmış, değiştirilmiş pozitif koşullandırma |
| `latent` | LATENT | Video oluşturma modelleri tarafından daha fazla işlenmeye hazır video gizil temsili |

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`

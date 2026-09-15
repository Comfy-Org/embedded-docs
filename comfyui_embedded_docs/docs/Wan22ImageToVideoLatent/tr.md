# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent, görüntülerden video latent temsilleri oluşturur. Belirtilen genişlik, yükseklik, kare uzunluğu ve toplu iş boyutuyla boş bir video latent uzayı üretir ve isteğe bağlı olarak başlangıç karelerine bir başlangıç görüntü dizisini kodlayabilir. Bir başlangıç görüntüsü sağlandığında, düğüm onu latent uzayına kodlar ve üretim sırasında hangi bölgelerin gürültüden arındırılacağını işaretleyen ilgili bir gürültü maskesi oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Başlangıç görüntüsünü latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280, adım: 32) | INT | Evet | 32 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704, adım: 32) | INT | Evet | 32 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 49, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Oluşturulacak video latent sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `start_image` | Video latentinin başlangıç karelerine kodlanacak isteğe bağlı başlangıç görüntü dizisi (ilk `length` kareyi kullanır) | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, görüntü dizisi hedef `width` ve `height` değerlerine ölçeklenir, VAE ile kodlanır ve latentin ilk karelerine yerleştirilir. Bu kareler için gürültü maskesi 0 (korunur) olarak ayarlanır; kalan kareler ise 1 (gürültüden arındırılacak) maske değerine sahip olur. Latent her zaman 48 kanala, `height / 16` x `width / 16` uzamsal boyutlarına ve `((length - 1) // 4) + 1` zamansal boyutuna sahiptir. `width` ve `height` 16'ya bölünebilmelidir (32'lik adımla zorunlu kılınır) ve `length` zamansal boyutu 4'lük adımlarla artırır.

`start_image` sağlanmadığında, gürültü maskesi olmadan tamamen boş bir latent döndürülür ve `batch_size` girdisi bu boş latente uygulanmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Oluşturulan video latent temsili, toplu işteki her öğe için yinelenir | LATENT |
| `noise_mask` | Hangi bölgelerin gürültüden arındırılacağını (değer 1) ve hangilerinin kodlanmış başlangıç görüntüsünü koruduğunu (değer 0) belirten gürültü maskesi | LATENT |

Her iki alan da tek bir LATENT çıktısı içinde birlikte döndürülür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`

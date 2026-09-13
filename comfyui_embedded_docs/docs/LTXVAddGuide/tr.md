# LTXVRehberEkle

LTXVAddGuide düğümü, giriş görüntülerini veya videolarını bir VAE kodlayıcı üzerinden kodlar ve bunları bir latent video dizisine kılavuz anahtar kareler olarak ekler. Hem pozitif hem de negatif koşullandırmayı günceller ve değiştirilmiş latent verisini döndürür; ayrıca başlangıç karesini, koşullandırma gücünü, isteğe bağlı bir dikkat maskesini ve isteğe bağlı IC-LoRA parametrelerini ayarlama seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Anahtar kare kılavuzlaması ile değiştirilecek pozitif koşullandırma girişi. | CONDITIONING | Evet | - |
| `negative` | Anahtar kare kılavuzlaması ile değiştirilecek negatif koşullandırma girişi. | CONDITIONING | Evet | - |
| `vae` | Giriş görüntü/video karelerini kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `latent` | Koşullandırma karelerini alacak giriş latent dizisi. | LATENT | Evet | - |
| `image` | Latent videoyu koşullandırmak için kullanılacak görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kareye kırpılır. | IMAGE | Evet | - |
| `frame_idx` | Koşullandırmanın başlatılacağı kare indeksi. Tek karelik görüntüler veya 1-8 karelik videolar için herhangi bir frame_idx değeri kabul edilebilir. 9+ kareli videolar için frame_idx 8'e bölünebilir olmalıdır; aksi takdirde en yakın 8'in katına aşağı yuvarlanır. Negatif değerler videonun sonundan itibaren sayılır. Varsayılan: 0. | INT | Evet | -9999 ile 9999 |
| `strength` | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygular ve 0.0 hiç koşullandırma uygulamaz. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 10.0 |
| `attention_mask` | İsteğe bağlı piksel uzayı uzamsal maskesi. Öz-dikkat yoluyla bölge başına koşullandırma etkisini kontrol eder; strength ile çarpılır. | MASK | Hayır | - |
| `iclora_parameters` | Bir Get IC-LoRA Parameters düğümünden isteğe bağlı IC-LoRA parametreleri. Belirli IC-LoRA'ların gerektirdiği şekilde kılavuz işlemeyi ayarlamak için kullanılır (örn. reference_downscale_factor > 1 olanlar). Zincirlendiğinde, her LTXVAddGuide yalnızca kendisine bağlanan parametreleri kullanır. | IC_LORA_PARAMETERS | Hayır | - |

**Not:** Giriş görüntüsü/videosu, 8*n + 1 desenine uyan bir kare sayısına sahip olmalıdır (örn. 1, 9, 17, 25 kare). Giriş bu deseni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılır.

**`iclora_parameters` hakkında not:** `reference_downscale_factor` 1'den büyük olan IC-LoRA parametrelerini kullanırken, latent uzamsal boyutları (genişlik ve yükseklik) bu faktöre bölünebilir olmalıdır. Bu koşul karşılanmazsa düğüm bir hata verir.

**Not:** Kodlanan kılavuz kareleri, seçilen kare konumunda latent diziye sığmalıdır. Koşullandırılan kareler latent dizinin uzunluğunu aşarsa, düğüm bir hata verir.

**Not:** Ses ve video kanallarını birleştiren bir latent'e kılavuz eklemek desteklenmez ve bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Anahtar kare kılavuzlaması bilgisiyle güncellenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Anahtar kare kılavuzlaması bilgisiyle güncellenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Koşullandırma kareleri dahil edilmiş ve gürültü maskesi güncellenmiş latent dizi. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`

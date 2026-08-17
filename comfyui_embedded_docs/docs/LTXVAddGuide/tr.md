# LTXVRehberEkle

LTXVAddGuide, giriş görüntülerini veya videolarını kodlayarak ve bunları koşullandırma verisine ana kareler olarak dahil ederek latent dizilere video koşullandırma kılavuzluğu ekler. Girişi bir VAE kodlayıcı aracılığıyla işler ve elde edilen latentleri belirtilen kare konumlarına stratejik olarak yerleştirirken, hem pozitif hem de negatif koşullandırmayı ana kare bilgileriyle günceller. Düğüm, kare hizalama kısıtlamalarını ele alır ve koşullandırma etkisinin gücü üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Ana kare kılavuzluğuyla değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Ana kare kılavuzluğuyla değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Giriş görüntüsünü/video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `latent` | Koşullandırma karelerini alacak girdi latent dizisi | LATENT | Evet | - |
| `image` | Latent videoyu koşullandırmak için kullanılacak görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kare sayısına kırpılır. | IMAGE | Evet | - |
| `frame_idx` | Koşullandırmanın başlatılacağı kare dizini. Tek kareli görüntüler veya 1-8 kareli videolar için herhangi bir frame_idx değeri kabul edilebilir. 9+ kareli videolar için frame_idx 8'e bölünebilir olmalıdır, aksi takdirde en yakın 8'in katına yuvarlanır. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) | INT | Hayır | -9999 to 9999 |
| `strength` | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygular, 0.0 hiç koşullandırma uygulamaz (varsayılan: 1.0) | FLOAT | Hayır | 0.0 to 10.0 |
| `attention_mask` | İsteğe bağlı piksel uzayı uzamsal maskesi. Öz-dikkat yoluyla bölge bazında koşullandırma etkisini kontrol eder; strength ile çarpılır. | MASK | Hayır | - |
| `iclora_parameters` | Get IC-LoRA Parameters düğümünden alınan isteğe bağlı IC-LoRA parametreleri. Belirli IC-LoRA'ların (ör. `reference_downscale_factor` > 1 olanlar) gerektirdiği şekilde kılavuz işlemeyi ayarlamak için kullanılır. Zincirlendiğinde, her LTXVAddGuide yalnızca kendisine bağlı parametreleri kullanır. | IC_LORA_PARAMETERS | Hayır | - |

**Notlar:**

- Giriş görüntüsü/videosu, 8*n + 1 kare desenini izlemelidir (ör. 1, 9, 17, 25 kare). Giriş bu deseni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılır.
- `reference_downscale_factor` değeri 1'den büyük olan IC-LoRA parametreleri kullanılırken, latent uzamsal boyutları (genişlik ve yükseklik) bu faktöre bölünebilir olmalıdır. Bu koşul sağlanmazsa düğüm bir hata verir.
- Kılavuz, latent diziye sığmalıdır: başlangıç kare dizini ile kılavuz kare sayısının toplamı, latent uzunluğunu aşamaz; aksi takdirde düğüm bir hata verir.
- Düğüm, birleşik ses-video latentlerini desteklemez. Hem `latent` girişi hem de kodlanmış kılavuz, standart 128 kanallı video latent formatını kullanmalıdır; aksi takdirde düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Ana kare kılavuz bilgisiyle güncellenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Ana kare kılavuz bilgisiyle güncellenmiş negatif koşullandırma | CONDITIONING |
| `latent` | İçerisine koşullandırma kareleri eklenmiş ve gürültü maskesi güncellenmiş latent dizi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`

# LTXVRehberEkle

LTXVAddGuide düğümü, giriş görüntülerini veya videolarını kodlayarak ve bunları koşullandırma verilerine anahtar kareler olarak dahil ederek latent dizilere video koşullandırma rehberliği ekler. Girişi bir VAE kodlayıcı aracılığıyla işler ve ortaya çıkan latentleri belirtilen kare konumlarına stratejik olarak yerleştirirken, hem pozitif hem de negatif koşullandırmayı anahtar kare bilgileriyle günceller. Düğüm, kare hizalama kısıtlamalarını yönetir ve koşullandırma etkisinin gücü üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Anahtar kare rehberliğiyle değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Anahtar kare rehberliğiyle değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Giriş görüntüsünü/video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `gizli` | Koşullandırma karelerini alacak giriş latent dizisi | LATENT | Evet | - |
| `görüntü` | Latent videonun koşullandırılacağı görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kareye kırpılır. | IMAGE | Evet | - |
| `kare_indeksi` | Koşullandırmanın başlayacağı kare dizini. Tek karelik görüntüler veya 1-8 kareli videolar için herhangi bir frame_idx değeri kabul edilebilir. 9+ kareli videolar için frame_idx 8'e bölünebilir olmalıdır, aksi takdirde 8'in en yakın katına aşağı yuvarlanır. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) | INT | Evet | -9999 ila 9999 |
| `güç` | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygular, 0.0 koşullandırma uygulamaz (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 10.0 |
| `attention_mask` | İsteğe bağlı piksel uzayı uzamsal maskesi. Öz-dikkat yoluyla bölge bazında koşullandırma etkisini kontrol eder, strength ile çarpılır. | MASK | Hayır | - |
| `iclora_parameters` | Get IC-LoRA Parameters düğümünden alınan isteğe bağlı IC-LoRA parametreleri. Belirli IC-LoRA'ların gerektirdiği şekilde rehber işlemeyi ayarlamak için kullanılır (örn. reference_downscale_factor > 1 olanlar). Zincirlendiğinde, her LTXVAddGuide yalnızca kendisine bağlı parametreleri kullanır. | IC_LORA_PARAMETERS | Hayır | - |

**Not:** Giriş görüntüsü/videosu, 8*n + 1 desenini izleyen bir kare sayısına sahip olmalıdır (örn. 1, 9, 17, 25 kare). Giriş bu deseni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılır.

**`iclora_parameters` hakkında not:** `reference_downscale_factor` değeri 1'den büyük olan IC-LoRA parametreleri kullanılırken, latent uzamsal boyutları (genişlik ve yükseklik) bu faktöre bölünebilir olmalıdır. Bu koşul sağlanmazsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Anahtar kare rehberlik bilgileriyle güncellenmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Anahtar kare rehberlik bilgileriyle güncellenmiş negatif koşullandırma | CONDITIONING |
| `gizli` | Dahil edilmiş koşullandırma kareleri ve güncellenmiş gürültü maskesi içeren latent dizisi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`

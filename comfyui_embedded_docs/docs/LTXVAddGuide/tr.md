> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

LTXVAddGuide düğümü, giriş görüntülerini veya videolarını kodlayarak ve bunları kare anahtarları olarak koşullandırma verilerine dahil ederek, latent dizilere video koşullandırma yönlendirmesi ekler. Girişi bir VAE kodlayıcı aracılığıyla işler ve ortaya çıkan latentleri, belirtilen kare konumlarına stratejik olarak yerleştirirken, hem pozitif hem de negatif koşullandırmayı kare anahtarı bilgileriyle günceller. Düğüm, kare hizalama kısıtlamalarını yönetir ve koşullandırma etkisinin gücü üzerinde kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `positive` | CONDITIONING | Evet | - | Kare anahtarı yönlendirmesi ile değiştirilecek pozitif koşullandırma girişi |
| `negative` | CONDITIONING | Evet | - | Kare anahtarı yönlendirmesi ile değiştirilecek negatif koşullandırma girişi |
| `vae` | VAE | Evet | - | Giriş görüntüsünü/video karelerini kodlamak için kullanılan VAE modeli |
| `latent` | LATENT | Evet | - | Koşullandırma karelerini alacak giriş latent dizisi |
| `image` | IMAGE | Evet | - | Latent videonun koşullandırılacağı görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kareye kırpılır. |
| `frame_idx` | INT | Hayır | -9999 ila 9999 | Koşullandırmanın başlatılacağı kare dizini. Tek kareli görüntüler veya 1-8 kareli videolar için herhangi bir frame_idx değeri kabul edilebilir. 9+ kareli videolar için frame_idx, 8'e bölünebilir olmalıdır, aksi takdirde 8'in en yakın katına yuvarlanır. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) |
| `strength` | FLOAT | Hayır | 0.0 ila 1.0 | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygularken, 0.0 hiç koşullandırma uygulamaz (varsayılan: 1.0) |

**Not:** Giriş görüntüsü/videosu, 8*n + 1 desenini izleyen bir kare sayısına sahip olmalıdır (örneğin, 1, 9, 17, 25 kare). Giriş bu deseni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Kare anahtarı yönlendirme bilgileriyle güncellenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Kare anahtarı yönlendirme bilgileriyle güncellenmiş negatif koşullandırma |
| `latent` | LATENT | Dahil edilmiş koşullandırma kareleri ve güncellenmiş gürültü maskesi ile latent dizi |

---
**Source fingerprint (SHA-256):** `e7f4e6ed25cddd4b50b98341c63fc9915afc4956317ac7a5a9121fdc53c03a2d`

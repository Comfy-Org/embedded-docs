> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

LTXVAddGuide düğümü, girdi görüntülerini veya videolarını kodlayarak ve bunları koşullandırma verilerine ana kareler olarak dahil ederek, gizli dizilere video koşullandırma kılavuzu ekler. Girdiyi bir VAE kodlayıcı aracılığıyla işler ve ortaya çıkan gizli öğeleri belirtilen kare konumlarına stratejik olarak yerleştirirken, hem pozitif hem de negatif koşullandırmayı ana kare bilgileriyle günceller. Düğüm, kare hizalama kısıtlamalarını ele alır ve koşullandırma etkisinin gücü üzerinde kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Ana kare kılavuzu ile değiştirilecek pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Ana kare kılavuzu ile değiştirilecek negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Girdi görüntüsünün/video karelerinin kodlanmasında kullanılan VAE modeli |
| `latent` | LATENT | Evet | - | Koşullandırma karelerini alacak olan girdi gizli dizisi |
| `image` | IMAGE | Evet | - | Gizli videoyu koşullandırmak için kullanılan görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kareye kırpılacaktır. |
| `frame_idx` | INT | Hayır | -9999 - 9999 | Koşullandırmanın başlayacağı kare indeksi. Tek kareli görüntüler veya 1-8 kareye sahip videolar için herhangi bir frame_idx değeri kabul edilebilir. 9+ kareye sahip videolar için frame_idx 8'e bölünebilir olmalıdır, aksi takdirde en yakın 8 katına aşağı yuvarlanacaktır. Negatif değerler videonun sonundan sayılır. (varsayılan: 0) |
| `strength` | FLOAT | Hayır | 0.0 - 1.0 | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygular, 0.0 ise hiç koşullandırma uygulamaz (varsayılan: 1.0) |

**Not:** Girdi görüntüsü/videosu 8*n + 1 desenini takip eden bir kare sayısına sahip olmalıdır (örneğin, 1, 9, 17, 25 kare). Girdi bu deseni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılacaktır.

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Ana kare kılavuz bilgisi ile güncellenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Ana kare kılavuz bilgisi ile güncellenmiş negatif koşullandırma |
| `latent` | LATENT | Birleştirilmiş koşullandırma kareleri ve güncellenmiş gürültü maskesi içeren gizli dizi |
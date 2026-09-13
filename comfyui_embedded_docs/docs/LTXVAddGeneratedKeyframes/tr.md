# LTXV Oluşturulan Anahtar Kareleri Ekle

LTXV Add Generated Keyframes düğümü, bir video latente detaylandırma ana kareleri ekler. Her ana kare, tek bir piksel kare üzerine yerleştirilmiş tokenlardan oluşan bir latent karesidir; video ile birlikte gürültüden arındırılır ve çözülen çıktının parçası değildir. Yerleştirme, her `interval_frames` pikselde bir yuvadır; I2V kareleri, mevcut kılavuzlar ve koşullandırma üzerinde zaten bulunan oluşturulmuş ana kareler atlanır; onları LTXV Separate Generated Keyframes ile geri çıkarın. Oluşturulmuş ana kareler için eğitilmiş bir checkpoint (`keyframes_abs_pos_embedding` taşıyan bir tanesi) gereklidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Ana karelerin bağlandığı pozitif koşullandırma. | CONDITIONING | Evet | N/A |
| `negative` | Ana karelerin bağlandığı negatif koşullandırma. | CONDITIONING | Evet | N/A |
| `vae` | Yalnızca latent ölçek faktörlerini okumak için kullanılır. | VAE | Evet | N/A |
| `latent` | Yanında ana kareler oluşturmak için düz 5D video latent. Bunları Concat AV Latent'ten önce ekleyin. | LATENT | Evet | N/A |
| `interval_frames` | Otomatik yerleştirme için piksel kare adımı. Varsayılan 24, 24 fps'de yaklaşık saniyede bir ana kare anlamına gelir. Kullanılan pikseller atlanır. `frame_indices` ayarlandığında yok sayılır. (varsayılan: 24) | INT | Hayır | 1-1024 |
| `keyframes` | Yeni ana kareleri başlatmak için isteğe bağlı içerik. Daha önceki bir Separate düğümünden ana kareleri (aynı uzamsal boyutta) bağlayın veya her yeni yuvada en yakın kareyi kopyalamak için düz bir video latent bağlayın (örn. zamansal büyütmeden sonra). Bunlar yine de gürültüden arındırılır, kılavuz olarak sabitlenmez. `frame_indices` ayarlanmadıkça bir ana kareler latentindeki kayıtlı indeksler yok sayılır. Yalnızca örnekleme sigma 1'in altında başladığında etkisi olur. | LATENT | Hayır | N/A |
| `frame_indices` | İsteğe bağlı piksel kare indeksleri. Geçerli tuval üzerinde `interval_frames` değerinden yerleştirmek için boş bırakın. Ayarlandığında, bu liste yerleşimdir (bağlı ana kareler sırayla eşleştirilir). Son kareye izin verilir; 0. kareye izin verilmez (zaten bağımsız bir tokendır). (varsayılan: boş dize) | STRING | Hayır | Virgülle ayrılmış tamsayılar; 1'den son piksel karesine kadar (0. kare hariç) |

**Not:** `latent`, Concat AV Latent'ten önce oluşturulmuş ana kareler eklenmiş düz bir 5D video latent olmalıdır. `frame_indices` ayarlandığında, listelenen her piksel karesi benzersiz olmalı ve hâlihazırda bir görüntü ana karesi, bir kılavuz veya oluşturulmuş bir ana kare içermemelidir. `frame_indices` boşsa, kullanılan pikseller otomatik olarak atlanır; boş bir detaylandırma yuvası yoksa düğüm bir hata verir. Mevcut oluşturulmuş ana karelere ekleme yaparken, latent yine de kare başına aynı tokenlara sahip olmalı ve mevcut blok son latent karesinde bitmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Oluşturulmuş ana kare dikkati eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Oluşturulmuş ana kare dikkati eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | T üzerinde oluşturulmuş ana kareler eklenmiş video latent. | LATENT |

## Notlar

- `interval_frames` parametresi, otomatik yerleştirilen ana karelerin aralığını belirler. Daha yüksek bir değer daha az ana kare ve daha geniş aralıklarla sonuçlanır; daha düşük bir değer daha fazla ana kare üretir.
- `keyframes` girdisi, yeni ana kareleri mevcut ana karelerle veya bir video latent ile başlatmanıza olanak tanır. Daha uzun düz bir video latent sağlanırsa, her yeni yuvada en yakın video karesi kopyalanır. Bu ana kareler yine de gürültüden arındırılır ve kılavuz olarak sabitlenmez.
- `frame_indices` parametresi, ana karelerin yerleştirileceği tam piksel kare indekslerini belirtmenize olanak tanır. Sağlandığında, `interval_frames` yok sayılır. Liste, geçerli piksel aralığında benzersiz tamsayılar içermelidir ve 0. kareye izin verilmez.
- `positive` ve `negative` çıktıları, oluşturulmuş ana kare dikkati eklenmiş koşullandırmayı içerir.
- `latent` çıktısı, T üzerinde oluşturulmuş ana kareler eklenmiş video latentini içerir.
- Oluşturulmuş ana kareler için eğitilmiş bir checkpoint (`keyframes_abs_pos_embedding` taşıyan bir tanesi) gereklidir.
- Oluşturulmuş ana kareleri LTXV Separate Generated Keyframes ile geri çıkarın.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`

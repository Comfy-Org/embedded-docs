# LTXV Oluşturulan Anahtar Kareleri Kılavuzlara Dönüştür

LTXV Generated Keyframes to Guides düğümü, önceki bir aşamada oluşturulan anahtar kareleri sonraki bir tuval üzerinde dondurulmuş görüntü kılavuzları olarak sabitler. Anahtar kareleri bağımsız kareler olarak çözer, gerekirse yeniden boyutlandırır ve yeniden gürültüsüzleştirilmemeleri için 0 gürültü maskesiyle yazar. Zamansal ölçeklendirmeden sonra, kaydedilen indeksler oluşturuldukları tuvalden bu tuvale ölçeklenir; konumları açıkça ayarlamak için `override_frame_indices` kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pozitif` | Anahtar kare kılavuzlarının ekleneceği pozitif koşullandırma. | CONDITIONING | Evet | |
| `negatif` | Anahtar kare kılavuzlarının ekleneceği negatif koşullandırma. | CONDITIONING | Evet | |
| `vae` | Yeniden boyutlandırma gerekirse anahtar kareleri çözmek için kullanılan VAE. | VAE | Evet | |
| `latent` | Kılavuzların ekleneceği hedef video latent değeri; örn. zamansal olarak ölçeklendirilmiş olan. | LATENT | Evet | |
| `anahtar kareler` | LTXV Separate Generated Keyframes düğümünün, her anahtar karenin üretildiği piksel kare indeksini taşıyan keyframes çıktısı. | LATENT | Evet | |
| `güç` | Kılavuz gücü. 1.0 katı bir sabitlemedir; daha düşük değerler gevşetir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 (adım 0.01) |
| `override_frame_indices` | İsteğe bağlı — kaydedilen (veya otomatik ölçeklenen) konumlar yerine bu piksel karelerine sabitleyin. Her anahtar kare için bir indeks sağlayın. Kaydedilen konumları yeniden kullanmak veya hedef tuval farklı uzunluktaysa (örn. zamansal x2 sonrası) bunları ölçeklemek için boş bırakın. (varsayılan: "") | STRING | Hayır | |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Anahtar karelerin görüntü kılavuzları olarak sabitlendiği pozitif koşullandırma. | CONDITIONING |
| `negative` | Anahtar karelerin görüntü kılavuzları olarak sabitlendiği negatif koşullandırma. | CONDITIONING |
| `latent` | Anahtar karelerin dondurulmuş kılavuzlar olarak eklendiği hedef video latent değeri. | LATENT |

## Notlar

- `keyframes` girdisi, LTXV Separate Generated Keyframes düğümünün keyframes çıktısına bağlanmalıdır. Latent, oluşturulmuş anahtar kare konumlarını taşımıyorsa düğüm bir hata verir.
- `positive` ve `negative` koşullandırma girdileri, LTXV Separate Generated Keyframes düğümünün positive ve negative çıktılarından gelmelidir. Pozitif koşullandırma hâlâ oluşturulmuş anahtar kareler taşıyorsa düğüm bir hata verir.
- `latent` girdisi düz bir video latent (5D tensör) olmalıdır. Kılavuzlar, Concat AV Latent ile video ve ses latentleri birleştirilmeden önce eklenmelidir.
- Yalnızca 1 toplu iş boyutu desteklenir. Her kılavuz tek bir görüntüden kodlandığı için toplu iş öğeleri arasında farklılık gösteremez.
- `keyframes` latent değerindeki anahtar kare sayısı, kaydedilen konumların sayısıyla eşleşmelidir; aksi takdirde bir hata oluşur.
- `override_frame_indices` boş bırakılırsa kaydedilen konumlar kullanılır. Hedef tuval, anahtar karelerin oluşturulduğu tuvalden farklı sayıda kareye sahipse kaydedilen indeksler otomatik olarak ölçeklenir.
- `override_frame_indices` sağlanırsa, virgül veya boşlukla ayrılmış olarak her anahtar kare için bir tam sayı indeks içermelidir. İndeksler benzersiz olmalı ve 1 ile (hedef latentteki piksel kare sayısı - 1) arasında olmalıdır. Aksi takdirde bir hata oluşur.
- Herhangi bir nihai anahtar kare indeksi, hedef latentteki piksel kare sayısından büyük veya bu sayıya eşitse düğüm bir hata verir. Bu, anahtar kareler oluşturulduktan sonra hedef zamansal olarak yeniden boyutlandırıldığında meydana gelebilir.
- `strength` parametresinin minimumu 0.0 ve maksimumu 10.0'dır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/tr.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`

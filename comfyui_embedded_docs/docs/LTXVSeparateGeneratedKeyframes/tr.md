# LTXV Oluşturulan Anahtar Kareleri Ayır

## Genel Bakış

LTXV Separate Generated Keyframes düğümü, LTXV Add Generated Keyframes tarafından eklenen oluşturulan anahtar kareleri örneklenmiş bir latentten ayırır ve bunları koşullandırmadan kaldırır. Video latentini uzamsal olarak büyütmeden önce kullanın. Önce LTXV Crop Guides çalıştırmayın — oluşturulan anahtar kareleri tek kullanımlık kılavuzlar olarak ele alır ve onları atar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Oluşturulan anahtar kare meta verilerini tutan pozitif koşullandırma. Çıktıda meta veriler ondan kaldırılır. | CONDITIONING | Evet | N/A |
| `negative` | Oluşturulan anahtar kare meta verilerini tutan negatif koşullandırma. Çıktıda meta veriler ondan kaldırılır. | CONDITIONING | Evet | N/A |
| `latent` | Oluşturulan anahtar kareleri içeren video latent. Çıktıda anahtar kareler ondan çıkarılır. | LATENT | Evet | N/A |
| `keyframes_to_batch` | Anahtar kareleri tek kareli latentlerden oluşan bir grup olarak döndürün. Tek bir çok kareli latent olarak almak için kapalı bırakın; latent büyütücü ve daha sonraki bir Add Generated Keyframes düğümünün beklediği şey budur. | BOOLEAN | Hayır | varsayılan: False |

### Girdilerle İlgili Notlar

- `positive`, oluşturulan anahtar kare meta verilerini içermelidir; aksi halde düğüm, bunları önce LTXV Add Generated Keyframes ile eklemenizi söyleyen bir hata verir.
- `latent` düz bir video latent (5D tensör) olmalıdır. Video ve ses latentleri hâlâ birleşikse, önce bunları Separate AV Latent ile ayırın.
- Anahtar kareler eklendiğinde kaydedilen latent kare başına token sayısı, sağlanan `latent`in kare başına token sayısıyla eşleşmelidir. Anahtar kareler eklendikten sonra latent yeniden ölçeklendirilmişse, artık hizalanmazlar ve düğüm bir hata verir — latent'i büyütmeden önce bunları ayırın.
- Kaydedilen anahtar karelerin kare aralığı, sağlanan `latent`in içine sığmalıdır; aksi halde düğüm, anahtar karelerin farklı bir latent'e göre kaydedildiğine dair bir hata verir.
- Kaydedilen kılavuz dikkat girdisi indeksi, koşullandırmada hâlâ mevcut olmalıdır. Anahtar kareler eklendikten sonra koşullandırma yeniden oluşturulmuşsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Oluşturulan anahtar kare meta verileri kaldırılmış pozitif koşullandırma. | CONDITIONING |
| `negative` | Oluşturulan anahtar kare meta verileri kaldırılmış negatif koşullandırma. | CONDITIONING |
| `latent` | Oluşturulan anahtar karelerin çıkarıldığı video latent. | LATENT |
| `keyframes` | Çıkarılan anahtar kareler; generated_keyframe_indices ve generated_keyframe_num_frames ile etiketlenir. Bunları, yeni yuvaları başlatmak için daha sonraki bir Add Generated Keyframes düğümüne veya onları donmuş görüntü kılavuzları olarak sabitlemek için Generated Keyframes To Guides düğümüne besleyin (tuval uzunluğu değiştiyse indeksler yeniden eşlenir). | LATENT |

## Notlar

- `keyframes_to_batch` parametresi, anahtar karelerin tek kareli latentlerden oluşan bir grup olarak mı yoksa tek bir çok kareli latent olarak mı döndürüleceğini belirler.
- Düğüm, herhangi bir ileri işlemeden önce oluşturulan anahtar karelerin koşullandırmadan ve latentten kaldırılmasını sağlar.
- `keyframes` çıktısı, oluşturulan anahtar kareler için yeni yuvaları başlatmak veya bunları donmuş görüntü kılavuzları olarak sabitlemek için kullanılabilir.
- Düğüm, latent oluşturulan anahtar kareleri içermiyorsa veya anahtar kareler beklenen biçimle eşleşmiyorsa bir `ValueError` hatası verir.
- Düğüm, oluşturulan anahtar karelerin LTXV Add Generated Keyframes düğümü kullanılarak eklendiğini ve mevcut latentle uyumlu olduklarını varsayar.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`

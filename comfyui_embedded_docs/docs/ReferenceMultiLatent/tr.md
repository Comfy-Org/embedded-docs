# Set Reference Multi Latent

Bu düğüm, bir veya daha fazla referans görüntüyü kodlar ve latentlerini bir düzenleme modelinin tükettiği koşullandırmaya ekler. Set Reference Latent düğümünün çok görüntülü karşılığıdır: bir VAE ile bir referans görüntü kümesi bağlarsınız; düğüm, kodlanan her latenti pozitif koşullandırmaya ve bir negatif koşullandırma bağlıysa ona da ekler. Bir model tek bir latent yerine aynı anda birkaç referans görüntü beklediğinde bunu kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Referans latentleriyle değiştirilecek pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negative` | Aynı referans latentlerini alacak isteğe bağlı negatif koşullandırma. `negative` çıktısında değiştirilmiş pozitif koşullandırmayı yeniden kullanmak için bağlantısız bırakın. | CONDITIONING | Hayır | - |
| `vae` | Bağlı referans görüntüleri kodlamak için kullanılan VAE. Hiçbir VAE bağlı değilse referans görüntüler yok sayılır. | VAE | Hayır | - |
| `resolution` | Her referans görüntünün kodlamadan önce nasıl hazırlanacağı. `"keep resolution"` görüntüyü geldiği boyutta kodlar; `"resize"` en boy oranını koruyarak hedef megapiksel sayısına ölçekler ve `megapixels` seçeneğini görünür kılar. (varsayılan: "keep resolution") | DYNAMIC_COMBO | Evet | `"keep resolution"`<br>`"resize"` |
| `images` | Genişletilebilir yuva: referans olarak kullanmak için bir veya daha fazla referans görüntü (`image_1`, `image_2`, ...) bağlayın. Görüntüler yuva sırasına göre kodlanır ve koşullandırmaya aynı sırayla eklenir. | IMAGE | Hayır | 1 ile 100 arası |

### Yeniden Boyutlandırma Girdileri

Bu seçenekler `resolution` `"resize"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `megapixels` | En boy oranını koruyarak her referans görüntünün hedef boyutu. 1.0 yaklaşık 1024 x 1024 pikseldir. (varsayılan: 1.0) | FLOAT | Evet | 0.01 ile 16.0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Kodlanan referans latentlerinin eklendiği pozitif koşullandırma. | CONDITIONING |
| `negative` | Aynı referans latentlerinin eklendiği negatif koşullandırma. Hiçbir negatif koşullandırma bağlı olmadığında pozitif çıktıyı döndürür. | CONDITIONING |
| `empty_latent` | Bir örnekleyiciyi başlatmaya hazır, 0.0 ile çarpılmış ilk referans latenti. Hiçbir referans görüntü bağlı olmadığında boştur. | LATENT |

## Notlar

- Latentler değiştirilmek yerine eklenir; bu nedenle birkaç Set Reference Multi Latent düğümünü zincirlemek referansları biriktirir.
- Bağlı her görüntü kendi başına kodlanır; bu nedenle referans görüntülerin aynı boyutta olması gerekmez.
- Hiçbir görüntü bağlı olmadığında `positive` ve `negative` değiştirilmeden döndürülür ve `empty_latent` boş olur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/tr.md)

---
**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`

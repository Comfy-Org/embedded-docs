# TextEncodeFibo2

Bir Fibo 2.0 istemini koşullandırmaya ve eşleşen boş bir latent'e kodlayın. İstem ya düz metindir ya da yapılandırılmış bir JSON açıklamasıdır; görseller bağlandığında düzenleme talimatına veya sonucun `edit_instruction` anahtarlı bir JSON açıklamasına dönüşür ve bir VAE bağlı olduğunda görseller her iki çıktı için referans latentleri olarak işlev görür. Boyutu görsellerin kırpıldığı boyut olan `latent` çıktısını örnekleyin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | İstemi tokenize etmek ve kodlamak için kullanılan Fibo 2.0 metin kodlayıcısı. | CLIP | Evet | - |
| `prompt` | Oluşturma için kullanılacak açıklama veya görseller bağlıyken düzenleme talimatı. Görsellere `<image_1>`, `<image_2>` vb. şeklinde atıfta bulunun. Beklenen sonucun bir JSON açıklaması da kullanılabilir; değişiklik, `edit_instruction` anahtarında açıklanır. | STRING | Evet | - |
| `negative_prompt` | Uzaklaşılacak açıklama; negatif koşullandırma olarak kodlanır. Boş bırakılması, Fibo 2.0'un classifier-free guidance için eğitildiği null açıklamadır (varsayılan: boş). | STRING | Evet | - |
| `vae` | Görselleri referans latentlerine kodlamak için kullanılan VAE. Olmadığında görseller yalnızca metin kodlamasını koşullandırır. | VAE | Hayır | - |
| `images` | Düzenlenecek görseller, en fazla 16 adet. Tek bir görsel, sonucun boyutuna ölçeklenir ve ortadan kırpılır; çünkü düzenleme onunla piksel piksel hizalanır; birden fazla görsel ise her biri kendi eğitildiği boyuta ölçeklenir. | IMAGE | Hayır | 0 ile 16 arası görüntü |
| `width` | Sonucun genişliği; 16'nın katına aşağı yuvarlanır. 0 değeri, ilk görselin en-boy oranı için Fibo 2.0'un eğitildiği boyutu kullanır; yaklaşık 1 megapiksel veya görsel yoksa 1024 (varsayılan: 0). | INT | Evet | 0 ile 16384 arası (adım: 16) |
| `height` | Sonucun yüksekliği; 16'nın katına aşağı yuvarlanır. 0 değeri, ilk görselin en-boy oranı için Fibo 2.0'un eğitildiği boyutu kullanır; yaklaşık 1 megapiksel veya görsel yoksa 1024 (varsayılan: 0). | INT | Evet | 0 ile 16384 arası (adım: 16) |
| `batch_size` | Partide oluşturulacak latent sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 arası |

Referans latentleri her iki çıktıya da eklenir; böylece görseller yalnızca pozitif dalla değil, koşullandırmayla birlikte taşınır. VAE bağlı değilken görseller yalnızca metin kodlayıcısı tarafından görülür ve hiçbir referans latentı eklenmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İstemin koşullandırması; bir VAE ve görseller bağlıyken referans latentleriyle birlikte. | CONDITIONING |
| `negative` | `negative_prompt` değerinin koşullandırması; yalnızca metin, aynı referans latentleriyle. | CONDITIONING |
| `latent` | İstenen boyutta, örneklemeye hazır boş latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/tr.md)

---
**Source fingerprint (SHA-256):** `f400d041a3dd224e30c0fa2acc803e3de11d6c10654bde122e8d569fa1cd1d79`

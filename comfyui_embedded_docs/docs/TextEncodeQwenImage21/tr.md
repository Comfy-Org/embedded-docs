# TextEncodeQwenImage21

TextEncodeQwenImage21 düğümü, Qwen-Image 2.1 modeli için bir prompt ve negatif prompt kodlar; isteğe bağlı olarak referans görselleri ekler. Referans görseller metin kodlayıcı tarafından görülür ve bir VAE bağlandığında, diziye eklenen latentler olarak da kodlanır; böylece koşullandırma hem metin talimatını hem de görsel referansı taşır. Düğüm, örneklemeye hazır, ilk referans görsele göre boyutlandırılmış boş bir latent ile birlikte pozitif ve negatif koşullandırma döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Prompt'ları tokenleştirmek ve kodlamak için kullanılan Qwen-Image 2.1 metin kodlayıcı. | CLIP | Evet | - |
| `prompt` | Oluşturulacak görseli veya uygulanacak düzenlemeyi tanımlayan metin prompt'u. Çok satırlı girdiyi ve dinamik prompt'ları destekler. | STRING | Evet | Herhangi bir metin |
| `negative_prompt` | Sonucun kaçınması gereken şeyi tanımlayan metin prompt'u. Çok satırlı girdiyi ve dinamik prompt'ları destekler. | STRING | Evet | Herhangi bir metin |
| `vae` | Referans görselleri referans latentlere kodlamak için kullanılan VAE. Atlanırsa, referans görseller sonucu yalnızca metin kodlayıcı aracılığıyla koşullandırır. | VAE | Hayır | - |
| `resolution` | Referans görseller, en-boy oranı korunarak yaklaşık `resolution` x `resolution` piksele, 32'nin katlarına göre yeniden boyutlandırılır. 0, her referansı kendi boyutunda tutar ve 32'nin katına yuvarlar (varsayılan: 1024). | INT | Evet | 0 - 4096 (adım 32) |
| `images` | Metin kodlayıcı tarafından görülen ve VAE latentleri olarak diziye eklenen referans görseller. Genişletilebilir yuva: en fazla 16 görsel bağlayın (`image_1` ... `image_16`). | IMAGE | Hayır | 0 - 16 görsel |

Boş latent çıktısı, bağlanan ilk referans görselin boyutuna ya da hiç referans görsel bağlı değilse `resolution` değerine göre boyutlandırılır. Bu düğümün döndürdüğü latentte örnekleme yapın: başka herhangi bir boyut düzenlemenin kaymasına neden olur. Bir VAE bağlandığında, aynı referans latentler hem pozitif hem de negatif koşullandırmaya eklenir; böylece tek bir örnekleyici adımı her ikisini de gürültüden arındırabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Prompt için kodlanmış koşullandırma; bir VAE bağlandığında referans latentleri taşır. | CONDITIONING |
| `negative` | Negatif prompt için kodlanmış koşullandırma; aynı referans latentleri içerir. | CONDITIONING |
| `latent` | İlk referans görselin boyutunda boş latent veya hiç referans görsel bağlı değilse 1024 x 1024. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/tr.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`

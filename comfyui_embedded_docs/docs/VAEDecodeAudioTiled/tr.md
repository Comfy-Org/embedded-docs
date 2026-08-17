# VAE Sesini Çöz (Döşemeli)

Bu düğüm, sıkıştırılmış bir ses temsilini (latent örnekler) bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak tekrar bir ses dalga formuna dönüştürür. Verileri bellek kullanımını yönetmek için daha küçük, örtüşen bölümler (döşemeler) halinde işler; bu da onu daha uzun ses dizilerini işlemek için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Kod çözülecek sesin sıkıştırılmış latent temsili. | LATENT | Evet | N/A |
| `vae` | Kod çözme işlemini gerçekleştirmek için kullanılan Varyasyonel Otomatik Kodlayıcı modeli. | VAE | Evet | N/A |
| `tile_size` | Her bir işleme döşemesinin boyutu. Ses, belleği korumak için bu uzunluktaki bölümler halinde kod çözülür (varsayılan: 512). | INT | Evet | 32 ila 8192 |
| `overlap` | Bitişik döşemelerin örtüştüğü örnek sayısı. Bu, döşemeler arasındaki sınırlarda oluşan yapaylıkların azaltılmasına yardımcı olur (varsayılan: 64). | INT | Evet | 0 ila 1024 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kod çözülmüş ses dalga formu. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/tr.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`

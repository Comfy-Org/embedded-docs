# VAE Sesini Çöz (Döşemeli)

Bu düğüm, sıkıştırılmış bir ses temsilini (latent örnekler) bir Değişken Otomatik Kodlayıcı (VAE) kullanarak tekrar ses dalga formuna dönüştürür. Verileri, bellek kullanımını yönetmek için daha küçük, örtüşen bölümler (tile'lar) halinde işler; bu da onu daha uzun ses dizilerini işlemek için uygun hale getirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Kod çözülecek sesin sıkıştırılmış latent temsili. | LATENT | Evet | Yok |
| `vae` | Kod çözme işlemini gerçekleştirmek için kullanılan Değişken Otomatik Kodlayıcı modeli. | VAE | Evet | Yok |
| `döşeme boyutu` | Her bir işleme tile'ının boyutu. Ses, belleği korumak için bu uzunluktaki bölümler halinde kod çözülür (varsayılan: 512). | INT | Evet | 32 ila 8192 |
| `örtüşme` | Bitişik tile'ların örtüştüğü örnek sayısı. Bu, tile'lar arasındaki sınırlardaki yapaylıkları azaltmaya yardımcı olur (varsayılan: 64). | INT | Evet | 0 ila 1024 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kod çözülmüş ses dalga formu. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/tr.md)

---
**Source fingerprint (SHA-256):** `d989f0cd0e4b4bf992d6860e27c25b8e814df52763c82909a61c58f418306352`

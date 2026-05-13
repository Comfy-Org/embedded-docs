> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/tr.md)

Bu düğüm, sıkıştırılmış bir ses temsilini (latent örnekler) bir Değişken Otomatik Kodlayıcı (VAE) kullanarak tekrar ses dalga formuna dönüştürür. Verileri, bellek kullanımını yönetmek için daha küçük, örtüşen bölümler (tile'lar) halinde işler; bu da onu daha uzun ses dizilerini işlemek için uygun hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | Yok | Kod çözülecek sesin sıkıştırılmış latent temsili. |
| `vae` | VAE | Evet | Yok | Kod çözme işlemini gerçekleştirmek için kullanılan Değişken Otomatik Kodlayıcı modeli. |
| `döşeme boyutu` | INT | Evet | 32 ila 8192 | Her bir işleme tile'ının boyutu. Ses, belleği korumak için bu uzunluktaki bölümler halinde kod çözülür (varsayılan: 512). |
| `örtüşme` | INT | Evet | 0 ila 1024 | Bitişik tile'ların örtüştüğü örnek sayısı. Bu, tile'lar arasındaki sınırlardaki yapaylıkları azaltmaya yardımcı olur (varsayılan: 64). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | AUDIO | Kod çözülmüş ses dalga formu. |

---
**Source fingerprint (SHA-256):** `d989f0cd0e4b4bf992d6860e27c25b8e814df52763c82909a61c58f418306352`

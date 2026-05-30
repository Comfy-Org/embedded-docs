> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/tr.md)

## Genel Bakış

Bu düğüm, VAE modelinin hangi GPU cihazına yerleştirileceğini manuel olarak seçmenizi sağlar. Varsayılan olarak VAE, model yükleyici tarafından atanan cihaza yerleştirilir, ancak belirli bir GPU'ya (örneğin, `gpu:0`, `gpu:1`) sabitleyebilirsiniz. Seçilen cihaz makinenizde mevcut değilse, düğüm VAE'yi değiştirmeden geçirir ve hata vermek yerine bir mesaj günlüğe kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `vae` | VAE | Evet | | Belirli bir cihaza atanacak VAE modeli. |
| `cihaz` | COMBO | Evet | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` | VAE için hedef cihaz. `"default"`, yükleyici tarafından atanan cihazı geri yükler. `"gpu:N"`, VAE'yi N. kullanılabilir GPU'ya sabitler. CPU desteklenen bir seçenek değildir ve sağlanırsa yok sayılır. (varsayılan: `"default"`) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `vae` | VAE | Artık seçilen cihaza atanmış olan VAE modeli. İstenen cihaz kullanılamıyor veya geçersizse, VAE değiştirilmeden geçirilir. |

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`

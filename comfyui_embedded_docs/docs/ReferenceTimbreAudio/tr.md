> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/tr.md)

Bu düğüm, "ace step 1.5" sürecinde kullanılmak üzere bir referans ses tınısı ayarlar. Bir koşullandırma girdisi ve isteğe bağlı olarak bir ses örtük temsili alarak, bu örtük veriyi iş akışındaki sonraki düğümler tarafından kullanılmak üzere koşullandırmaya ekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | | Referans ses bilgisinin ekleneceği koşullandırma verisi. |
| `latent` | LATENT | Hayır | | Referans sesin isteğe bağlı örtük temsili. Sağlandığında, örnekleri koşullandırmaya eklenir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | İsteğe bağlı `latent` girdisi sağlanmışsa, artık referans ses tınısı örtüklerini içeren değiştirilmiş koşullandırma verisi. |

---
**Source fingerprint (SHA-256):** `2d39399eb79cfe76b72d01326b89863e2553bc23414b1166d310e5222b215b29`

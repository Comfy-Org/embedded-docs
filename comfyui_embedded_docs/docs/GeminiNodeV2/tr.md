# Google Gemini

Google'ın Gemini modelleriyle metin yanıtları oluşturun. Bir metin istemi ve isteğe bağlı olarak çok modlu bağlam olarak bir veya daha fazla resim, ses klibi, video veya dosya sağlayın.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Modele metin girişi. Ayrıntılı talimatlar, sorular veya bağlam ekleyin. | STRING | Evet |  |
| `model` | Yanıtı oluşturmak için kullanılan Gemini modeli. | COMBO | Evet | `"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `seed` | Örnekleme için tohum değeri. Rastgele tohum için 0 olarak ayarlayın. Deterministik çıktı garanti edilmez. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır |  |

**Not:** Çok modlu bağlam olarak resim, ses veya video sağlarken, düğüm ilk 10 giriş için medyayı URL olarak yükler. Ek medyalar, maksimum 18 MB satır içi yük boyutuyla base64 verisi olarak satır içi gönderilir. Satır içi yük bu sınırı aşarsa bir hata oluşur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `output` | Gemini modelinden oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `ec9921f218a726082eb8987cf94b3575f61a3c6cf55fb33aeb81d42fad35d302`

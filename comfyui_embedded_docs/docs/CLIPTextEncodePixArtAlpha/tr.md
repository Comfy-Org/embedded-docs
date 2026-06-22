# CLIPMetinKodlamaPixArtAlpha

Metni PixArt Alpha için kodlar ve çözünürlük koşullandırmasını ayarlar. Bu düğüm, metin girişini işler ve PixArt Alpha modelleri için özel olarak koşullandırma verileri oluşturmak üzere genişlik ve yükseklik bilgilerini ekler. PixArt Sigma modelleri için geçerli değildir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Çözünürlük koşullandırması için genişlik boyutu (varsayılan: 1024) | INT | Evet | 0 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `yükseklik` | Çözünürlük koşullandırması için yükseklik boyutu (varsayılan: 1024) | INT | Evet | 0 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `metin` | Kodlanacak metin girişi, çok satırlı girişi ve dinamik istemleri destekler | STRING | Evet | - |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Metin tokenleri ve çözünürlük bilgileriyle kodlanmış koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/tr.md)

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`

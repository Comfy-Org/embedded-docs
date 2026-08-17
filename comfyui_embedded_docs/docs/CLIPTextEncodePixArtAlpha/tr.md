# CLIPMetinKodlamaPixArtAlpha

PixArt Alpha için metni kodlar ve çözünürlük koşullandırmasını ayarlar. Bu düğüm, metin girişini işler ve PixArt Alpha modellerine özel koşullandırma verileri oluşturmak için genişlik ve yükseklik bilgisi ekler. PixArt Sigma modelleri için geçerli değildir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Çözünürlük koşullandırması için genişlik boyutu (varsayılan: 1024) | INT | Evet | 0 to MAX_RESOLUTION |
| `height` | Çözünürlük koşullandırması için yükseklik boyutu (varsayılan: 1024) | INT | Evet | 0 to MAX_RESOLUTION |
| `text` | Kodlanacak metin girişi; çok satırlı girişi ve dinamik istemleri destekler | STRING | Evet | - |
| `clip` | Belirteçleştirme ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Metin belirteçleri ve çözünürlük bilgisi içeren kodlanmış koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/tr.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`

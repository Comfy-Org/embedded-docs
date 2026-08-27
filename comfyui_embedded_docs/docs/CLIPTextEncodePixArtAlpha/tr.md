# CLIPMetinKodlamaPixArtAlpha

PixArt Alpha için metni kodlar ve çözünürlük koşullandırmasını ayarlar. Bu düğüm, metin girdisini işler ve PixArt Alpha modellerine özel koşullandırma verisi oluşturmak için genişlik ve yükseklik bilgisi ekler. PixArt Sigma modelleri için geçerli değildir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `genişlik` | Çözünürlük koşullandırması için genişlik boyutu (varsayılan: 1024) | INT | Evet | 0 ile MAX_RESOLUTION |
| `yükseklik` | Çözünürlük koşullandırması için yükseklik boyutu (varsayılan: 1024) | INT | Evet | 0 ile MAX_RESOLUTION |
| `metin` | Kodlanacak metin girdisi. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | - |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Metin tokenleri ve çözünürlük bilgisiyle kodlanmış koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/tr.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`

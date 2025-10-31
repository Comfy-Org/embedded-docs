> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/tr.md)

Metni kodlar ve PixArt Alpha için çözünürlük koşullandırmasını ayarlar. Bu düğüm, metin girişini işler ve PixArt Alpha modelleri için özel olarak koşullandırma verisi oluşturmak üzere genişlik ve yükseklik bilgisi ekler. PixArt Sigma modelleri için geçerli değildir.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `genişlik` | INT | Giriş | 1024 | 0 - MAX_RESOLUTION | Çözünürlük koşullandırması için genişlik boyutu |
| `yükseklik` | INT | Giriş | 1024 | 0 - MAX_RESOLUTION | Çözünürlük koşullandırması için yükseklik boyutu |
| `metin` | STRING | Giriş | - | - | Kodlanacak metin girişi, çok satırlı giriş ve dinamik istemleri destekler |
| `clip` | CLIP | Giriş | - | - | Tokenleştirme ve kodlama için kullanılan CLIP modeli |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Metin token'ları ve çözünürlük bilgisi içeren kodlanmış koşullandırma verisi |
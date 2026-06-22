# MetinKodlamaHunyuanVideo_GörüntüdenVideoya

**Genel Bakış**

TextEncodeHunyuanVideo_ImageToVideo düğümü, metin istemlerini görsel yerleştirmelerle birleştirerek video oluşturma için koşullandırma verileri oluşturur. Hem metin girişini hem de bir CLIP görüş çıktısından gelen görsel bilgileri işlemek için bir CLIP modeli kullanır ve ardından belirtilen görsel enterpolasyon ayarına göre bu iki kaynağı harmanlayan tokenler oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenleştirme ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_görü_çıktısı` | Görsel bağlam sağlayan bir CLIP görüş modelinden gelen görsel yerleştirmeler | CLIP_VISION_OUTPUT | Evet | - |
| `istem` | Video oluşturmayı yönlendiren metin açıklaması; çok satırlı giriş ve dinamik istemleri destekler | STRING | Evet | - |
| `görüntü_serpiştirme` | Görselin metin istemine kıyasla sonuçları ne kadar etkilediği. Daha yüksek değer, metin isteminin daha fazla etkisi olduğu anlamına gelir. (varsayılan: 2) | INT | Evet | 1-512 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Video oluşturma için metin ve görsel bilgilerini birleştiren koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`

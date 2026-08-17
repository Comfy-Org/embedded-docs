# MetinKodlamaHunyuanVideo_GörüntüdenVideoya

The TextEncodeHunyuanVideo_ImageToVideo düğümü, metin istemlerini görüntü yerleştirmeleriyle birleştirerek video oluşturma için koşullandırma verileri oluşturur. Hem metin girişini hem de CLIP görüş çıktısındaki görsel bilgiyi işlemek için bir CLIP modeli kullanır ve ardından belirtilen görüntü aralık ayarına göre bu iki kaynağı harmanlayan tokenlar üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `clip_vision_output` | Görüntü bağlamı sağlayan CLIP görüş modelinden görsel yerleştirmeler | CLIP_VISION_OUTPUT | Evet | - |
| `prompt` | Video oluşturmayı yönlendiren metin açıklaması. Çok satırlı girişi ve dinamik istemleri destekler. İstem, modele referans görüntüye dayalı videoyu tanımlamasını isteyen bir şablon kullanılarak biçimlendirilir; ana içerik, nesne ayrıntıları, eylemler, arka plan ve kamera açıları gibi yönleri kapsar. | STRING | Evet | - |
| `image_interleave` | Görüntünün, metin istemine kıyasla şeyleri ne kadar etkilediği. Daha yüksek sayı, metin isteminden daha fazla etki anlamına gelir. (varsayılan: 2, gelişmiş parametre) | INT | Evet | 1-512 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Video oluşturma için metin ve görüntü bilgilerini birleştiren koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/tr.md)

TextEncodeHunyuanVideo_ImageToVideo düğümü, metin istemlerini görsel yerleştirmelerle birleştirerek video üretimi için koşullandırma verileri oluşturur. Metin girişini ve bir CLIP görüntü çıktısından gelen görsel bilgileri işlemek için bir CLIP modeli kullanır, ardından belirtilen görüntü araya ekleme ayarına göre bu iki kaynağı harmanlayan token'lar üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Token oluşturma ve kodlama için kullanılan CLIP modeli |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Evet | - | Görsel bağlam sağlayan bir CLIP görüntü modelinden gelen görsel yerleştirmeler |
| `prompt` | STRING | Evet | - | Video üretimine rehberlik edecek metin açıklaması, çok satırlı girişi ve dinamik istemleri destekler |
| `image_interleave` | INT | Evet | 1-512 | Görüntünün, metin istemine kıyasla ne kadar etkili olacağını belirler. Daha yüksek sayı, metin isteminden daha fazla etki anlamına gelir. (varsayılan: 2) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Video üretimi için metin ve görüntü bilgisini birleştiren koşullandırma verileri |
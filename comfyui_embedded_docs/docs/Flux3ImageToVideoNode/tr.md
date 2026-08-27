# Flux 3 Görselden Videoya

Flux 3 Image to Video, FLUX 3 ile 1 ila 10 görüntüyü canlandırır. Her görüntü klibin bir karesi olur: tek görüntü klibi açar, iki görüntü birinciden ikinciye dönüşür, daha fazlası klibe yayılır veya seçtiğiniz sürelere sabitlenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Sahnenin nasıl hareket etmesi ve ses çıkarması gerektiği; prompt, üretimden önce yorumlanır ve genişletilir. En az bir karakter içermelidir. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |
| `keyframes` | Oynatma sırasına göre 1 ila 10 görüntü. Her biri en az 256x256 piksel. Büyütülebilir girdi: görüntüleri `image_1`, `image_2` vb. şeklinde bağlayın. | IMAGE | Evet | 1 ila 10 görüntü |
| `placement` | "spread across the clip" seçeneği FLUX 3'ün görüntüleri yerleştirmesini sağlar (tek görüntü klibi açar, iki görüntü klibin başlangıcı ve sonu olur); "at times" ise her görüntüyü seçtiğiniz bir saniyeye sabitler. | DYNAMIC_COMBO | Evet | `"spread across the clip"` (varsayılan)<br>`"at times"` |
| `times` | Görüntü başına saniye cinsinden bir süre; virgülle ayrılmış ve artan şekilde, örn. "0, 2.5, 5". Yalnızca `placement` "at times" olduğunda görünür; her ana kare görüntüsü için bir süre gereklidir. | STRING | Hayır | Saniye cinsinden virgülle ayrılmış (varsayılan: "0") |
| `aspect_ratio` | Çıktı en boy oranı. "auto" seçeneği, prompt'tan ve girdilerden birini seçer. | COMBO | Evet | `"auto"` (varsayılan)<br>diğer mevcut en boy oranları |
| `duration` | Klibin saniye cinsinden süresi. "auto" süreyi içeriğe göre ayarlar. | COMBO | Evet | `"auto"` (varsayılan)<br>diğer mevcut süreler |
| `resolution` | Çıktı çözünürlüğü. | COMBO | Evet | `"720p"` (varsayılan)<br>`"1080p"` |
| `generate_audio` | Senkronize ses üret (ortam sesi, konuşma, efektler). Kapalı, ses parçası olmayan bir video üretir. | BOOLEAN | Evet | true / false (varsayılan: true) |
| `safety_tolerance` | Moderasyon toleransı; 0 en katıdır. Görüntü veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlandırılır. | INT | Evet | 0 ila 4 (varsayılan: 2, gelişmiş ayar) |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değer ne olursa olsun gerçek sonuçlar deterministik değildir. | INT | Evet | 0 ila 4294967295 (varsayılan: 42, control-after-generate) |

Not: `keyframes` en az bir görüntü içermelidir; hiçbiri bağlanmazsa düğüm bir hata verir. Her ana kare görüntüsü en az 256x256 piksel olmalı ve en boy oranı 64:1'den daha uç olamaz.

`placement` "spread across the clip" olduğunda ve 3 veya daha fazla ana kare bağlandığında, `duration` "auto" değil, açık bir değere ayarlanmalıdır; aksi takdirde düğüm bir hata verir.

`placement` "at times" olduğunda, `times` görüntü başına saniye cinsinden bir süre sağlamalıdır. Süreler artan olmalı, negatif olamaz ve son süre klibin sonunu geçemez (`duration` "auto" olduğunda en fazla 20 saniye).

Bu düğüm görüntü gönderdiği için, `safety_tolerance` sizin ayarladığınız değer ne olursa olsun 2 ile sınırlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Ana kare görüntülerinden, seçilen en boy oranı, süre, çözünürlük ve ses ayarıyla oluşturulan video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`

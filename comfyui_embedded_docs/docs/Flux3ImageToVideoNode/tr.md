# Flux 3 Görselden Videoya

Flux 3 Image to Video, FLUX 3 ile 1 ila 10 görüntüyü canlandırır. Her görüntü klibin bir karesi olur: bir görüntü klibi açar, iki görüntü birinciden ikinciye dönüşür, daha fazlası ise klip boyunca yayılır veya seçtiğiniz zamanlara sabitlenir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `placement` | "spread across the clip" FLUX 3'ün görüntüleri yerleştirmesini sağlar (biri klibi açar, ikisi başlangıcı ve sonu olur); "at times" her görüntüyü seçtiğiniz bir saniyeye sabitler. | DYNAMIC_COMBO | Evet | `"spread across the clip"` (varsayılan)<br>`"at times"` |
| `prompt` | Sahnenin nasıl hareket edeceği ve nasıl ses çıkaracağı; istem üretimden önce yorumlanır ve genişletilir. En az bir karakter içermelidir. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |
| `aspect_ratio` | Çıktı en-boy oranı. "auto" istemden ve girdilerden birini seçer. | COMBO | Evet | `"auto"` (varsayılan)<br>diğer kullanılabilir en-boy oranları |
| `duration` | Saniye cinsinden klip uzunluğu. "auto" uzunluğu içeriğe uydurur. | COMBO | Evet | `"auto"` (varsayılan)<br>diğer kullanılabilir süreler |
| `resolution` | Çıktı çözünürlüğü. | COMBO | Evet | `"720p"` (varsayılan)<br>`"1080p"` |
| `generate_audio` | Senkronize ses üretir (ortam, konuşma, efektler). Kapalı olduğunda ses parçası olmayan bir video üretir. | BOOLEAN | Evet | true / false (varsayılan: true) |
| `safety_tolerance` | Moderasyon toleransı; 0 en katıdır. Görüntü veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlandırılır. | INT | Evet | 0 ila 4 (varsayılan: 2, gelişmiş ayar) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. | INT | Evet | 0 ila 4294967295 (varsayılan: 42, üretim sonrası kontrol) |

### spread across the clip Girdileri

Bu yerleştirme seçeneğinin ek parametresi yoktur.

### at times Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `times` | Görüntü başına saniye cinsinden bir zaman; virgülle ayrılmış ve artan sırada olmalıdır, örn. "0, 2.5, 5". Yalnızca `placement` "at times" olduğunda görünür; her ana kare görüntüsü için bir zaman gereklidir. | STRING | Hayır | Virgülle ayrılmış saniyeler (varsayılan: "0") |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `keyframes` | Büyütülebilir yuva: 1 ila 10 ana kare görüntüsünü oynatma sırasına göre bağlayın, örn. `image_1`, `image_2` vb. Her görüntü klibin bir karesi olur. Her biri en az 256x256 piksel olmalıdır; en-boy oranı 64:1'den daha uç olamaz. | IMAGE | Evet | 1 ila 10 görüntü |

Not: `keyframes` en az bir görüntü içermelidir; hiçbiri bağlı değilse düğüm bir hata verir. Her ana kare görüntüsü en az 256x256 piksel olmalıdır ve en-boy oranı 64:1'den daha uç olamaz.

`placement` "spread across the clip" olduğunda ve 3 veya daha fazla ana kare bağlandığında, `duration` "auto" değil, açık bir değere ayarlanmalıdır; aksi halde düğüm bir hata verir.

`placement` "at times" olduğunda, `times` görüntü başına saniye cinsinden bir zaman sağlamalıdır. Zamanlar artan sırada olmalı, negatif olamaz ve son zaman klibin sonunu aşamaz (`duration` "auto" olduğunda en fazla 20 saniye).

Bu düğüm görüntü gönderdiği için, `safety_tolerance` ayarladığınız değerden bağımsız olarak 2 ile sınırlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen en-boy oranı, süre, çözünürlük ve ses ayarıyla ana kare görüntülerinden oluşturulan üretilmiş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`

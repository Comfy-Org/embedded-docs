# Flux3ImageToVideoNode

Flux 3 Image to Video, FLUX 3 ile 1 ila 10 görüntüyü canlandırır. Her görüntü klibin bir karesi olur: tek görüntü klibi açar, iki görüntü birinciden ikinciye dönüşür, daha fazlası klibe yayılır veya seçtiğiniz zamanlara sabitlenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Sahnenin nasıl hareket edeceğini ve ses çıkaracağını belirtir; istem, üretimden önce yorumlanır ve genişletilir. En az bir karakter içermelidir. | STRING | Evet | Çok satırlı metin (varsayılan: boş) |
| `keyframes` | Oynatma sırasına göre 1 ila 10 görüntü. Her biri minimum 256x256 piksel. Her ana kare, klipte bir nokta haline gelir. | IMAGE | Evet | 1 ila 10 görüntü |
| `placement` | 'spread across the clip' seçeneği FLUX 3'ün görüntüleri yerleştirmesine izin verir (biri klibi açar, ikisi başlangıç ve bitiş olur); 'at times' seçeneği her görüntüyü seçtiğiniz bir saniyeye sabitler. | STRING | Evet | `"spread across the clip"` (varsayılan)<br>`"at times"` |
| `times` | Görüntü başına saniye cinsinden bir zaman, virgülle ayrılmış ve artan şekilde, örn. '0, 2.5, 5'. `placement` `"at times"` olduğunda gereklidir. | STRING | Hayır | Virgülle ayrılmış saniyeler (varsayılan: "0") |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto' seçeneği, istem ve girdilerden birini seçer. | STRING | Evet | `"auto"` (varsayılan)<br>diğer mevcut seçenekler |
| `duration` | Klibin saniye cinsinden uzunluğu. 'auto' uzunluğu içeriğe göre ayarlar. | STRING | Evet | `"auto"` (varsayılan)<br>diğer mevcut seçenekler |
| `resolution` | Çıktı çözünürlüğü. | STRING | Evet | `"720p"` (varsayılan)<br>`"1080p"` |
| `generate_audio` | Senkronize ses üret (ortam sesi, konuşma, efektler). Kapalı, ses parçası olmayan bir video üretir. | BOOLEAN | Evet | true / false (varsayılan: true) |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. Görüntü veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlıdır. | INT | Evet | 0 ila 4 (varsayılan: 2, gelişmiş ayar) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değer ne olursa olsun gerçek sonuçlar deterministik değildir. | INT | Evet | 0 ila 4294967295 (varsayılan: 42, üretim sonrası kontrol ile) |

Not: `keyframes` gereklidir — hiçbir ana kare görüntüsü bağlanmazsa düğüm bir hata verir. `placement` `"spread across the clip"` olduğunda ve 3 veya daha fazla görüntü sağlandığında, `duration` açık bir değere ayarlanmalıdır (`"auto"` değil); aksi takdirde düğüm hata verir. `placement` `"at times"` olduğunda, `times` görüntü başına saniye cinsinden artan sırada bir zaman sağlamalıdır. Görüntü gönderen istekler, ayarlanan değer ne olursa olsun güvenlik toleransı 2 ile sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen en-boy oranı, süre, çözünürlük ve ses ayarıyla ana kare görüntülerinden oluşturulan video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `3b9472194020ec98cd4e8c60463cdd0e9dc074ec6cbc1fc03d313894fa570ba8`

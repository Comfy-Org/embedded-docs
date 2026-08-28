# Magnific Görüntü Büyütme (Hassas V2)

Magnific Image Upscale (Precise V2) düğümü, keskinlik, gren ve detay iyileştirme üzerinde ince ayar kontrolü sağlayarak yüksek doğruluklu görüntü büyütme gerçekleştirir. Görüntüleri harici bir API üzerinden işler ve maksimum 10060×10060 piksel çıktı çözünürlüğünü destekler. Düğüm farklı işleme stilleri sunar ve istenen çıktı maksimum izin verilen boyutu aşarsa girdiyi otomatik olarak küçültebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Büyütülecek girdi görüntüsü. Tam olarak bir görüntü gereklidir. Minimum boyutlar 160x160 pikseldir. En-boy oranı 1:3 ile 3:1 arasında olmalıdır. | IMAGE | Evet | - |
| `ölçek_faktörü` | İstenen büyütme çarpanı. | COMBO | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `stil` | İşleme stili: genel kullanım için sublime, fotoğraflar için photo, gürültülü fotoğraflar için photo_denoiser. | COMBO | Evet | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `keskinleştirme` | Görüntü keskinlik yoğunluğu. Daha yüksek değerler kenar tanımını ve netliği artırır. Varsayılan: 7. | INT | Hayır | 0 ila 100 |
| `akıllı_gren` | Görüntünün çok pürüzsüz veya yapay görünmesini önlemek için akıllı gren/doku iyileştirmesi. Varsayılan: 7. | INT | Hayır | 0 ila 100 |
| `ultra_detay` | Büyütme sırasında eklenen ince detayları, dokuları ve mikro detayları kontrol eder. Varsayılan: 30. | INT | Hayır | 0 ila 100 |
| `otomatik_küçültme` | Çıktı maksimum çözünürlüğü aşarsa girdi görüntüsünü otomatik olarak küçültür. Varsayılan: False. | BOOLEAN | Hayır | - |

**Not:** `auto_downscale` devre dışıysa ve istenen çıktı boyutu (girdi boyutları × `scale_factor`) 10060x10060 pikseli aşarsa, düğüm bir hata verir. `auto_downscale` etkinleştirildiğinde, düğüm kalite kaybını minimumda tutan en uygun ölçek faktörünü bulmaya çalışır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Elde edilen büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/tr.md)

---
**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`

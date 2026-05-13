> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/tr.md)

Magnific Image Upscale (Precise V2) düğümü, keskinlik, gren ve detay iyileştirme üzerinde hassas kontrol sağlayarak yüksek doğrulukta görüntü büyütme işlemi gerçekleştirir. Görüntüleri harici bir API aracılığıyla işler ve maksimum 10060×10060 piksel çıktı çözünürlüğünü destekler. Düğüm, farklı işleme stilleri sunar ve istenen çıktı izin verilen maksimum boyutu aşarsa girdiyi otomatik olarak küçültebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Büyütülecek girdi görüntüsü. Tam olarak bir görüntü gereklidir. Minimum boyutlar 160x160 pikseldir. En-boy oranı 1:3 ile 3:1 arasında olmalıdır. |
| `scale_factor` | STRING | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` | İstenen büyütme çarpanı. |
| `flavor` | STRING | Evet | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` | İşleme stili. "sublime" genel kullanım içindir, "photo" fotoğraflar için optimize edilmiştir ve "photo_denoiser" gürültülü fotoğraflar içindir. |
| `sharpen` | INT | Hayır | 0 ile 100 | Kenar tanımını ve netliğini artırmak için görüntü keskinleştirmenin yoğunluğunu kontrol eder. Daha yüksek değerler daha keskin bir sonuç üretir. Varsayılan: 7. |
| `smart_grain` | INT | Hayır | 0 ile 100 | Büyütülmüş görüntünün çok pürüzsüz veya yapay görünmesini önlemek için akıllı gren veya doku iyileştirmesi ekler. Varsayılan: 7. |
| `ultra_detail` | INT | Hayır | 0 ile 100 | Büyütme işlemi sırasında eklenen ince detay, doku ve mikro detay miktarını kontrol eder. Varsayılan: 30. |
| `auto_downscale` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, hesaplanan çıktı boyutları izin verilen maksimum 10060x10060 piksel çözünürlüğünü aşarsa düğüm girdi görüntüsünü otomatik olarak küçültür. Bu, hataları önlemeye yardımcı olur ancak kaliteyi etkileyebilir. Varsayılan: False. |

**Not:** `auto_downscale` devre dışı bırakılırsa ve istenen çıktı boyutu (girdi boyutları × `scale_factor`) 10060x10060 pikseli aşarsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Elde edilen büyütülmüş görüntü. |

---
**Source fingerprint (SHA-256):** `cceff30e9702c6a24ab8102698c59f1afb20ec50e7f279b3c0d50befc9673b24`

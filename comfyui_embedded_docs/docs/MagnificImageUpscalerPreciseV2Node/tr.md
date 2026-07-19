# Magnific Görüntü Büyütme (Hassas V2)

Magnific Image Upscale (Precise V2) düğümü, keskinlik, gren ve detay iyileştirme üzerinde hassas kontrol sağlayarak yüksek doğrulukta görüntü büyütme işlemi gerçekleştirir. Görüntüleri harici bir API aracılığıyla işler ve maksimum 10060×10060 piksel çıktı çözünürlüğünü destekler. Düğüm, farklı işleme stilleri sunar ve istenen çıktı izin verilen maksimum boyutu aşarsa girdiyi otomatik olarak küçültebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Büyütülecek girdi görüntüsü. Tam olarak bir görüntü gereklidir. Minimum boyutlar 160x160 pikseldir. En-boy oranı 1:3 ile 3:1 arasında olmalıdır. | IMAGE | Evet | - |
| `ölçek_faktörü` | İstenen büyütme çarpanı. | STRING | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `stil` | İşleme stili. "sublime" genel kullanım içindir, "photo" fotoğraflar için optimize edilmiştir ve "photo_denoiser" gürültülü fotoğraflar içindir. | STRING | Evet | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `keskinleştirme` | Kenar tanımını ve netliğini artırmak için görüntü keskinleştirmenin yoğunluğunu kontrol eder. Daha yüksek değerler daha keskin bir sonuç üretir. Varsayılan: 7. | INT | Hayır | 0 ile 100 |
| `akıllı_gren` | Büyütülmüş görüntünün çok pürüzsüz veya yapay görünmesini önlemek için akıllı gren veya doku iyileştirmesi ekler. Varsayılan: 7. | INT | Hayır | 0 ile 100 |
| `ultra_detay` | Büyütme işlemi sırasında eklenen ince detay, doku ve mikro detay miktarını kontrol eder. Varsayılan: 30. | INT | Hayır | 0 ile 100 |
| `otomatik_küçültme` | Etkinleştirildiğinde, hesaplanan çıktı boyutları izin verilen maksimum 10060x10060 piksel çözünürlüğünü aşarsa düğüm girdi görüntüsünü otomatik olarak küçültür. Bu, hataları önlemeye yardımcı olur ancak kaliteyi etkileyebilir. Varsayılan: False. | BOOLEAN | Hayır | - |

**Not:** `auto_downscale` devre dışı bırakılırsa ve istenen çıktı boyutu (girdi boyutları × `scale_factor`) 10060x10060 pikseli aşarsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Elde edilen büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/tr.md)

---
**Source fingerprint (SHA-256):** `cceff30e9702c6a24ab8102698c59f1afb20ec50e7f279b3c0d50befc9673b24`

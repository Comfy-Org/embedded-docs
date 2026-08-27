# Flux2Scheduler

Flux2Scheduler, denoising işlemi için Flux modeline özel olarak uyarlanmış bir dizi gürültü seviyesi (sigma) üretir. Zamanlamayı, denoising adım sayısına ve hedef görüntünün boyutlarına göre hesaplar; bu da görüntü üretimi sırasında gürültü giderme ilerleyişini etkiler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `adım` | Gerçekleştirilecek denoising adım sayısı. Daha yüksek bir değer genellikle daha detaylı sonuçlara yol açar ancak işlemin daha uzun sürmesine neden olur (varsayılan: 20). | INT | Evet | 1 ile 4096 |
| `genişlik` | Oluşturulacak görüntünün piksel cinsinden genişliği. Bu değer gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 ile 16384 |
| `yükseklik` | Oluşturulacak görüntünün piksel cinsinden yüksekliği. Bu değer gürültü zamanlaması hesaplamasını etkiler (varsayılan: 1024). | INT | Evet | 16 ile 16384 |

Not: Zamanlama, `width` ve `height` değerlerinden `(width * height) / 256` olarak türetilen görüntü dizisi uzunluğundan hesaplanır; bu da modelin 16x latent alt örneklemesini yansıtır. Daha büyük görüntüler daha uzun diziler üretir ve gürültü zamanlamasını buna göre kaydırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Örnekleyici için denoising zamanlamasını tanımlayan gürültü seviyesi değerleri (sigma) dizisi. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`

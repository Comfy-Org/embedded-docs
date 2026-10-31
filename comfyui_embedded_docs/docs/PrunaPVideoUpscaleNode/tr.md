# Pruna P-Video Upscale

Pruna P-Video Upscale, en-boy oranını ve ses parçasını koruyarak bir videoyu 720p, 1080p, 2K veya 4K'ya büyütür. Klip Pruna'ya gönderilir, tahmin durumu sorgulanır ve büyütülmüş video döndürülür. Hedef boyuta zaten eşit veya daha büyük olan bir kaynak, boyutlarını korur ve yalnızca iyileştirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Büyütülecek video, 512 MiB'a kadar. 10 megapikselden büyük videolar yalnızca 2K veya 4K hedefine gönderilebilir. | VIDEO | Evet | 512 MiB'a kadar |
| `target` | Çıktı piksel alanı: 720p yaklaşık 0,9 megapiksel, 1080p 2,1, 2K 3,7 ve 4K 8,3'tür. En uzun klip hedefe göre sınırlanır: 2400, 1200, 600 veya 300 kare; 24 fps'te yaklaşık 100, 50, 25 veya 12,5 saniye (varsayılan: "1080p"). | COMBO | Evet | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | Çıktı kare hızı (varsayılan: "source"). "source" videonun hızını korur, 60'a kadar; daha yüksek bir hız enterpolasyonla elde edilir. 30 fps üzerindeki çıktı iki kat maliyetlidir. | COMBO | Evet | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | Aynı fiyatla daha yumuşak ayrıntılarla daha hızlı büyütme (varsayılan: false). | BOOLEAN | Hayır | true<br>false |

### Parametre Kısıtlamaları

- Klip, H.264 MP4 olarak yeniden kodlandıktan sonra ölçüldüğünde 512 MiB veya daha küçük olmalıdır.
- Kare sınırı 30 fps'e kadar sayılır: 720p için 2400 kare, 1080p için 1200, 2K için 600 ve 4K için 300. Daha uzun bir klip daha düşük bir hedef, daha düşük `fps` veya daha kısa bir kesit gerektirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Orijinal sesiyle birlikte büyütülmüş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `e8fc88b6177085e0852d17ff92b0a22a26c9914c012a9a244b19da9b2c0e38c2`

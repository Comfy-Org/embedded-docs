# Kling Omni Video'dan Video'ya (Pro)

Bu düğüm, bir girdi videosu ve isteğe bağlı referans görüntülerine dayanarak yeni bir video oluşturmak için Kling AI modelini kullanır. İstenen içeriği tanımlayan bir metin istemi (prompt) sağlarsınız ve düğüm, referans videoyu buna göre dönüştürür. Ayrıca, çıktının stilini ve içeriğini yönlendirmek için en fazla dört ek referans görüntüsü de dahil edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: "kling-v3-omni"). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz tanımlamalar içerebilir. | STRING | Evet | Yok |
| `aspect_ratio` | Oluşturulan video için istenen en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 3). | INT | Evet | 3 ila 10 |
| `reference_video` | Referans olarak kullanılacak video. | VIDEO | Evet | Yok |
| `keep_original_sound` | Referans videodaki sesin çıktıda korunup korunmayacağını belirler (varsayılan: True). | BOOLEAN | Evet | Yok |
| `reference_images` | En fazla 4 adet ek referans görüntüsü. | IMAGE | Hayır | Yok |
| `resolution` | Oluşturulan video için çözünürlük (varsayılan: "1080p"). | COMBO | Hayır | `"1080p"`<br>`"720p"` |
| `tohum` | Tohum (seed), düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |

**Parametre Kısıtlamaları:**

* `prompt` 1 ile 2500 karakter arasında olmalıdır.
* `reference_video` 3.0 ile 10.05 saniye arasında bir süreye sahip olmalıdır.
* `reference_video` 720x720 ile 2160x2160 piksel arasında boyutlara sahip olmalıdır.
* En fazla 4 adet `reference_images` sağlanabilir. Her görüntü en az 300x300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Yeni oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `1bed976530603bcf7db67048e89ad6adac218fba8597744f8ece3e16a2ee4993`

# Kling Omni Video'dan Video'ya (Pro)

Bu düğüm, bir giriş videosu ve isteğe bağlı referans görsellerine dayalı yeni bir video oluşturmak için Kling AI modelini kullanır. İstenen içeriği açıklayan bir metin istemi sağlarsınız ve düğüm referans videoyu buna göre dönüştürür. Çıktının stilini ve içeriğini yönlendirmek için en fazla dört ek referans görsel de ekleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: "kling-v3-omni"). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini açıklayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. | STRING | Evet | N/A |
| `aspect_ratio` | Oluşturulan video için istenen en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 3). | INT | Evet | 3 ile 10 |
| `reference_video` | Referans olarak kullanılacak video. | VIDEO | Evet | N/A |
| `keep_original_sound` | Referans videodaki sesin çıktıda korunup korunmayacağını belirler (varsayılan: True). | BOOLEAN | Evet | N/A |
| `reference_images` | En fazla 4 ek referans görsel. | IMAGE | Hayır | N/A |
| `resolution` | Oluşturulan video için çözünürlük (varsayılan: "1080p"). | COMBO | Hayır | `"1080p"`<br>`"720p"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 |

**Parametre Kısıtlamaları:**

* `prompt` 1 ile 2500 karakter uzunluğunda olmalıdır.
* `reference_video` süresi 3.0 ile 10.05 saniye arasında olmalıdır.
* `reference_video` boyutları 720x720 ile 2160x2160 piksel arasında olmalıdır.
* En fazla 4 `reference_images` sağlanabilir. Her görsel en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Yeni oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `3dc2e3d153ddd9e6da705b764c51b4a859d66464b893fdebb0689d2ad5e870c7`

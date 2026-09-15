# Reve Görsel Oluştur

Reve Image Create düğümü, Reve AI modelini kullanarak bir metin açıklamasından görüntüler üretir. Prompt'u Reve API'sine gönderir ve isteğe bağlı olarak büyütme ve arka plan kaldırma son işlemleriyle birlikte ortaya çıkan görüntüyü döndürür. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak model sürümü. | DYNAMIC_COMBO | Evet | `"reve-create@20250915"` |
| `prompt` | İstenen görüntünün metin açıklaması. En fazla 2560 karakter. Varsayılan: "" (boş). | STRING | Evet | 1 - 2560 karakter |
| `upscale` | Üretilen görüntüyü büyütür. Ek maliyet ekleyebilir. Varsayılan: "disabled". | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Üretilen görüntünün arka planını kaldırır. Ek maliyet ekleyebilir. Varsayılan: False. | BOOLEAN | Hayır | N/A |
| `seed` | `seed`, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Hayır | 0 - 2147483647 |

### reve-create@20250915 Girdileri

`model` parametresi `"reve-create@20250915"` olarak ayarlandığında kullanılabilen seçenekler:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. | COMBO | Evet | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla kredi harcar. Varsayılan: 1. Gelişmiş seçenek. | INT | Hayır | 1 - 5 |

### Büyütme Girdileri

`upscale` parametresi `"enabled"` olarak ayarlandığında kullanılabilen seçenekler:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). Varsayılan: 2. | INT | Hayır | 2 - 4 |

**Not:** `prompt` 1 ile 2560 karakter arasında olmalıdır. `upscale_factor` girdisi yalnızca `upscale` `"enabled"` olarak ayarlandığında görünür. `seed` parametresi deterministik çıktıları garanti etmez — sonuçlar seed değerinden bağımsız olarak deterministik değildir. Hem `upscale` hem de `remove_background` ek maliyet ekleyebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Girdi promptuna dayalı olarak Reve modeli tarafından üretilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/tr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`

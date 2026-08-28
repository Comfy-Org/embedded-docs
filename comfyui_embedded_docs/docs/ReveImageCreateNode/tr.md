# Reve Görsel Oluştur

Reve Image Create düğümü, Reve AI modelini kullanarak metin açıklamalarından görseller üretir. Metin prompt'unu Reve API'sine gönderir ve üretilen görseli; en-boy oranı kontrolleri ile büyütme ve arka plan kaldırma gibi isteğe bağlı son işleme adımlarıyla birlikte döndürür. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak model sürümü. | DYNAMIC_COMBO | Evet | `"reve-create@20250915"` |
| `prompt` | İstenen görselin metin açıklaması. En fazla 2560 karakter. | STRING | Evet | 1 ila 2560 karakter |
| `upscale` | Üretilen görseli büyütür. Ek maliyet ekleyebilir. Varsayılan: "disabled". | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Üretilen görselden arka planı kaldırır. Ek maliyet ekleyebilir. Varsayılan: False. | BOOLEAN | Hayır | N/A |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Hayır | 0 ila 2147483647 |

### reve-create@20250915 Girdileri

`model` parametresi `"reve-create@20250915"` olarak ayarlandığında kullanılabilir seçenekler:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Çıktı görselinin en-boy oranı. | COMBO | Evet | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Daha yüksek değerler daha iyi görseller üretir ancak daha fazla kredi harcar. Varsayılan: 1. Gelişmiş seçenek. | INT | Hayır | 1 ila 5 |

### Upscale Girdileri

`upscale` parametresi `"enabled"` olarak ayarlandığında kullanılabilir seçenekler:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). Varsayılan: 2. | INT | Hayır | 2 ila 4 |

**Not:** `seed` parametresi deterministik çıktıları garanti etmez. `upscale` parametresi, büyütmenin son işleme adımı olarak uygulanıp uygulanmadığını kontrol eder ve ek maliyet ekleyebilir. `prompt` 1 ila 2560 karakter arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Reve modelinin girdi prompt'una göre ürettiği görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/tr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`

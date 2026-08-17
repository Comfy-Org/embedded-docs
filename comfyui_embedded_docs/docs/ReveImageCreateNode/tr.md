# Reve Görsel Oluştur

Reve Image Create düğümü, Reve AI modelini kullanarak metin açıklamalarından görüntüler üretir. Metin istemini (prompt) Reve API'ye gönderir ve üretilen görüntüyü döndürür. Görüntünün en-boy oranını kontrol edebilir ve yükseltme (upscaling) ile arka plan kaldırma gibi isteğe bağlı işlem sonrası efektler uygulayabilirsiniz. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model sürümü. Bu model seçildiğinde `aspect_ratio` ve `test_time_scaling` ayarları görünür. | DYNAMIC_COMBO | Evet | `"reve-create@20250915"` |
| `prompt` | İstenen görüntünün metin açıklaması. En fazla 2560 karakter. Varsayılan: boş. | STRING | Evet | N/A |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Hayır | 0 to 2147483647 |
| `upscale` | Üretilen görüntüyü büyütür. Ek maliyet getirebilir. `enabled` olarak ayarlandığında `upscale_factor` ayarı görünür. Varsayılan: `disabled`. | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Üretilen görüntüden arka planı kaldırır. Ek maliyet getirebilir. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |

### reve-create@20250915 Girdileri

Bu ayarlar `model` değeri `"reve-create@20250915"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. | COMBO | Evet | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla kredi harcar. Varsayılan: 1. | INT | Hayır | 1 to 5 |

### Upscale Girdileri

Bu ayarlar `upscale` değeri `"enabled"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). Varsayılan: 2. | INT | Hayır | 2 to 4 (step 1) |

**Not:** `seed` parametresi deterministik çıktıları garanti etmez. `upscale` parametresi, işlem sonrası bir adım olarak büyütmenin uygulanıp uygulanmayacağını kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-------------|-----------|
| `image` | Reve modelinin verilen isteme dayanarak ürettiği görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/tr.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`

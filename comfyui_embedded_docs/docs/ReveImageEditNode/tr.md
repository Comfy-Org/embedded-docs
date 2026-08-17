# Reve Görsel Düzenle

Reve Image Edit düğümü, mevcut bir görüntüyü metin açıklamasına dayalı olarak değiştirmenizi sağlar. Talimatlarınızı yorumlamak ve istediğiniz değişiklikleri sağladığınız görüntüye uygulamak için Reve API'sini kullanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Düzenlenecek görüntü. | IMAGE | Evet | - |
| `edit_instruction` | Görüntünün nasıl düzenleneceğine dair metin açıklaması. En fazla 2560 karakter. (varsayılan: "") | STRING | Evet | 1 ile 2560 karakter arası |
| `model` | Düzenleme için kullanılacak model sürümü. | DYNAMIC_COMBO | Evet | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Oluşturulan görüntüyü büyütür. Ek maliyet getirebilir. (varsayılan: "disabled") | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Oluşturulan görüntüden arka planı kaldırır. Ek maliyet getirebilir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

### Model Girdileri

`reve-edit@20250915` ve `reve-edit-fast@20251030` modelleri tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | Çıktı görüntüsünün en-boy oranı. `"auto"` olarak ayarlandığında, en-boy oranı otomatik olarak belirlenir. (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Daha yüksek değerler daha iyi görüntüler üretir ancak daha fazla krediye mal olur. (varsayılan: 1) | INT | Hayır | 1 ile 5 arası |

### Upscale Girdileri

`upscale` değeri `"enabled"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Büyütme faktörü (2x, 3x veya 4x). (varsayılan: 2) | INT | Hayır | 2 ile 4 arası |

**Not:** `upscale.upscale_factor` parametresi yalnızca `upscale` değeri `"enabled"` olarak ayarlandığında görünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Talimatlara göre oluşturulan düzenlenmiş görüntü. | IMAGE |

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`

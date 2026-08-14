# Wan 2.7 Video Devamı

Wan 2.7 Video Devamı düğümü, bir girdi video klibinin sonundan itibaren devam eden yeni bir video segmenti üretir. Devamı metin istemine göre sentezlemek için Wan 2.7 modelini kullanır ve isteğe bağlı olarak bitişi belirli bir hedef kareye yönlendirebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak video üretim modeli. | COMBO | Evet | `"wan2.7-i2v"` |
| `first_clip` | Devam edilecek girdi videosu. Süre: 2s-10s. Çıktı en-boy oranı bu videodan türetilir. | VIDEO | Evet | 2 ile 10 saniye arası |
| `last_frame` | Son kare görüntüsü. Devam, bu kareye doğru geçiş yapar. | IMAGE | Hayır | - |
| `seed` | Üretim için kullanılacak seed. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `prompt_extend` | İstem'in yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. (varsayılan: True) | BOOLEAN | Evet | - |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Evet | - |

### wan2.7-i2v Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: boş dize) | STRING | Evet | - |
| `model.negative_prompt` | Kaçınılması gerekenleri tanımlayan olumsuz istem. (varsayılan: boş dize) | STRING | Evet | - |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.duration` | Saniye cinsinden toplam çıktı süresi. Model, girdi klibinden sonra kalan süreyi doldurmak için devamı üretir. (varsayılan: 5) | INT | Evet | 2 ile 15 arası |

**Not:** `first_clip` girdi videosunun süresi 2 ile 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video devamı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/tr.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`

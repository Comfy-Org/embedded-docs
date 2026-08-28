# Wan 2.7 Görüntüden Videoya

Wan 2.7 Image to Video düğümü, ilk kare görüntüsünden başlayarak bir video oluşturur. İsteğe bağlı olarak, iki görüntü arasında geçiş oluşturmak için bir son kare görüntüsü veya videonun hareketini ve zamanlamasını yönlendirmek için bir ses dosyası sağlayabilirsiniz. Düğüm, sahneyi metin açıklamanıza göre canlandırmak için bir yapay zeka modeli kullanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak yapay zeka modeli. | DYNAMIC_COMBO | Evet | `"wan2.7-i2v"` |
| `first_frame` | İlk kare görüntüsü. Çıktının en-boy oranı bu görüntüden türetilir. | IMAGE | Evet | - |
| `last_frame` | Son kare görüntüsü. Model, ilk kareden son kareye geçiş yapan bir video oluşturur. | IMAGE | Hayır | - |
| `audio` | Video oluşturmayı yönlendirmek için ses (örn. dudak senkronizasyonu, ritim eşleşmeli hareket). Süre: 2sn-30sn. Sağlanmazsa model otomatik olarak uygun arka plan müziği veya ses efektleri üretir. | AUDIO | Hayır | - |
| `seed` | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `prompt_extend` | İstem yapay zeka yardımıyla geliştirilsin mi (varsayılan: True). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True<br>False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklensin mi (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True<br>False |

### wan2.7-i2v Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: boş) | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan olumsuz istem. (varsayılan: boş) | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ile 15 |

**Not:** `audio` girdisinin bir süre sınırı vardır. Sağlanırsa ses dosyası 2 ila 30 saniye uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`

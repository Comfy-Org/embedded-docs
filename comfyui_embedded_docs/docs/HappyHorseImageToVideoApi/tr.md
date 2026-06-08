## Genel Bakış

Bu düğüm, HappyHorse modelini kullanarak tek bir başlangıç görüntüsünden kısa bir video oluşturur. Bir ilk kare görüntüsü ve istenen hareket ile sahneyi tanımlayan bir metin istemi sağlarsınız; düğüm, bu görüntüden devam eden bir video oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak HappyHorse modeli. | COMBO | Evet | `"happyhorse-1.0-i2v"` |
| `model.prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. (varsayılan: "") | STRING | Hayır | Yok |
| `model.resolution` | Çıktı video çözünürlüğü. (varsayılan: "720P") | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.duration` | Oluşturulan videonun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 3 ila 15 |
| `ilk_kare` | İlk kare görüntüsü. Çıktı en-boy oranı bu görüntüden türetilir. | IMAGE | Evet | Yok |
| `tohum` | Oluşturma için kullanılacak tohum değeri. (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`

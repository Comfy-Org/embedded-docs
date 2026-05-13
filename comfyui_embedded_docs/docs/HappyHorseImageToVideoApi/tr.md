> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/tr.md)

## Genel Bakış

Bu düğüm, HappyHorse modelini kullanarak tek bir başlangıç görüntüsünden kısa bir video oluşturur. Bir ilk kare görüntüsü ve istenen hareket ile sahneyi tanımlayan bir metin istemi sağlarsınız; düğüm, bu görüntüden devam eden bir video oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"happyhorse-1.0-i2v"` | Video oluşturma için kullanılacak HappyHorse modeli. |
| `model.prompt` | STRING | Hayır | Yok | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. (varsayılan: "") |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı video çözünürlüğü. (varsayılan: "720P") |
| `model.duration` | INT | Evet | 3 ila 15 | Oluşturulan videonun saniye cinsinden süresi. (varsayılan: 5) |
| `ilk_kare` | IMAGE | Evet | Yok | İlk kare görüntüsü. Çıktı en-boy oranı bu görüntüden türetilir. |
| `tohum` | INT | Hayır | 0 ila 2147483647 | Oluşturma için kullanılacak tohum değeri. (varsayılan: 0) |
| `filigran` | BOOLEAN | Hayır | True / False | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`

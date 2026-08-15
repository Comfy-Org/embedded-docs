# HappyHorse Görüntüden Videoya

Bu düğüm, HappyHorse modelini kullanarak tek bir başlangıç görüntüsünden kısa bir video oluşturur. İlk kare görüntüsü ve istenen hareketi ve sahneyi tanımlayan bir metin istemi sağlarsınız; düğüm, bu görüntüden devam eden bir video oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak HappyHorse modeli. | DYNAMIC_COMBO | Evet | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `ilk_kare` | İlk kare görüntüsü. Çıktı en-boy oranı bu görüntüden türetilir. | IMAGE | Evet | min. 300×300 piksel; oran 1:2.5 ile 2.5:1 arası |
| `tohum` | Üretim için kullanılacak tohum. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (gelişmiş seçenek; varsayılan: False) | BOOLEAN | Hayır | True / False |

### happyhorse-1.1-i2v ve happyhorse-1.0-i2v Girdileri

Her iki model sürümü de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: "") | STRING | Hayır | N/A |
| `çözünürlük` | Çıktı video çözünürlüğü. (varsayılan: "720P") | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `süre` | Oluşturulan videonun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 3 ile 15 |

Not: `first_frame` görüntüsü en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`

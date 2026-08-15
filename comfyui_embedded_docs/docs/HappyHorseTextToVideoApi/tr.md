# HappyHorse Metinden Videoya

HappyHorse modelini kullanarak metin istemine dayalı bir video oluşturur. Bu düğüm, isteminizi ve ayarlarınızı HappyHorse API'sine gönderir, videonun oluşturulmasını bekler ve ardından sonucu indirir.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılan HappyHorse modeli ve alt parametreleri. Bir model seçmek, hangi alt parametrelerin kullanılabilir olduğunu belirler (aşağıdaki model bölümlerine bakın). | DICT | Evet | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `tohum` | Üretim için kullanılacak tohum (seed). Aynı girdilerle aynı tohumu kullanmak aynı sonucu üretir. (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False). | BOOLEAN | Hayır | True / False |

### happyhorse-1.1-t2v Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: ""). | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | STRING | Evet | "720P"<br>"1080P" |
| `oran` | Çıktı videosunun en-boy oranı. | STRING | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `süre` | Videonun saniye cinsinden uzunluğu. (varsayılan: 5, min: 3, max: 15, step: 1). | INT | Evet | 3 ile 15 arası |

### happyhorse-1.0-t2v Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: ""). | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | STRING | Evet | "720P"<br>"1080P" |
| `oran` | Çıktı videosunun en-boy oranı. | STRING | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `süre` | Videonun saniye cinsinden uzunluğu. (varsayılan: 5, min: 3, max: 15, step: 1). | INT | Evet | 3 ile 15 arası |

Not: İstem boş olmamalıdır; istem sağlanmazsa bir hata oluşturulur. Her iki model de 3 ila 15 saniye arası video sürelerini destekler. `happyhorse-1.1-t2v` modeli, `happyhorse-1.0-t2v` ile kullanılamayan ek en-boy oranları (`21:9`, `9:21`, `5:4`, `4:5`) sunar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`

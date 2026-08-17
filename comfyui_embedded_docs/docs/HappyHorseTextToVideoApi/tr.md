# HappyHorse Metinden Videoya

HappyHorse modelini kullanarak metin istemine dayalı bir video oluşturur. Bu düğüm, isteminizi ve ayarlarınızı HappyHorse API'sine gönderir, videonun oluşturulmasını bekler ve ardından sonucu indirir.
## Girişler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Üretim için kullanılan HappyHorse modeli ve alt parametreleri. Bir model seçmek, hangi alt parametrelerin kullanılabilir olduğunu belirler (aşağıdaki model bölümlerine bakın). | DYNAMIC_COMBO | Evet | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Üretim için kullanılacak tohum (seed). Aynı girdilerle aynı tohumu kullanmak aynı sonucu üretir. (varsayılan: 0). | INT | Evet | 0 to 2147483647 |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False). | BOOLEAN | Evet | True / False |

### happyhorse-1.1-t2v Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: ""). | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `duration` | Videonun saniye cinsinden uzunluğu. (varsayılan: 5, min: 3, max: 15, step: 1). | INT | Evet | 3 to 15 |

### happyhorse-1.0-t2v Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. (varsayılan: ""). | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Videonun saniye cinsinden uzunluğu. (varsayılan: 5, min: 3, max: 15, step: 1). | INT | Evet | 3 to 15 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `VIDEO` | The generated video file. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`

# Wan 2.7 Referanstan Videoya

Bu düğüm, sağlanan referans materyallerine dayalı olarak bir kişiyi veya nesneyi içeren bir video üretir. Metin isteminden videolar oluşturmak için Wan 2.7 modelini kullanır; tek karakterli performansları ve çok karakterli etkileşimleri destekler. Üretimin çalışması için en az bir referans video veya referans görsel sağlamanız gerekir.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak belirli model. | DYNAMIC_COMBO | Evet | "wan2.7-r2v" |
| `seed` | Üretim için kullanılan ve çıktının rastgeleliğini kontrol etmeye yardımcı olan tohum (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |
| `watermark` | Sonuca yapay zeka tarafından üretilmiş bir filigran eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True<br>False |

### wan2.7-r2v Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istek` | Videoyu tanımlayan istem. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. En az bir karakter içermelidir. | STRING | Evet | - |
| `negatif_istek` | Kaçınılması gerekenleri tanımlayan negatif istem (varsayılan: boş). | STRING | Hayır | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `oran` | Çıktı videosunun en-boy oranı. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `süre` | Üretilen videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ile 10 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `reference_videos` | Genişletilebilir yuva: en fazla 3 referans videosu bağlayın (`video1` ile `video3` arasındaki yuvalar). Genel olarak en az bir referans videosu veya görseli gereklidir. | VIDEO | Hayır | 0 ile 3 öğe arası |
| `reference_images` | Genişletilebilir yuva: en fazla 5 referans görseli bağlayın (`image1` ile `image5` arasındaki yuvalar). Genel olarak en az bir referans videosu veya görseli gereklidir. | IMAGE | Hayır | 0 ile 5 öğe arası |

**Önemli Kısıtlamalar:**

* `model.reference_videos` veya `model.reference_images` girdilerinde en az bir referans videosu veya referans görseli sağlamalısınız.
* Referans videoları ve referans görsellerinin toplam birleşik sayısı 5'i aşamaz.
* `model.prompt` girdisi en az bir karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`

# Wan 2.7 Referanstan Videoya

Bu düğüm, sağlanan referans materyallerine dayalı olarak bir kişi veya nesneyi içeren bir video üretir. Metin isteminden videolar oluşturmak için Wan 2.7 modelini kullanır; tek karakterli performansları ve çok karakterli etkileşimleri destekler. Üretimin çalışması için en az bir referans video veya referans görsel sağlamalısınız.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak belirli model. | DYNAMIC_COMBO | Evet | "wan2.7-r2v" |
| `seed` | Üretim için kullanılacak tohum değeri; çıktının rastgeleliğini kontrol etmeye yardımcı olur (varsayılan: 0). | INT | Evet | 0 - 2147483647 |
| `watermark` | Sonuca yapay zekâ tarafından oluşturulmuş filigran eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True<br>False |

### wan2.7-r2v Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Videoyu tanımlayan istem. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcıları kullanın. En az bir karakter içermelidir. | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem (varsayılan: boş). | STRING | Hayır | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 - 10 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `reference_videos` | Genişletilebilir yuva: en fazla 3 referans video bağlayın (`video1` ile `video3` yuvaları). Toplamda en az bir referans video veya görsel gereklidir. | VIDEO | Hayır | 0 - 3 öğe |
| `reference_images` | Genişletilebilir yuva: en fazla 5 referans görsel bağlayın (`image1` ile `image5` yuvaları). Toplamda en az bir referans video veya görsel gereklidir. | IMAGE | Hayır | 0 - 5 öğe |

**Önemli Kısıtlamalar:**

* `reference_videos` veya `reference_images` girdilerinde en az bir referans video ya da referans görsel sağlamalısınız. Aksi halde düğüm bir hata oluşturur.
* Referans videolarının ve referans görsellerinin toplam birleşik sayısı 5'i aşamaz.
* `prompt` girdisi en az bir karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`

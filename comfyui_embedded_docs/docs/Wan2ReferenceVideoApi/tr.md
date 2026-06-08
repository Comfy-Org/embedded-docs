Bu düğüm, sağlanan referans materyallere dayanarak bir kişi veya nesneyi içeren bir video oluşturur. Metin isteminden video oluşturmak için Wan 2.7 modelini kullanır; tek karakterli performansları ve çok karakterli etkileşimleri destekler. Oluşturma işleminin çalışması için en az bir referans videosu veya görseli sağlamanız gerekir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak belirli model. | COMBO | Evet | `"wan2.7-r2v"` |
| `model.prompt` | Videoyu tanımlayan istem. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. | STRING | Evet | - |
| `model.negative_prompt` | Oluşturulan videoda kaçınılması gerekenleri açıklayan olumsuz istem (varsayılan: boş). | STRING | Hayır | - |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ila 10 |
| `model.reference_videos` | Bir referans videoları listesi. En fazla 3 video ekleyebilirsiniz. | VIDEO | Hayır | - |
| `model.reference_images` | Bir referans görselleri listesi. En fazla 5 görsel ekleyebilirsiniz. | IMAGE | Hayır | - |
| `seed` | Oluşturma için kullanılacak tohum değeri; çıktının rastgeleliğini kontrol etmeye yardımcı olur (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Hayır | - |

**Önemli Kısıtlamalar:**
*   `model.reference_videos` veya `model.reference_images` girişlerinde en az bir referans videosu veya referans görseli sağlamanız gerekir.
*   Referans videolarının ve görsellerinin toplam birleşik sayısı 5'i geçemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `f28a765e310410fc62241e11dbfe25562c7ae16e8e6ffbfb004face7a7e2b727`

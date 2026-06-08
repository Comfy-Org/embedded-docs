## Genel Bakış

Bu düğüm, HappyHorse modelini kullanarak referans görüntülere dayalı olarak bir kişi veya nesneyi içeren bir video oluşturur. Tek bir karakter veya birbiriyle etkileşime giren birden fazla karakter içeren videolar oluşturmayı destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak HappyHorse modeli. | COMBO | Evet | `"happyhorse-1.0-r2v"` |
| `prompt` | Oluşturmak istediğiniz videonun metin açıklaması. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. | STRING | Evet | Yok |
| `resolution` | Oluşturulan videonun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | Oluşturulan videonun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 ila 15 |
| `reference_images` | Videoda yer alacak kişi veya nesnenin bir veya daha fazla referans görüntüsü. En az bir görüntü sağlamanız gerekir. | IMAGE | Evet | 1 ila 9 |
| `tohum` | Tekrarlanabilir oluşturma için bir tohum değeri (varsayılan: 0). Tohum, her oluşturmadan sonra otomatik olarak değişecek şekilde ayarlanabilir. | INT | Hayır | 0 ila 2147483647 |
| `filigran` | Ortaya çıkan videoya yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | True veya False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `VIDEO` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`

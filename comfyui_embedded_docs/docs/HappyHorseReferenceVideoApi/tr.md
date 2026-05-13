> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/tr.md)

## Genel Bakış

Bu düğüm, HappyHorse modelini kullanarak referans görüntülere dayalı olarak bir kişi veya nesneyi içeren bir video oluşturur. Tek bir karakter veya birbiriyle etkileşime giren birden fazla karakter içeren videolar oluşturmayı destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | COMBO | Evet | `"happyhorse-1.0-r2v"` | Video oluşturma için kullanılacak HappyHorse modeli. |
| `prompt` | STRING | Evet | Yok | Oluşturmak istediğiniz videonun metin açıklaması. Referans karakterlere atıfta bulunmak için 'character1' ve 'character2' gibi tanımlayıcılar kullanın. |
| `resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Oluşturulan videonun çözünürlüğü. |
| `ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Oluşturulan videonun en-boy oranı. |
| `duration` | INT | Evet | 3 ila 15 | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 5). |
| `reference_images` | IMAGE | Evet | 1 ila 9 | Videoda yer alacak kişi veya nesnenin bir veya daha fazla referans görüntüsü. En az bir görüntü sağlamanız gerekir. |
| `tohum` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir oluşturma için bir tohum değeri (varsayılan: 0). Tohum, her oluşturmadan sonra otomatik olarak değişecek şekilde ayarlanabilir. |
| `filigran` | BOOLEAN | Hayır | True veya False | Ortaya çıkan videoya yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `VIDEO` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`

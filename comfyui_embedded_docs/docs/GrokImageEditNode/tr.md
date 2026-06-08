Grok Görüntü Düzenleme düğümü, bir metin istemine dayanarak mevcut bir görüntüyü değiştirir. Girdi görüntünüzün varyasyonları olan bir veya daha fazla yeni görüntü oluşturmak için Grok API'sini kullanır; bu süreç açıklamanız tarafından yönlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Görüntü düzenleme için kullanılacak belirli AI modeli. | COMBO | Evet | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `görüntü` | Düzenlenecek girdi görüntüsü/görüntüleri. "Pro" modeli yalnızca 1 görüntüyü desteklerken, diğer modeller en fazla 3 girdi görüntüsünü destekler. | IMAGE | Evet |  |
| `istem` | Düzenlenmiş görüntüyü oluşturmak için kullanılan metin istemi. Boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır. | STRING | Evet |  |
| `çözünürlük` | Çıktı görüntüsünün çözünürlüğü. | COMBO | Evet | `"1K"`<br>`"2K"` |
| `görüntü sayısı` | Oluşturulacak düzenlenmiş görüntü sayısı (varsayılan: 1). | INT | Hayır | 1 ila 10 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `en-boy oranı` | Çıktı görüntüsünün en-boy oranı. Yalnızca görüntü girişine birden fazla görüntü bağlandığında izin verilir. "auto" olarak ayarlanırsa, en-boy oranı otomatik olarak belirlenir (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Önemli kısıtlamalar:**
- `image` girişi, `grok-imagine-image-pro` modeli kullanılırken yalnızca 1 girdi görüntüsünü destekler; diğer modellerde en fazla 3 görüntü desteklenir.
- `aspect_ratio` parametresi, yalnızca `image` girişine birden fazla görüntü bağlandığında özel bir değere ("auto" dışında) ayarlanabilir. Tek bir girdi görüntüsüyle özel bir en-boy oranı ayarlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Düğüm tarafından oluşturulan düzenlenmiş görüntü(ler). `görüntü sayısı` 1'den büyükse, çıktılar bir toplu iş halinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `021d867e9e04451c0c4ef035c19fa86ebc8d4a3f64572aff33f493324d7fe308`

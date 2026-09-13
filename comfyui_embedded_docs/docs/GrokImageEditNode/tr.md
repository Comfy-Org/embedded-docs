# Grok Görüntü Düzenle

Grok Image Edit düğümü, bir metin istemi temelinde mevcut bir görüntüyü değiştirir. Girdi görüntüyü/görüntüleri ve açıklamanızı Grok API'sine gönderir ve istemi takip eden bir veya daha fazla yeni oluşturulmuş görüntü döndürür. Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü düzenleme için kullanılacak belirli yapay zeka modeli. | COMBO | Evet | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | Düzenlenecek girdi görüntü(ler). | IMAGE | Evet |  |
| `prompt` | Görüntüyü oluşturmak için kullanılan metin istemi. Çok satırlı metin; en az bir boşluk dışı karakter içermelidir. | STRING | Evet |  |
| `resolution` | Çıktı görüntüsü için çözünürlük. | COMBO | Evet | `"1K"`<br>`"2K"` |
| `number_of_images` | Oluşturulacak düzenlenmiş görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ile 10 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `aspect_ratio` | Çıktı görüntüsü için en-boy oranı. Yalnızca `image` girdisine birden çok görüntü bağlandığında izin verilir (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Önemli kısıtlamalar:**
- `image` girdisi en fazla 3 görüntüyü destekler; ancak `grok-imagine-image-pro` modeli kullanıldığında bu model yalnızca 1 girdi görüntüsünü destekler.
- `aspect_ratio` parametresi yalnızca `image` girdisine birden çok görüntü bağlandığında özel bir değere ("auto" dışında) ayarlanabilir. Tek bir girdi görüntüsüyle özel en-boy oranı ayarlamak hataya neden olur.
- `prompt` en az bir boşluk dışı karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Düğüm tarafından oluşturulan düzenlenmiş görüntü(ler). Birden fazla görüntü oluşturulursa, görüntüler tek bir toplu iş halinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`

# Tencent HY Image: Text to Image

Tencent HY Image: Text to Image düğümü, Tencent'in Hunyuan Image modeliyle bir metin açıklamasından görüntü oluşturur. İstem API'ye gönderilir; API, oluşturmadan önce istemi yeniden yazar ve genişletir, tamamlanan görüntü ise bir görüntü grubu olarak döndürülür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılan model. Seçilen model, hangi ek girdilerin gösterileceğini belirler. | DYNAMIC_COMBO | Evet | `"hy-image-3.5-preview"` |

### hy-image-3.5-preview Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü tanımlar. Model, oluşturmadan önce istemi yeniden yazar ve genişletir. Boş olmamalıdır (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `aspect_ratio` | Çıktının en-boy oranı. `"auto"`, modelin oranı istemden seçmesini sağlar ve 4K'da kullanılamaz. `resolution` `"custom"` olduğunda yok sayılır. | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (varsayılan: `"auto"`) |
| `resolution` | Görüntünün piksel alanı: 1K yaklaşık 1024x1024, 2K yaklaşık 2048x2048 ve 4K yaklaşık 4096x4096'dır. 2K'nın üzerindeki her şey 2K'da oluşturulur ve model tarafından büyütülür. Ön ayarlı alan yerine `width` ve `height` kullanmak için `"custom"` olarak ayarlayın. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (varsayılan: `"2K"`) |
| `width` | Görüntünün piksel cinsinden genişliği. Yalnızca `resolution` `"custom"` olduğunda kullanılır. | INT | Evet | 256-8192, 16'lık adımlarla (varsayılan: 2048) |
| `height` | Görüntünün piksel cinsinden yüksekliği. Yalnızca `resolution` `"custom"` olduğunda kullanılır. | INT | Evet | 256-8192, 16'lık adımlarla (varsayılan: 2048) |
| `seed` | Oluşturma için kullanılan tohum. Aynı tohumla bile sonuçlar farklı çalıştırmalar arasında değişebilir. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | true<br>false (varsayılan: false) |

`prompt` boş olmamalıdır. `"custom"` çözünürlükte, `width` ve `height` değerlerinin ikisi de 16'nın katı olmalıdır ve çarpımları 4096 x 4096 piksel alan sınırını (yaklaşık 16,7 megapiksel) aşmamalıdır; herhangi bir en-boy oranı çalışır, ancak kabaca 6:1'in ötesinde model özneyi tekrarlamaya başlar. `"auto"` en-boy oranı, modelin bir boyut seçmesini gerektirir; bu nedenle yalnızca 2K alan sınırında çalışır: 4K'da açık bir en-boy oranı seçin veya `"custom"` kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`

# Tencent HY Image: Edit

Tencent HY Image: Edit düğümü, Tencent'in Hunyuan Image modeliyle bir metin talimatından referans görselleri düzenler veya birleştirir. Bir ila beş görsel bağlayın, istemde değişikliği tanımlayın ve görsellere `@Image1`, `@Image2` vb. şeklinde başvurun. Düğüm, referans görselleri yükler, isteği API'ye gönderir ve düzenlenmiş sonucu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Düzenleme için kullanılan model. Seçilen model, hangi ek girdilerin gösterileceğini belirler. | DYNAMIC_COMBO | Evet | `"hy-image-3.5-preview"` |

### hy-image-3.5-preview Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları. Bağlı görsellere `@Image1` tarzı başvuruları destekler. Boş olmamalıdır (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `aspect_ratio` | Çıktının en-boy oranı. `"auto"`, ilk referans görselin en-boy oranını izler ve 4K'da kullanılamaz. `resolution` `"custom"` olduğunda yok sayılır. | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (varsayılan: `"auto"`) |
| `resolution` | Çıktının piksel alanı: 1K yaklaşık 1024x1024, 2K yaklaşık 2048x2048 ve 4K yaklaşık 4096x4096'dır. 2K'nın üzerindeki her şey 2K'da işlenir ve model tarafından büyütülür. Ön ayarlı alan yerine `width` ve `height` kullanmak için `"custom"` olarak ayarlayın. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (varsayılan: `"2K"`) |
| `width` | Çıktının piksel cinsinden genişliği. Yalnızca `resolution` `"custom"` olduğunda kullanılır. | INT | Evet | 256-8192, 16'şar adımlarla (varsayılan: 2048) |
| `height` | Çıktının piksel cinsinden yüksekliği. Yalnızca `resolution` `"custom"` olduğunda kullanılır. | INT | Evet | 256-8192, 16'şar adımlarla (varsayılan: 2048) |
| `seed` | Üretim için kullanılan tohum. Aynı tohumla bile sonuçlar çalıştırmalar arasında değişebilir. | INT | Evet | 0-2147483647 (varsayılan: 42) |
| `reference_detail` | Modelin referans görsellerinin ne kadar ayrıntısını gördüğü: `"standard"` görsel başına 1024x1024 piksele kadar izin verir, `"high"` 2048x2048'e kadar izin verir ve küçük metni ve ince ayrıntıları daha iyi korur, ancak daha uzun sürer. Bu gelişmiş bir parametredir. | COMBO | Hayır | `"standard"`<br>`"high"` (varsayılan: `"standard"`) |
| `watermark` | Sonuca yapay zekâ tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | true<br>false (varsayılan: false) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Düzenlenecek veya birleştirilecek referans görseller. Büyütülebilir yuva: 1 ila 5 görsel bağlayın (`image_1` ile `image_5` arası). İstemde bunlara `@Image1` ... `@Image5` olarak başvurun; girdi sırasına göre numaralandırılır; toplu bir girdi, görsel başına bir kez sayılır. | IMAGE | Evet | 1-5 görsel |

`prompt` boş olmamalıdır ve yalnızca 1 veya 2 görsel bağlıyken `@Image3` gibi bir istem başvurusu hata verir. Toplamda en fazla 5 referans görseli kullanılabilir; bir toplu girişteki her görsel ayrı ayrı sayılır. `"custom"` çözünürlükte, `width` ve `height` her ikisi de 16'nın katı olmalıdır ve çarpımları 4096 x 4096 piksel alan sınırını (yaklaşık 16,7 megapiksel) aşmamalıdır; herhangi bir en-boy oranı çalışır, ancak kabaca 6:1'in ötesinde model özneyi tekrarlamaya başlar. `"auto"` en-boy oranı yalnızca 2K alan sınırı içinde çalışır, bu nedenle 4K'da açık bir en-boy oranı seçin veya `"custom"` kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Referans görsellerden ve istemden üretilen düzenlenmiş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`

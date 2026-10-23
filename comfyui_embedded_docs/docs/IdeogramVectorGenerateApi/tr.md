# Ideogram Vector Generate SVG

Bu düğüm, Ideogram Vector ile bir metin isteminden düzenlenebilir bir SVG oluşturur; isteğe bağlı olarak en fazla 5 referans görüntüyle yönlendirilebilir. Sonuç, raster görüntü yerine vektör işaretlemesidir, böylece şekiller bir vektör düzenleyicide düzenlenebilir kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Varsayılan: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Evet | `"ideogram-vector-1"` |
| `images` | İsteğe bağlı referans görüntüler. Görüntü 1 ana kaynaktır ve 2 ile 5 arasındaki görüntüler ek referanslardır; bunlardan istemde `@Image1`, `@Image2` vb. şeklinde bahsedin. Toplu (batched) bir girdi, her görüntü için bir kez sayılır. | AUTOGROW | Hayır | 0 ila 5 görüntü |
| `prompt` | SVG'nin açıklaması. Girdi görüntülerine `@Image1` tarzı referansları destekler. | STRING | Evet | 1 ila 9500 karakter |
| `aspect_ratio` | `"auto"`, görüntü 1'i veya görüntü bağlı değilse istemi takip eder. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"1:3"`<br>`"1:2"`<br>`"9:16"`<br>`"10:16"`<br>`"2:3"`<br>`"3:4"`<br>`"4:5"`<br>`"1:1"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:10"`<br>`"16:9"`<br>`"2:1"`<br>`"3:1"` |
| `quality` | Kalite seviyesi. Daha yüksek seviyeler daha pahalıdır ve daha uzun sürer. Varsayılan: `"medium"`. | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı istem, görüntüler, ayarlar ve tohum aynı SVG'yi verir. Varsayılan: 42. | INT | Evet | 0 ila 2147483647 |

**Kısıtlamalar:**

* İstem 1 ile 9500 karakter arasında olmalıdır.
* `images` en fazla 5 görüntü kabul eder; girdi toplu olduğunda her görüntü için sayılır ve her görüntünün en-boy oranı 1:6 ile 6:1 arasında olmalıdır.
* En uzun kenarı 2048 pikselin üzerinde olan görüntüler yüklemeden önce küçültülür.
* Bağlı olmayan bir görüntüye referans vermek, örneğin yalnızca iki görüntü sağlanmışken `@Image4` kullanmak, bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Düzenlenebilir vektör işaretlemesi olarak oluşturulan SVG. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/tr.md)

---
**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`

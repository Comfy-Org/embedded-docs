# ByteDance Seedance 2.0 Metinden Videoya

Bu düğüm, ByteDance'in Seedance 2.5 veya 2.0 modellerini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi seçilen modele gönderir, videonun işlenmesini bekler ve sonucu döndürür.

## Girdiler

`model` parametresi dinamik bir birleşik kutudur. Bir model seçtiğinizde, metin istemi, çözünürlük, en-boy oranı, süre ve ses üretim ayarı dahil olmak üzere doldurulması gereken birkaç modele özel girdi görüntülenir.

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. Seedance 2.5 en yeni modeldir ve mp4/mov çıktısıyla 30 saniyeye kadar videolar üretir; Seedance 2.0, 1080p/4k ile maksimum kalite sunar; Fast, hız optimizasyonu içindir; Mini, en hızlı ve en düşük maliyetli üretimdir. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir ayardır. | BOOLEAN | Hayır | True / False |

### Seedance 2.5 Girdileri

Bu girdiler `model` `Seedance 2.5` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için sözlü satırları çift tırnak içine alın (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "720p"). | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ile 30 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Hayır | True / False |
| `output_format` | Çıktı videosunun kap formatı (varsayılan: "mp4"). | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

Bu girdiler `model` `Seedance 2.0` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Hayır | True / False |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Bu girdiler `model` `Seedance 2.0 Fast` veya `Seedance 2.0 Mini` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Hayır | True / False |

**Not:** `prompt` boşluklar kaldırıldıktan sonra en az 1 karakter içermelidir, aksi takdirde görev doğrulamada başarısız olur. Süre sınırları modele bağlıdır: Seedance 2.5, 4 ile 30 saniye arasını desteklerken; Seedance 2.0, Seedance 2.0 Fast ve Seedance 2.0 Mini, 4 ile 15 saniye arasını destekler. Çözünürlük seçenekleri de modele göre farklılık gösterir: Seedance 2.5, 480p ve 720p'yi destekler; Seedance 2.0, 480p, 720p, 1080p ve 4k'yı destekler; Seedance 2.0 Fast ve Seedance 2.0 Mini yalnızca 480p ve 720p'yi destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`

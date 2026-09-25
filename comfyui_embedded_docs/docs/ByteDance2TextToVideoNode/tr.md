# ByteDance Seedance 2.0 Metinden Videoya

Bu düğüm, ByteDance'in Seedance 2.5 veya 2.0 modellerini kullanarak bir metin isteminden video üretir. İstemi seçilen modele gönderir, videonun işlenmesinin tamamlanmasını bekler ve sonuçta oluşan video dosyasını döndürür. `Seedance 2.5 Draft` modelinin seçilmesi bunun yerine hızlı bir 480p önizleme oluşturur; 1080p nihai çıktıyı oluşturmak için sonuçta oluşan `draft_task_id` değerini ByteDance Seedance 2.5 Draft to Final Video düğümüne bağlayın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak Seedance modeli. Seedance 2.5 en yeni modeldir; 30 saniyeye kadar videoları ve mp4/mov çıktısını destekler; Seedance 2.5 Draft, `draft_task_id` çıktısı ByteDance Seedance 2.5 Draft to Final Video düğümünde 1080p nihai çıktıyı oluşturan hızlı bir 480p önizleme oluşturur; Seedance 2.0 maksimum kalite ve 4k içindir; Seedance 2.0 Fast hız optimizasyonu içindir; Seedance 2.0 Mini en hızlı, en düşük maliyetli üretim içindir. Bir model seçildiğinde istem, çözünürlük, en-boy oranı, süre ve ses üretimi için ek girdiler görünür. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. (varsayılan: False) Bu gelişmiş bir ayardır. | BOOLEAN | Hayır | True / False |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Üretilen diyaloğu yönlendirmek için söylenen replikleri çift tırnak içine alın. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. (varsayılan: `"720p"`) | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 4 ile 30 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |
| `output_format` | Çıktı videosunun kapsayıcı biçimi. (varsayılan: `"mp4"`) | COMBO | Evet | `"mp4"` |

### Seedance 2.5 Draft Girdileri

Bu girdiler `Seedance 2.5 Draft` seçildiğinde görünür. Parametre kümesi yukarıdaki Seedance 2.5 ile eşleşir; ancak `resolution` yalnızca `"480p"` sunar (varsayılan `"480p"`).

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 7) | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Seedance 2.0 Fast ve Seedance 2.0 Mini tarafından paylaşılır; her iki model de aynı parametreleri sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 7) | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |

**Not:** `model` seçici dinamiktir; her model bölümünün altında gösterilen girdiler o model seçildiğinde görünür. `prompt`, boşluklar kaldırıldıktan sonra en az 1 karakter uzunluğunda olmalıdır. Çözünürlük ve süre sınırları seçilen modele bağlıdır: Seedance 2.5, 480p/720p/1080p ve 4 ila 30 saniyeyi destekler; Seedance 2.0, 480p/720p/1080p/4k ve 4 ila 15 saniyeyi destekler; Seedance 2.0 Fast ve Seedance 2.0 Mini yalnızca 480p/720p ve 4 ila 15 saniyeyi destekler; Seedance 2.5 Draft yalnızca 480p ve 4 ila 30 saniyeyi destekler. `draft_task_id` çıktısı yalnızca Seedance 2.5 Draft tarafından üretilir; bu nedenle başka herhangi bir modelde bağlantısız bırakılmalıdır, aksi takdirde çalıştırma başarısız olur. `seed` değeri yalnızca düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçları deterministik yapmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video dosyası. | VIDEO |
| `draft_task_id` | Taslak çalıştırmasının görev kimliği. Yalnızca Seedance 2.5 Draft modeli tarafından üretilir; 1080p nihai çıktıyı oluşturmak için ByteDance Seedance 2.5 Draft to Final Video düğümüne bağlayın. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`

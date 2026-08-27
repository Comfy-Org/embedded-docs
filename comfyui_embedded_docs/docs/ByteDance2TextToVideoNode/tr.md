# ByteDance Seedance 2.0 Metinden Videoya

Bu düğüm, ByteDance'ın Seedance 2.5 veya 2.0 modellerini kullanarak bir metin isteminden video oluşturur. İstemi seçilen modele gönderir, videonun işlenmesinin bitmesini bekler ve sonuçtaki video dosyasını döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak Seedance modeli. Seedance 2.5, 30 saniyeye kadar videoları ve mp4/mov çıktısını destekleyen en yeni modeldir; Seedance 2.0 maksimum kalite ve 4k içindir; Seedance 2.0 Fast hız optimizasyonu içindir; Seedance 2.0 Mini en hızlı, en düşük maliyetli oluşturma içindir. Bir model seçmek, istem, çözünürlük, en-boy oranı, süre ve ses oluşturma için ek girdiler ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak belirleyici değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceğini belirler. (varsayılan: False) Bu bir gelişmiş ayardır. | BOOLEAN | Hayır | True / False |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşma satırlarını çift tırnak içine alın. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. (varsayılan: `"720p"`) | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 4 ile 30 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |
| `output_format` | Çıktı videosunun kapsayıcı formatı. (varsayılan: `"mp4"`) | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 7) | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Seedance 2.0 Fast ve Seedance 2.0 Mini tarafından paylaşılır; her iki model de aynı parametreleri sunar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | — |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: `"16:9"`) | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 7) | INT | Evet | 4 ile 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. (varsayılan: True) | BOOLEAN | Evet | True / False |

**Not:** `model` seçici dinamiktir; her model bölümünün altında gösterilen girdiler, o model seçildiğinde görünür. İstem, boşluklar kaldırıldıktan sonra en az 1 karakter uzunluğunda olmalıdır. Çözünürlük ve süre sınırları seçilen modele bağlıdır: Seedance 2.5, 480p/720p/1080p ve 4 ila 30 saniyeyi destekler; Seedance 2.0, 480p/720p/1080p/4k ve 4 ila 15 saniyeyi destekler; Seedance 2.0 Fast ve Seedance 2.0 Mini ise yalnızca 480p/720p ve 4 ila 15 saniyeyi destekler. `seed` değeri yalnızca düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçları belirleyici yapmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `e3b11f5a538d4b9b7e49f651d3939651edfe85000e02e66a8d7700c3389c4b9c`

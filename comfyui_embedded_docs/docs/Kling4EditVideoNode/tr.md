# Kling 4.0 Edit Video

Kling 4.0 modelini kullanarak, isteğe bağlı olarak referans videolar ve referans görsellerle yönlendirilen bir metin istemiyle mevcut bir videoyu düzenler. Sonuç, giriş videosunun uzunluğunu korur. Bir klipte ne olduğunu değiştirmek, stilini yeniden düzenlemek veya özgün zamanlama korunurken öğeleri değiştirmek için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. Yalnızca `"kling-4.0"` kullanılabilir; seçildiğinde aşağıdaki girdiler görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"` |

### kling-4.0 Girdileri

Bu girdiler `model` değeri `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Düzenlenecek video, 3 ila 30 saniye uzunluğunda. Çıktı, bunun uzunluğunu korur. | VIDEO | Evet | 3 ila 30 saniye |
| `reference_videos` | Referans videolar için en fazla 4 adete kadar büyütülebilir yuvalar. İstemde bunlara `@Video2` vb. olarak başvurun. Her video ve tüm videolar birlikte 3 ila 30 saniye uzunluğunda olmalıdır. | AUTOGROW | Hayır | 0 ila 4 video |
| `reference_images` | Referans görseller için en fazla 10 adete kadar büyütülebilir yuvalar. İstemde bunlara `@Image1`, `@Image2` vb. olarak başvurun. | AUTOGROW | Hayır | 0 ila 10 görsel |
| `prompt` | Neyin değiştirileceğinin ve neyin korunacağının açıklaması. Düzenlenen videoya `@Video1`, referans videolara `@Video2` vb. ve görsellere `@Image1` vb. olarak başvurun. | STRING | Evet | 1 ila 26000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en boy oranı. `"adaptive"` giriş videosunun en boy oranını korur. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ila 2147483647 |

**Kısıtlamalar ve davranış:**

* Giriş videosu ve her referans video 3 ila 30 saniye uzunluğunda, en az 700x700 ve en fazla 4553x4553 piksel, toplamda en fazla 8,294,400 piksel olmalı; en boy oranı 2:5 ile 5:2 arasında ve kare hızı en az 24 fps olmalıdır. Tüm videolar birlikte 30 saniyeyi aşmamalıdır.
* Her referans görsel en az 300x300 piksel olmalı ve en boy oranı 2:5 ile 5:2 arasında olmalıdır; en fazla 10 görsel bağlanabilir.
* `@VideoN` veya `@ImageN` ifadesini içeren bir istem, bu türden N'den daha az girdi bağlandığında hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Düzenlenmiş video; görev tamamlandığında sağlayıcıdan indirilir. Giriş videosuyla aynı uzunluğa sahiptir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `00e8de2529df9be6bc1fae5f2c2beda01f151143448e91b79f9cfb27436064ff`

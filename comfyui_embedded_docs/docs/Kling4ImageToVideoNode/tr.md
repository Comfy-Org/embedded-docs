# Kling 4.0 Görüntüden Videoya

Kling 4.0 modeliyle bir dizi ana kareden ses dahil video oluşturur. İlk kare, en fazla sekiz ara kare ve son kare sırayla gönderilir; ara kareler klip boyunca eşit aralıklarla yerleştirilir ve çıktı, ilk ana karenin en-boy oranını alır. Tek bir görüntüyü canlandırmak veya bir çekimi bir dizi kilit an boyunca yönlendirmek için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 4K HDR ve 30 saniyeye kadar destekler; `"kling-4.0-flash"` 720p, 20 saniye ve tek bir ilk kare ile sınırlıdır. Bir model seçildiğinde aşağıda o modelin girdileri görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler `model` değeri `"kling-4.0"` olarak ayarlandığında görünür. Kare girdilerinden en az biri bağlanmalıdır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı isteğe bağlı kare. | IMAGE | Hayır | - |
| `middle_frames` | İlk ve son kare arasındaki kareler için isteğe bağlı, büyütülebilir yuvalar; en fazla 8. Klip boyunca eşit aralıklarla yerleştirilir. | AUTOGROW | Hayır | 0 ile 8 görsel arası |
| `last_frame` | Videonun bittiği isteğe bağlı kare. | IMAGE | Hayır | - |
| `prompt` | Hareketin isteğe bağlı açıklaması. Bağlı karelere ilk kare, ara kareler, son kare sırasıyla `@Image1`, `@Image2` vb. olarak atıfta bulunun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü; adında `HDR` bulunan bir seçenek HDR video döndürür. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 30 arası |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### kling-4.0-flash Girdileri

Bu girdiler `model` değeri `"kling-4.0-flash"` olarak ayarlandığında görünür. Flash tek bir ilk kareyi canlandırır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı kare. | IMAGE | Evet | - |
| `prompt` | Hareketin isteğe bağlı açıklaması. İlk kareye `@Image1` olarak atıfta bulunun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 20 arası |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlar ve davranış:**

* İlk kare, her ara kare ve son kare dahil olmak üzere toplamda en fazla 10 kare bağlanabilir.
* Video, ilk ana karenin en-boy oranını alır; bu nedenle en-boy oranı girdisi gerekmez.
* Her kare en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* `@ImageN` ifadesine değinen bir prompt, N'den az kare bağlandığında hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `289c96204f02fdd378ae7a4dd5a5685ffa4bf7619d098785b9d1ae148fb3ac4a`

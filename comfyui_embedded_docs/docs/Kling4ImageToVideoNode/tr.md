# Kling 4.0 Image to Video

Kling 4.0 modeliyle bir dizi anahtar kareden ses dahil video oluşturur. İlk kare, en fazla sekiz ara kare ve son kare sırayla gönderilir; ara kareler klip boyunca eşit aralıklarla yerleştirilir ve çıktı, ilk anahtar karenin en-boy oranını alır. Tek bir görseli canlandırmak veya bir çekimi bir dizi kilit an boyunca yönlendirmek için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. Yalnızca `"kling-4.0"` kullanılabilir; seçildiğinde aşağıdaki girdileri gösterir. | DYNAMIC_COMBO | Evet | `"kling-4.0"` |

### kling-4.0 Girdileri

Bu girdiler `model` değeri `"kling-4.0"` olarak ayarlandığında görünür. Kare girdilerinden en az biri bağlanmalıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başlayacağı isteğe bağlı kare. | IMAGE | Hayır | - |
| `middle_frames` | İlk ve son kare arasındaki kareler için isteğe bağlı büyütülebilir yuvalar, en fazla 8. Klip boyunca eşit aralıklarla yerleştirilir. | AUTOGROW | Hayır | 0 ila 8 görsel |
| `last_frame` | Videonun sona ereceği isteğe bağlı kare. | IMAGE | Hayır | - |
| `prompt` | Hareketin isteğe bağlı açıklaması. Bağlı karelere ilk kare, ara kareler, son kare sırasıyla `@Image1`, `@Image2` vb. olarak atıfta bulunun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 - 30 |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 - 2147483647 |

**Kısıtlar ve davranış:**

* İlk kare, her ara kare ve son kare sayılarak toplamda en fazla 10 kare bağlanabilir.
* Video, ilk anahtar karenin en-boy oranını alır, bu nedenle en-boy oranı girdisine gerek yoktur.
* Her kare en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* `@ImageN` ifadesinden bahseden bir istem, N'den daha az kare bağlandığında hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `762c350abd4a881b96355a7ce5b9e346d5c3ff22e9f11db820584d02aee12885`

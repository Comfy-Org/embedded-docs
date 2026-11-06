# Kling 4.0 Görüntüden Videoya

Kling 4.0 modeliyle bir dizi anahtar kareden ses dahil video oluşturur. İlk kare, en fazla sekiz orta kare ve son kare sırayla gönderilir, orta kareler klip boyunca eşit aralıklarla yerleştirilir ve çıktı, ilk anahtar karenin en-boy oranını alır. Tek bir görüntüyü canlandırmak veya bir çekimi bir dizi kilit an boyunca yönlendirmek için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 1080p ve 30 saniyeye kadar destekler; `"kling-4.0-flash"` 720p, 20 saniye ve tek bir ilk kare ile sınırlıdır. Bir model seçildiğinde, o modele ait girdiler aşağıda görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler `model` `"kling-4.0"` olarak ayarlandığında görünür. Kare girdilerinden en az biri bağlanmalıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı isteğe bağlı kare. | IMAGE | Hayır | - |
| `middle_frames` | Birinci ve son kare arasındaki kareler için isteğe bağlı, büyütülebilir yuvalar, en fazla 8. Klip boyunca eşit aralıklarla yerleştirilirler. | AUTOGROW | Hayır | 0 ile 8 görsel arası |
| `last_frame` | Videonun bittiği isteğe bağlı kare. | IMAGE | Hayır | - |
| `prompt` | Hareketin isteğe bağlı açıklaması. Bağlı karelere `@Image1`, `@Image2` vb. olarak ilk kare, orta kareler, son kare sırasıyla atıfta bulunun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 30 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### kling-4.0-flash Girdileri

Bu girdiler `model` `"kling-4.0-flash"` olarak ayarlandığında görünür. Flash tek bir ilk kareyi canlandırır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı kare. | IMAGE | Evet | - |
| `prompt` | Hareketin isteğe bağlı açıklaması. İlk kareye `@Image1` olarak atıfta bulunun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 20 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar ve davranış:**

* İlk kare, her orta kare ve son kare dahil olmak üzere toplamda en fazla 10 kare bağlanabilir.
* Video, ilk anahtar karenin en-boy oranını alır, bu nedenle en-boy oranı girdisine gerek yoktur.
* Her kare en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* `@ImageN` ifadesini içeren bir istem, N'den daha az kare bağlandığında hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `248ab33bf7a50afbc08baf1e64e5b1908a38905cda2a87d1303eeeb2755b5a6d`

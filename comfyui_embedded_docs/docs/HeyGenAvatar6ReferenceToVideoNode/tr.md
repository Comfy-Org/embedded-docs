# HeyGen Avatar 6 Reference to Video

HeyGen Avatar 6 ile bir kişiye veya karaktere, referans olarak bir fotoğraf ya da video kullanarak bağladığınız sesi konuşturun. Avatar 6, yüzü ve sahneyi bu referanstan yeniden oluşturur; böylece aynı ses bir sabit fotoğrafı, mevcut bir klibi veya her ikisini de yönlendirebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici; bir model seçildiğinde aşağıda o modelin girdileri görünür. `"heygen-avatar-6-turbo"` daha ucuz ve daha hızlı katmandır. | DYNAMIC_COMBO | Evet | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |

### `heygen-avatar-6` Girdileri

`"heygen-avatar-6-turbo"` aynı sınırlarla aynı girdileri sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Canlandırılacak kişinin veya karakterin isteğe bağlı fotoğrafı. Görünümü ve sahneyi belirler; ilk kare olarak kullanılmaz. | IMAGE | Hayır | Tek görüntü |
| `video` | Animasyonlu veya stilize bir karakterin nasıl konuştuğunu ve hareket ettiğini gösteren isteğe bağlı video. Daha uzun videolar ilk 30 saniyeye kırpılır. | VIDEO | Hayır | 2 ile 30 saniye arası |
| `audio` | Avatar için konuşma. Video uzunluğu sesi takip eder. | AUDIO | Evet | 1.5 saniye ile 10 dakika arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"1080p"`. | COMBO | Evet | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"auto"` görüntünün şeklini veya görüntü bağlı değilken videonun şeklini korur; diğer değerler sahneyi yeniden çerçeveler. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Jestler, mimikler, duruş ve kamera hareketi için isteğe bağlı yönlendirme. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin, en fazla 1200 karakter |
| `motion_expressiveness` | `"less"` daha az ve daha küçük jestler verir. İkisinin çakıştığı yerlerde hareket istemi önceliklidir. Varsayılan: `"default"`. | COMBO | Evet | `"less"`<br>`"default"` |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar ve davranış:**

* Bir görüntü, bir video veya her ikisini bağlayın; hiçbiri yoksa düğüm hata verir.
* Görüntü girdisi tam olarak bir görüntü içermelidir, bir toplu iş değil.
* Gerçekçi insanların referans videoları reddedilir. Animasyonlu veya stilize bir karakterin videosunu kullanın ya da bunun yerine kişinin bir fotoğrafını bağlayın.
* Bir referans video en az 2 saniye uzunluğunda ve en fazla 50 MB boyutunda olmalıdır.
* Fiyatlandırma, çıktı videosunun saniyesi başına yapılır ve modele ve çözünürlüğe bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan konuşan video; oluşturma işlemi bittiğinde HeyGen'den indirilir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6ReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `1a50342827511e355a1d857c34e8bbfc0b74ca7b003dca783b76fcd151413ff8`

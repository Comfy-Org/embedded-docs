# VEED Dubbing

VEED Dubbing, bir videodaki konuşmayı VEED ile başka bir dile çevirir; her konuşmacının sesini klonlar ve dudaklarını çeviriyle senkronize eder. Klip yüklenir, VEED işi sorgulanır ve dublajlı video, yeni ses parçasıyla aynı uzunlukta olacak şekilde 25 fps'de geri döner. Tamamlanmış bir klibi yeniden çekim veya sesi yeniden kaydetme olmadan yerelleştirmek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Dublaj modeli. `"standard"` daha ucuzdur ve mono ses döndürür, Latin Amerika İspanyolcası ve Brezilya Portekizcesi ile; `"pro"` bölgesel aksanlar ve stereo ses ekler. Bir model seçmek `video`, `target_language`, `source_language` ve `seed` girdilerini ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"standard"`<br>`"pro"` |

### standard Girdileri

Bu girdiler `model` `"standard"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Yüzü görünen ve konuşma içeren video, 599 saniyeye kadar. Çıktı, ses parçasıyla aynı uzunluktadır ve 25 fps'de oynatılır. | VIDEO | Evet | 599 saniyeye kadar |
| `target_language` | Dublaj yapılacak dil, 85 dilden biri. (varsayılan: `"English"`) | COMBO | Evet | 85 dil |
| `source_language` | Videoda konuşulan dil veya algılamak için `"auto"`. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>85 dil |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### pro Girdileri

Bu girdiler `model` `"pro"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Yüzü görünen ve konuşma içeren video, 599 saniyeye kadar. Çıktı, ses parçasıyla aynı uzunluktadır ve 25 fps'de oynatılır. | VIDEO | Evet | 599 saniyeye kadar |
| `target_language` | Dublaj yapılacak dil veya bölgesel aksan: 87 dil artı `"English (UK)"`, `"Spanish (Mexico)"` ve `"Portuguese (Brazil)"` gibi 14 aksan. (varsayılan: `"English (US)"`) | COMBO | Evet | 101 seçenek |
| `source_language` | Videoda konuşulan dil veya algılamak için `"auto"`. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>91 dil |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

Video ses parçası içermediğinde, klip 599 saniyeden uzun olduğunda veya VEED işi başarısız olduğunda düğüm bir hatayla durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Dublajlı video: çevrilmiş konuşma ve eşleştirilmiş dudak hareketiyle orijinal görüntü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/tr.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`

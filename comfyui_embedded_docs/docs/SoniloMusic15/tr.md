# Sonilo Music 1.5

Sonilo Music 1.5 düğümü, bir metin isteminden vokal içeren eksiksiz bir şarkı üretir. Tür, ruh hali, enstrümanlar ve vokalleri tanımlayın; isteğe bağlı olarak kendi şarkı sözlerinizi de sağlayabilirsiniz; düğüm isteği Sonilo hizmetine gönderir ve tamamlanmış parçayı ses olarak döndürür. Enstrümantal bir klibe değil, tam bir şarkıya ihtiyaç duyduğunuzda kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Şarkının açıklaması: tür, ruh hali, enstrümanlar ve vokaller. Sözleri kendiniz belirlemek için `[Verse]` ve `[Chorus]` etiketleri içeren bir `Lyrics:` bloğu ekleyin; bu blok olmadan model kendi şarkı sözlerini yazar. Boşluklar kırpıldıktan sonra 1 ile 2000 karakter arasında olmalıdır. | STRING | Evet | 1 ile 2000 karakter arası |
| `duration` | `auto`, şarkı uzunluğunu şarkı sözlerine uydurur. `custom`, `seconds` değerini kullanır; sığmayan şarkı sözlerini keser ve kısa olanları yineler. | DYNAMIC_COMBO | Evet | `"auto"`<br>`"custom"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 18446744073709551615 arası |

### Özel Süre Parametreleri (`duration` değeri `"custom"` olduğunda)

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Oluşturulan şarkının saniye cinsinden uzunluğu (varsayılan: 60). | INT | Evet | 10 ile 360 arası |

**Not:** `prompt` girdisi zorunludur ve boş olmamalıdır. Düğüm, boşluklar kırpıldıktan sonra en az 1 karakter ve en fazla 2000 karakter içerdiğini doğrular.

**Not:** Kullanım, istenen sürenin saniyesi başına $0.0032175 olarak ücretlendirilir ve `custom` seçildiğinde fiyat rozeti `duration.seconds` değerini takip eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Oluşturulan şarkı, vokaller dahil, ses dosyası olarak. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloMusic15/tr.md)

---
**Source fingerprint (SHA-256):** `65ccf74ccdfa7a710d8c7bd9871e666d79ceadc7304644fe0101956832ca6024`

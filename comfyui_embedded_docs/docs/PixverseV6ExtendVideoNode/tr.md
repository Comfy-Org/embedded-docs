# PixVerse V6 Videoyu Uzat

Bu düğüm, PixVerse V6 modelini kullanarak mevcut bir videoyu devam ettirir ve devam videosuyla birlikte isteğe bağlı olarak yerel bir ses parçası oluşturur. Kaynak video 40 saniyeden kısa olmalı ve her iki kenarda da 1920 pikselden büyük olmamalıdır. Çıktı, kaynak videonun çözünürlüğünü korur; bu nedenle kalite ayarı kare boyutundan ziyade devam videosunun ne kadar iyi işlendiğini kontrol eder.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Devam ettirilecek video. | VIDEO | Evet | 40 saniyeden kısa; en fazla 1920 piksel genişlik ve yükseklik |
| `model` | Model ve üretim ayarları. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videonun nasıl devam etmesi gerektiğini açıklayan istem. (varsayılan: boş) | STRING | Evet | 1–5000 karakter |
| `quality` | Oluşturulan devam videosunun işleme kalitesi: 1080p, 540p veya 360p'den belirgin şekilde daha iyi görünür. Asla yeniden boyutlandırmaz - çıktı, kaynak videonun çözünürlüğünü korur. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu. (varsayılan: 5) | INT | Evet | 1–15 |
| `generate_audio` | Video ile birlikte yerel bir ses parçası oluşturun. (varsayılan: true) | BOOLEAN | Evet | true / false |
| `seed` | Video üretimi için tohum. PixVerse bunu kaydeder ancak bu değerden bir çalıştırmayı yeniden üretmez. (varsayılan: 42) | INT | Evet | 0–2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: boş) | STRING | Hayır | En fazla 2048 karakter |
| `style` | Videonun tamamına uygulanan isteğe bağlı görsel stil. (varsayılan: "none") | COMBO | Hayır | Birden çok seçenek mevcuttur; "none" varsayılandır |

**Not:** Kaynak `video` 40 saniyeden kısa olmalı ve hem genişlik hem de yükseklik açısından en fazla 1920 piksel olmalıdır; daha uzun veya daha büyük videolar reddedilir. Oluşturulan çıktı, kaynak videonun çözünürlüğünü korur; bu nedenle `quality`, çıktı kare boyutunu değil, işleme kalitesini değiştirir. `prompt` zorunludur ve boşluklar temizlendikten sonra 1 ile 5000 karakter arasında olmalıdır. `negative_prompt` sağlandığında 2048 karakterle sınırlıdır. `seed`, PixVerse tarafından kaydedilir ancak aynı çalıştırmayı yeniden üretmek için kullanılamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Kaynak videoyla aynı çözünürlükte, oluşturulan devam videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`

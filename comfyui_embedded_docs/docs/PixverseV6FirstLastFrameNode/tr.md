# PixVerse V6 İlk ve Son Kareden Videoya

PixVerse V6 First-Last-Frame to Video, PixVerse kullanarak ilk kareden son kareye geçiş yapan bir video oluşturur; isteğe bağlı olarak yerleşik ses içerir. Verilen iki görsel, PixVerse API'sine gönderilir; API geçiş videosunu üretir ve bunu bir video dosyası olarak döndürür. Çıktı, ilk karenin en-boy oranını korur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başlangıç görseli. | IMAGE | Evet | — |
| `last_frame` | Videonun bitiş görseli. | IMAGE | Evet | — |
| `model` | Model ve üretim ayarları. PixVerse modelini seçer ve üretim parametrelerini gösterir. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Geçişi tanımlayan istem. | STRING | Evet | En fazla 5000 karakter |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (varsayılan: 720p) | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu. (varsayılan: 5) | INT | Evet | 1 ile 15 |
| `generate_audio` | Video ile birlikte yerleşik bir ses parçası oluşturur. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `seed` | Video üretimi için seed. PixVerse bunu kaydeder ancak bu değerden bir çalıştırmayı yeniden üretmez. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelere ilişkin isteğe bağlı bir metin açıklaması. | STRING | Hayır | En fazla 2048 karakter |
| `style` | Videonun tamamına uygulanan isteğe bağlı bir görsel stil. (varsayılan: none) | COMBO | Hayır | Birden fazla seçenek mevcuttur (varsayılan: "none") |

Not: İstem, boşluk karakterleri çıkarıldıktan sonra boş olmamalıdır ve 5000 karakterle sınırlıdır. Negatif istem sağlandığında 2048 karakterle sınırlıdır. Süre 1 ile 15 saniye arasında olmalıdır. Çıktı videosu ilk karenin en-boy oranını korur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | İlk kareden son kareye geçiş yapan, `generate_audio` etkinleştirildiğinde bir ses parçası da içeren oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`

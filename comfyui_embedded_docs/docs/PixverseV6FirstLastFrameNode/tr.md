# PixVerse V6 İlk ve Son Kareden Videoya

PixVerse V6 İlk-Son Kare'den Videoya, PixVerse kullanarak isteğe bağlı yerel ses ile bir ilk kareden son kareye geçiş yapan bir video üretir. Sağlanan iki görsel PixVerse API'sine gönderilir; API geçiş videosunu üretir ve video dosyası olarak döndürür. Çıktı, ilk karenin en boy oranını korur.

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
| `prompt` | Geçişi açıklayan istem. | STRING | Evet | En fazla 5000 karakter |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (varsayılan: 720p) | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Üretilen videonun saniye cinsinden uzunluğu. (varsayılan: 5) | INT | Evet | 1 - 15 |
| `generate_audio` | Video ile birlikte yerel bir ses parçası üret. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `seed` | Video üretimi için seed. PixVerse bunu kaydeder ancak bundan bir çalıştırmayı yeniden üretmez. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması. | STRING | Hayır | En fazla 2048 karakter |
| `style` | Tüm videoya uygulanan isteğe bağlı görsel stil. (varsayılan: none) | COMBO | Hayır | Birden çok seçenek mevcut (varsayılan: "none") |

Not: İstem, boşluklar kaldırıldıktan sonra boş olmamalıdır ve 5000 karakterle sınırlıdır. Negatif istem sağlandığında 2048 karakterle sınırlıdır. Süre 1 ile 15 saniye arasında olmalıdır. Çıktı videosu ilk karenin en boy oranını korur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | İlk kareden son kareye geçiş yapan, `generate_audio` etkinleştirildiğinde bir ses parçası içeren üretilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`

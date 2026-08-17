# WEBM Kaydet

SaveWEBM düğümü, bir görüntü dizisini WEBM video dosyası olarak kaydeder. Girdi görüntülerini, yapılandırılabilir kare hızı ve kalite ayarlarıyla VP9 veya AV1 codec bileşenini kullanarak videoya kodlar ve dosyayı çıktı dizinine kaydeder. Kullanılabilir olduğunda, prompt ve iş akışı meta verileri video dosyasına gömülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Videoya kodlanacak görüntü dizisi. RGBA görüntüleri, alfa kanalları saydamlık olarak kaydedilir (yalnızca vp9 codec bileşeni). | IMAGE | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek; bir sayaç ve .webm uzantısı otomatik olarak eklenir (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `codec` | Kodlama için kullanılan video codec bileşeni | COMBO | Evet | "vp9"<br>"av1" |
| `fps` | Çıktı videosunun kare hızı (varsayılan: 24.0) | FLOAT | Hayır | 0.01-1000.0 |
| `crf` | Daha yüksek crf değeri, daha düşük kalite ve daha küçük dosya boyutu anlamına gelir; daha düşük crf değeri, daha yüksek kalite ve daha yüksek dosya boyutu anlamına gelir (varsayılan: 32.0) | FLOAT | Hayır | 0-63.0 |

**Alfa kanalı notu:** RGBA görüntülerinin alfa kanalı yalnızca vp9 codec bileşeni kullanıldığında korunur. av1 codec bileşeni kullanıldığında alfa kanalı yok sayılır ve yalnızca RGB verisi kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Girdi görüntü dizisi, değiştirilmeden aktarılır | IMAGE |
| `ui` | Kaydedilen WEBM dosyasını gösteren video önizlemesi | PREVIEW |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/tr.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`

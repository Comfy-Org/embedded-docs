# WEBM Kaydet

SaveWEBM düğümü, bir görüntü dizisini WEBM video dosyası olarak kaydeder. Birden çok giriş görüntüsü alır ve bunları yapılandırılabilir kalite ayarları ve kare hızıyla VP9 veya AV1 kodeğini kullanarak bir videoya kodlar. Ortaya çıkan video dosyası, prompt bilgilerini içeren meta verilerle birlikte çıktı dizinine kaydedilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | RGBA görüntüleri, alfa kanalı saydamlık olarak korunarak kaydedilir (yalnızca vp9 kodeği). | IMAGE | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adı için önek (varsayılan: "ComfyUI"). | STRING | Hayır | - |
| `codec` | Kodlama için kullanılacak video kodeği. | COMBO | Evet | "vp9"<br>"av1" |
| `fps` | Çıktı videosu için kare hızı (varsayılan: 24.0). | FLOAT | Hayır | 0.01-1000.0 |
| `crf` | Daha yüksek crf, daha küçük dosya boyutuyla daha düşük kalite anlamına gelir; daha düşük crf, daha büyük dosya boyutuyla daha yüksek kalite anlamına gelir (varsayılan: 32.0). | FLOAT | Hayır | 0-63.0 |

**Alfa kanalı hakkında not:** RGBA görüntülerindeki alfa kanalı yalnızca VP9 kodeği kullanılırken korunur. AV1 kodeği kullanılırken alfa kanalı yok sayılır ve yalnızca RGB verisi kodlanır.

**Dosya adlandırma hakkında not:** Videolar çıktı dizinine `{filename_prefix}_{counter:05}_.webm` olarak kaydedilir; sayaç, mevcut dosyaların üzerine yazılmasını önlemek için otomatik olarak artar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `images` | Video kaydedildikten sonra değiştirilmeden iletilen giriş görüntüleri. | IMAGE |
| UI preview | Kaydedilen WEBM dosyasını gösteren video önizlemesi. | PREVIEW |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/tr.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`

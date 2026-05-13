> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/tr.md)

SaveWEBM düğümü, bir dizi görüntüyü WEBM video dosyası olarak kaydeder. Birden fazla giriş görüntüsünü alır ve bunları VP9 veya AV1 codec bileşeni ile yapılandırılabilir kalite ayarları ve kare hızı kullanarak bir videoya kodlar. Ortaya çıkan video dosyası, bilgi istemi bilgilerini içeren meta verilerle birlikte çıktı dizinine kaydedilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntüler` | IMAGE | Evet | - | Video kareleri olarak kodlanacak giriş görüntüleri dizisi |
| `dosyaadı_öneki` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "ComfyUI") |
| `codec` | COMBO | Evet | "vp9"<br>"av1" | Kodlama için kullanılacak video codec bileşeni |
| `fps` | FLOAT | Hayır | 0,01-1000,0 | Çıktı videosu için kare hızı (varsayılan: 24,0) |
| `crf` | FLOAT | Hayır | 0-63,0 | Kalite ayarı; daha yüksek crf, daha küçük dosya boyutuyla daha düşük kalite, daha düşük crf ise daha büyük dosya boyutuyla daha yüksek kalite anlamına gelir (varsayılan: 32,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | PREVIEW | Kaydedilen WEBM dosyasını gösteren video önizlemesi |

---
**Source fingerprint (SHA-256):** `761ce5148c273ffe3789be75c2a00268241d3ec7ecebd5b10efd1b1cc98d85ea`

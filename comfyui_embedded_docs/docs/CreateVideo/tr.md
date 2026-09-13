# Video Oluştur

Create Video düğümü, bir görüntü dizisini videoda birleştirir. Oynatma hızını saniyedeki kare sayısı olarak ayarlayabilir, isteğe bağlı olarak ses ekleyebilir ve ortaya çıkan videonun sıkıştırma biçimini, bit derinliğini ve renk uzayını seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Video oluşturmak için kullanılacak görüntüler. | IMAGE | Evet | - |
| `fps` | Video oynatma hızı için saniyedeki kare sayısı (varsayılan: 30.0). | FLOAT | Evet | 1.0 - 120.0 |
| `audio` | Videoya eklenecek ses. | AUDIO | Hayır | - |
| `bit_depth` | Auto, sRGB için 8-bit, HDR ve HDR PQ için 10-bit kullanır. Açık 8-bit ve 10-bit seçimleri renk uzayından bağımsızdır. (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>8<br>10 |
| `color_space` | Girdi görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi seçer ve HDR PQ, BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Hayır | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `codec` | Videoyu isteğe bağlı olarak hemen kodlayın. None, görüntüleri tensör biçiminde tutar; Auto, H.264 kullanır. (varsayılan: "none") | COMBO | Hayır | `"none"`<br>Video kodek listesinden kullanılabilir video kodek seçenekleri (örn. `"auto"` ve desteklenen diğer kodekler) |

Not: `bit_depth` `"auto"` olarak ayarlandığında, düğüm HDR ve HDR PQ renk uzayları için otomatik olarak 10-bit, sRGB için 8-bit kullanır.

Not: `codec` parametresi gelişmiş bir seçenektir. `"none"` olarak bırakıldığında çıktı tensör biçiminde kalır; başka bir kodek seçildiğinde video hemen kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi görüntülerini ve isteğe bağlı sesi içeren oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

---
**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`

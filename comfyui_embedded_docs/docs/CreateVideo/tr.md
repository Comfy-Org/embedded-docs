# Video Oluştur

Create Video düğümü, bir görüntü dizisini videoda birleştirir. Oynatma hızını saniyedeki kare sayısı olarak ayarlayabilir, isteğe bağlı olarak ses ekleyebilir ve ortaya çıkan videonun sıkıştırma biçimini, bit derinliğini ve renk uzayını seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Video oluşturmak için kullanılacak görüntüler. | IMAGE | Evet | - |
| `fps` | Video oynatma hızı için saniyedeki kare sayısı (varsayılan: 30.0). | FLOAT | Evet | 1.0 - 120.0 |
| `ses` | Videoya eklenecek ses. | AUDIO | Hayır | - |
| `bit_depth` | Auto, sRGB için 8-bit, HDR ve HDR PQ için 10-bit kullanır. Açık 8-bit ve 10-bit seçimleri renk uzayından bağımsızdır. (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>8<br>10 |
| `color_space` | Girdi görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi seçer ve HDR PQ, BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Hayır | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `chroma_subsampling` | 444 tam renk çözünürlüğünü korur, 422 yatay renk çözünürlüğünü yarıya indirir ve 420 her iki ekseni de yarıya indirir. "auto" kodeğin varsayılanını kullanır. Desteklenmeyen seçenekler desteklenen en yakın modu kullanır ve konsola bir uyarı yazdırır. (varsayılan: "auto") none seçimi kodlayıcıya bırakır. | COMBO | Hayır | `"auto"`<br>`"444"`<br>`"422"`<br>`"420"`<br>`"none"` |
| `codec` | Videoyu isteğe bağlı olarak hemen kodlayın. None, görüntüleri tensör biçiminde tutar; Auto, H.264 kullanır. (varsayılan: "none") | COMBO | Hayır | `"none"`<br>Video kodek listesinden kullanılabilir video kodek seçenekleri (örn. `"auto"` ve desteklenen diğer kodekler) |

Not: `bit_depth` `"auto"` olarak ayarlandığında, düğüm HDR ve HDR PQ renk uzayları için otomatik olarak 10-bit, sRGB için 8-bit kullanır.

Not: `codec` parametresi gelişmiş bir seçenektir. `"none"` olarak bırakıldığında çıktı tensör biçiminde kalır; başka bir kodek seçildiğinde video hemen kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi görüntülerini ve isteğe bağlı sesi içeren oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e36be7cefdd794a39aa9e8806c89701d5b27bb8d49e856ae38af59eb43fbee48`

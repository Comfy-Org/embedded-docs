# Video Oluştur

Create Video düğümü, bir dizi görüntüden bir video dosyası oluşturur. Saniyedeki kare sayısı (fps) cinsinden oynatma hızını ayarlayabilir, isteğe bağlı olarak ses ekleyebilir ve elde edilen videonun bit derinliğini ve renk uzayını seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Video oluşturmak için kullanılan görüntüler. | IMAGE | Evet | - |
| `fps` | Video oynatma hızı için saniyedeki kare sayısı (varsayılan: 30.0). | FLOAT | Evet | 1.0 - 120.0 |
| `ses` | Videoya eklenecek ses. | AUDIO | Hayır | - |
| `bit_depth` | Otomatik, sRGB için 8-bit ve HDR için 10-bit kullanır. Açık 8-bit ve 10-bit seçimleri renk uzayından bağımsızdır. (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>8<br>10 |
| `color_space` | Giriş görüntülerinin renk uzayı. HDR, BT.2020/HLG'yi; HDR PQ ise BT.2020/PQ'yu seçer. (varsayılan: "sRGB") | COMBO | Hayır | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Not: `bit_depth` "auto" olarak ayarlandığında düğüm, HDR ve HDR PQ renk uzayları için 10-bit, sRGB için 8-bit kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Giriş görüntülerini ve isteğe bağlı sesi içeren oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

---
**Source fingerprint (SHA-256):** `2fa73f38b0609de4159e557b6abe73652c5bebab9d34ffdda743b0eac6049f13`

# Beeble SwitchX Video Düzenleme

Beeble SwitchX ile bir videoyu düzenleyin. Bu düğüm, orijinal nesnenin piksellerini ve hareketini korurken sahnedeki her şeyi (arka plan, aydınlatma, kostüm) değiştirebilir. Yeni görünümü tanımlamak için bir referans görseli ve/veya metin istemi sağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Düzenlenecek giriş videosu. Maksimum 240 kare, kare başına maksimum ~2,77 megapiksel. | VIDEO | Evet | Yok |
| `istem` | Sahne için istenen yeni görünümün metin açıklaması. | STRING | Evet | Yok |
| `alfa_modu` | Alfa mat modu. "fill" modunda ayrı bir mat yoktur ve tüm kare doldurulur. "select" modu, düzenlenecek alanı tanımlamak için tek bir ana kare görseli kullanır. "custom" modu, düzenlenecek alanı kare kare tanımlamak için tam bir alfa videosu kullanır. | COMBO | Evet | `"fill"`<br>`"select"`<br>`"custom"` |
| `maksimum_çözünürlük` | Çıktı videosu için maksimum çözünürlük (varsayılan: "1080p"). | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `tohum` | Tekrarlanabilirlik için tohum değeri. Aynı girdilerle aynı tohumu kullanmak aynı sonucu üretir. | INT | Evet | 0 ile 2147483647 |
| `referans_görsel` | Sahne için istenen yeni görünümü tanımlayan isteğe bağlı bir referans görseli. | IMAGE | Hayır | Yok |

### Alfa Modu Detayları

`alpha_mode` parametresi, videonun hangi bölümlerinin düzenleneceğini kontrol eder:

- **fill**: Video karesinin tamamı düzenlenir. Ayrı bir alfa mat üretilmez.
- **select**: Düzenlenecek alanı tanımlayan tek bir ana kare görseli sağlarsınız. Düğüm, videonun hangi bölümlerinin değiştirileceğini belirlemek için bunu kullanır.
- **custom**: Düzenlenecek alanı kare kare tanımlayan tam bir alfa videosu sağlarsınız. Bu, her karenin hangi bölümlerinin düzenleneceği üzerinde hassas kontrol sağlar.

`select` modunu kullanırken `alpha_keyframe` görselini sağlamanız gerekir. `custom` modunu kullanırken `alpha_mask` videosunu sağlamanız gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `alfa` | Sahne değişikliklerinin uygulandığı düzenlenmiş video. | VIDEO |
| `alpha` | Beeble tarafından kullanılan alfa mat. Ayrı bir matı olmayan "fill" modu için bu boştur. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/tr.md)

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`

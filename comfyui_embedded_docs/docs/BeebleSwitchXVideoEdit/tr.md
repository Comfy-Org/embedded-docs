> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/tr.md)

# Beeble SwitchX Video Düzenleme

Beeble SwitchX ile bir videoyu düzenleyin. Bu düğüm, orijinal nesnenin piksellerini ve hareketini korurken sahnedeki her şeyi (arka plan, aydınlatma, kostüm) değiştirebilir. Yeni görünümü tanımlamak için bir referans görseli ve/veya metin istemi sağlayın.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `video` | VIDEO | Evet | Yok | Düzenlenecek giriş videosu. Maksimum 240 kare, kare başına maksimum ~2,77 megapiksel. |
| `istem` | STRING | Evet | Yok | Sahne için istenen yeni görünümün metin açıklaması. |
| `alfa_modu` | COMBO | Evet | `"fill"`<br>`"select"`<br>`"custom"` | Alfa mat modu. "fill" modunda ayrı bir mat yoktur ve tüm kare doldurulur. "select" modu, düzenlenecek alanı tanımlamak için tek bir ana kare görseli kullanır. "custom" modu, düzenlenecek alanı kare kare tanımlamak için tam bir alfa videosu kullanır. |
| `maksimum_çözünürlük` | COMBO | Evet | `"720p"`<br>`"1080p"` | Çıktı videosu için maksimum çözünürlük (varsayılan: "1080p"). |
| `tohum` | INT | Evet | 0 ile 2147483647 | Tekrarlanabilirlik için tohum değeri. Aynı girdilerle aynı tohumu kullanmak aynı sonucu üretir. |
| `referans_görsel` | IMAGE | Hayır | Yok | Sahne için istenen yeni görünümü tanımlayan isteğe bağlı bir referans görseli. |

### Alfa Modu Detayları

`alpha_mode` parametresi, videonun hangi bölümlerinin düzenleneceğini kontrol eder:

- **fill**: Video karesinin tamamı düzenlenir. Ayrı bir alfa mat üretilmez.
- **select**: Düzenlenecek alanı tanımlayan tek bir ana kare görseli sağlarsınız. Düğüm, videonun hangi bölümlerinin değiştirileceğini belirlemek için bunu kullanır.
- **custom**: Düzenlenecek alanı kare kare tanımlayan tam bir alfa videosu sağlarsınız. Bu, her karenin hangi bölümlerinin düzenleneceği üzerinde hassas kontrol sağlar.

`select` modunu kullanırken `alpha_keyframe` görselini sağlamanız gerekir. `custom` modunu kullanırken `alpha_mask` videosunu sağlamanız gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `alfa` | VIDEO | Sahne değişikliklerinin uygulandığı düzenlenmiş video. |
| `alpha` | VIDEO | Beeble tarafından kullanılan alfa mat. Ayrı bir matı olmayan "fill" modu için bu boştur. |

---
**Source fingerprint (SHA-256):** `e2d67b037863f024f42c97943ec0d2daf32b547b232a7dfedd6de398f4b7ba28`

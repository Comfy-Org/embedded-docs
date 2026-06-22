# Beeble SwitchX Görüntü Düzenleme

## Genel Bakış

Beeble SwitchX ile tek bir görseli düzenleyin. Bu düğüm, orijinal nesnenin piksellerini korurken sahnedeki her şeyi (arka plan, aydınlatma, kostüm) değiştirebilir. Yeni görünümü tanımlamak için bir referans görseli ve/veya metin istemi sağlayın. Maksimum çözünürlük yaklaşık 2,77 megapikseldir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Düzenlenecek kaynak görsel. | IMAGE | Evet | - |
| `istem` | İstenen yeni görünümün metin açıklaması (örneğin, "zırhlı bir şövalye"). | STRING | Evet | - |
| `alfa_modu` | Alfa matının nasıl işleneceği. "select" nesneyi seçmek için bir ana kare kullanır, "fill" ayrı bir mat olmadan tüm görseli değiştirir, "custom" kullanıcı tarafından sağlanan bir maske kullanır. | COMBO | Evet | `"select"`<br>`"fill"`<br>`"custom"` |
| `maksimum_çözünürlük` | Çıktı görseli için maksimum çözünürlük. Daha yüksek çözünürlük daha fazla kredi harcar. | COMBO | Evet | `"1080p"`<br>`"720p"` |
| `tohum` | Tekrarlanabilirlik için bir tohum değeri. | INT | Evet | - |
| `referans_görsel` | Yeni sahne öğelerinin stilini veya görünümünü yönlendirmek için isteğe bağlı bir referans görseli. | IMAGE | Hayır | - |

**`alpha_mode` hakkında not:** `alpha_mode` `"select"` olarak ayarlandığında, ayrıca bir `alpha_keyframe` (nesneyi seçmek için kullanılan bir ana kare görseli) sağlamanız gerekir. `"custom"` olarak ayarlandığında, bir `alpha_mask` (kullanıcı tarafından oluşturulmuş bir maske) sağlamanız gerekir. `"fill"` olarak ayarlandığında, alfa girdisi gerekmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `alfa` | Sahne öğeleri değiştirilmiş düzenlenmiş görsel. | IMAGE |
| `alpha` | Beeble tarafından kullanılan alfa matı. Ayrı bir matı olmayan "fill" modu için boştur. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`

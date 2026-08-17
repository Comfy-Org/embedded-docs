# HiDream-O1 Referans Görselleri

## Genel Bakış

Referans görsellerini hem pozitif hem negatif koşullandırmaya ekleyin. Bu düğüm, görüntü oluşturma sürecini yönlendirmek için bir veya daha fazla referans görseli sağlamanıza olanak tanır; bir talimata dayalı düzenleme veya konu odaklı kişiselleştirme için.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Referans görsellerin ekleneceği pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negative` | Referans görsellerin ekleneceği negatif koşullandırma. | CONDITIONING | Evet | - |
| `images` | Referans görseller. 1 görsel = talimat düzenleme; 2-10 görsel = çoklu referans. | IMAGE | Evet | 1 ila 10 görsel |

**`images` parametresi hakkında not:** Bu, 1 ila 10 görsel kabul eden otomatik büyüyen bir girdidir. Görseller `image_1` ile `image_10` arasında etiketlenir. En az 1 görsel sağlamalısınız. Görsel sayısı çalışma modunu belirler: tek bir görsel düzenleme talimatları için kullanılırken, birden fazla görsel (2-10) konu odaklı kişiselleştirme için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Referans görsellerin eklendiği pozitif koşullandırma. | CONDITIONING |
| `negative` | Referans görsellerin eklendiği negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/tr.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`

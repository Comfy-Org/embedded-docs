# HiDream-O1 Referans Görselleri

## Genel Bakış

Referans görüntülerini hem pozitif hem negatif koşullamaya ekleyin. Bu düğüm, 1 ila 10 referans görüntüsü sağlamanıza olanak tanır; tek bir görüntü talimat tabanlı düzenleme için kullanılırken, birden fazla görüntü (2-10) özne odaklı kişiselleştirmeyi etkinleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Referans görüntülerin ekleneceği pozitif koşullama. | CONDITIONING | Evet | - |
| `negatif` | Referans görüntülerin ekleneceği negatif koşullama. | CONDITIONING | Evet | - |
| `görseller` | Referans görüntüleri. 1 görüntü = talimat düzenleme; 2-10 görüntü = çoklu referans. | IMAGE | Evet | 1 ile 10 images |

**`images` parametresi hakkında not:** Bu, 1 ila 10 görüntü kabul eden otomatik büyüyen (autogrow) bir girdidir. Görüntüler `image_1` ile `image_10` arasında etiketlenir. En az 1 görüntü sağlamalısınız. Görüntü sayısı çalışma modunu belirler: tek bir görüntü düzenleme talimatları için kullanılırken, birden fazla görüntü (2-10) özne odaklı kişiselleştirme için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Referans görüntülerin eklendiği pozitif koşullama. | CONDITIONING |
| `negatif` | Referans görüntülerin eklendiği negatif koşullama. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/tr.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`

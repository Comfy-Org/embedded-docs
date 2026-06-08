Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/en.md)

Bu düğüm, birden fazla ana kare arasında geçişler oluşturarak bir video üretir. Bir başlangıç görüntüsünden başlar ve kullanıcı tarafından tanımlanan bir dizi bitiş görüntüsü ve istemi aracılığıyla animasyon yaparak çıktı olarak tek bir video dosyası üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak Vidu modeli. | COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `başlangıç_görüntüsü` | Başlangıç karesi görüntüsü. En-boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Evet | - |
| `seed` | Tekrarlanabilir sonuçlar elde etmek için rastgele sayı üretiminde kullanılan tohum değeri (varsayılan: 1). | INT | Hayır | 0 ile 2147483647 |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `kareler` | Ana kare geçiş sayısı (2-9). Bir değer seçmek, her kare için gerekli girdileri dinamik olarak ortaya çıkarır. | DYNAMICCOMBO | Evet | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |

**Kare Girdileri (Dinamik Olarak Görüntülenir):**
`frames` için bir değer seçtiğinizde (örneğin, "3"), düğüm her geçiş için karşılık gelen bir dizi zorunlu girdi gösterecektir. Seçilen sayıya kadar olan her `i` karesi için aşağıdakileri sağlamanız gerekir:

* `end_image{i}` (IMAGE): Bu geçiş için hedef görüntü. En-boy oranı 1:4 ile 4:1 arasında olmalıdır.
* `prompt{i}` (STRING): Bu kareye geçişi yönlendiren bir metin açıklaması (maksimum 2000 karakter).
* `duration{i}` (INT): Bu belirli geçiş bölümü için saniye cinsinden süre.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm animasyonlu geçişleri içeren oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `02ddbb1e041b6d9e6654ab6c3cc25f4c2e5bc1545d84a30624608edc85e51f96`

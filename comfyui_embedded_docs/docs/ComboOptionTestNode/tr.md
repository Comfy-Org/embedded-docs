# ComboOptionTestNode

ComboOptionTestNode, açılır kutu seçimlerini test etmek ve iletmek için tasarlanmış bir mantık düğümüdür. Her biri önceden tanımlanmış bir seçenek kümesine sahip iki açılır kutu girişi alır ve seçilen değerleri değişiklik yapmadan doğrudan çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Üç test seçeneğinden oluşan bir kümeden ilk seçim. | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | Üç test seçeneğinden oluşan farklı bir kümeden ikinci seçim. | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_1` | İlk açılır kutudan (`combo`) seçilen değeri çıktı olarak verir. | COMBO |
| `output_2` | İkinci açılır kutudan (`combo2`) seçilen değeri çıktı olarak verir. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`

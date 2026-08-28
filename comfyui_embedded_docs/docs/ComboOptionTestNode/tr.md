# ComboOptionTestNode

ComboOptionTestNode, açılır kutu seçimlerini test etmek ve geçirmek için tasarlanmış bir mantık düğümüdür. Her biri önceden tanımlanmış bir dizi seçeneğe sahip iki açılır kutu girdisi alır ve seçilen değerleri doğrudan değişiklik yapmadan çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Üç test seçeneğinden oluşan bir kümeden yapılan ilk seçim. | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | Üç test seçeneğinden oluşan farklı bir kümeden yapılan ikinci seçim. | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `output_1` | İlk açılır kutudan (`combo`) seçilen değeri çıktı olarak verir. | COMBO |
| `output_2` | İkinci açılır kutudan (`combo2`) seçilen değeri çıktı olarak verir. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`

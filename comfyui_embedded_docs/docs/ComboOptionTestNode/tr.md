# ComboOptionTestNode

Bu düğüm, iki açılır kutu seçimini alır ve bunları değiştirmeden doğrudan çıktılarına aktarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | İlk seçim; üç test seçeneğinden oluşan bir kümeden seçilir. | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | İkinci seçim; üç test seçeneğinden oluşan farklı bir kümeden seçilir. | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_1` | İlk açılır kutuda (`combo`) seçilen değeri değiştirmeden döndürür. | COMBO |
| `output_2` | İkinci açılır kutuda (`combo2`) seçilen değeri değiştirmeden döndürür. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`

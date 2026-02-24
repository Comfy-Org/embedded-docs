> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

ComboOptionTestNode, açılır liste seçimlerini test etmek ve iletmek için tasarlanmış bir mantık düğümüdür. Önceden tanımlanmış seçenek setlerine sahip iki açılır liste girişi alır ve seçilen değerleri değiştirmeden doğrudan çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` | Üç test seçeneğinden oluşan bir setten yapılan ilk seçim. |
| `combo2` | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` | Farklı bir üç test seçeneği setinden yapılan ikinci seçim. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_1` | COMBO | İlk açılır listeden (`combo`) seçilen değeri çıktı olarak verir. |
| `output_2` | COMBO | İkinci açılır listeden (`combo2`) seçilen değeri çıktı olarak verir. |

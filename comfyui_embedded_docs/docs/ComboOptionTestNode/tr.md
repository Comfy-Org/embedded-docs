# ComboOptionTestNode

## Genel Bakış

ComboOptionTestNode, birleşik giriş kutusu seçimlerini test etmek ve iletmek için tasarlanmış bir mantık düğümüdür. Her biri önceden tanımlanmış seçenekler içeren iki birleşik giriş kutusu alır ve seçilen değerleri herhangi bir değişiklik yapmadan doğrudan çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `combo` | Üç test seçeneğinden oluşan ilk kümeden yapılan seçim. | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | Farklı üç test seçeneğinden oluşan ikinci kümeden yapılan seçim. | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_1` | İlk birleşik giriş kutusundan (`combo`) seçilen değeri çıktı olarak verir. | COMBO |
| `output_2` | İkinci birleşik giriş kutusundan (`combo2`) seçilen değeri çıktı olarak verir. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`

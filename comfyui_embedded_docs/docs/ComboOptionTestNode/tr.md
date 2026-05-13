> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/tr.md)

## Genel Bakış

ComboOptionTestNode, birleşik giriş kutusu seçimlerini test etmek ve iletmek için tasarlanmış bir mantık düğümüdür. Her biri önceden tanımlanmış seçenekler içeren iki birleşik giriş kutusu alır ve seçilen değerleri herhangi bir değişiklik yapmadan doğrudan çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `combo` | COMBO | Evet | `"option1"`<br>`"option2"`<br>`"option3"` | Üç test seçeneğinden oluşan ilk kümeden yapılan seçim. |
| `combo2` | COMBO | Evet | `"option4"`<br>`"option5"`<br>`"option6"` | Farklı üç test seçeneğinden oluşan ikinci kümeden yapılan seçim. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output_1` | COMBO | İlk birleşik giriş kutusundan (`combo`) seçilen değeri çıktı olarak verir. |
| `output_2` | COMBO | İkinci birleşik giriş kutusundan (`combo2`) seçilen değeri çıktı olarak verir. |

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`

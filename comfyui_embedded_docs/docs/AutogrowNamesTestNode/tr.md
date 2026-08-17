# AutogrowNamesTestNode

Bu düğüm, Autogrow giriş özelliği için bir testtir. Her biri belirli bir adla etiketlenmiş dinamik sayıda float girişi alır ve değerlerini virgülle ayrılmış tek bir dizede birleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | Dinamik bir giriş grubudur. Listede önceden tanımlanmış adlara sahip birden fazla float girişi ekleyebilirsiniz: "a", "b" veya "c". Düğüm, bu adlandırılmış girişlerin herhangi bir kombinasyonunu kabul eder. | FLOAT | Evet | N/A |

**Not:** `autogrow` girişi dinamiktir. İş akışınıza göre tek tek float girişleri ("a", "b" veya "c" adlı) ekleyebilir veya kaldırabilirsiniz. Düğüm, sağlanan tüm değerleri işler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sağlanan tüm float girişlerinin değerlerini virgülle birleştiren tek bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`

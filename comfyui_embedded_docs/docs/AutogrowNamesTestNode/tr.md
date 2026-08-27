# AutogrowNamesTestNode

Bu düğüm, Autogrow girdi özelliği için bir testtir. Dinamik sayıda float girdisi alır; her biri belirli bir adla etiketlenir ve değerlerini virgülle ayrılmış tek bir dizede birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | Dinamik bir girdi grubu. Her biri "a", "b" veya "c" listesinden önceden tanımlanmış bir ada sahip birden çok float girdisi ekleyebilirsiniz. Düğüm, bu adlandırılmış girdilerin herhangi bir kombinasyonunu kabul eder. | FLOAT | Evet | N/A |

**Not:** `autogrow` girdisi dinamiktir. İş akışınız için gerektiğinde tek tek float girdileri ("a", "b" veya "c" adlı) ekleyebilir veya kaldırabilirsiniz. Düğüm, sağlanan tüm değerleri işler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sağlanan tüm float girdilerindeki değerleri virgüllerle birleştirilmiş tek bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`

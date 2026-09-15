# AutogrowNamesTestNode

Bu düğüm, Autogrow girdi özelliği için bir testtir. Her biri önceden tanımlanmış bir ada sahip dinamik bir float girdi grubunu kabul eder ve değerlerini virgülle ayrılmış tek bir dizede birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | Dinamik bir girdi grubu. Şu listeden önceden tanımlanmış bir ada sahip birden fazla float girdisi ekleyebilirsiniz: "a", "b" veya "c". Düğüm, bu adlandırılmış girdilerin herhangi bir kombinasyonunu kabul eder. | FLOAT | Evet | Adlandırılmış yuvalar: `a`, `b`, `c` |

**Not:** `autogrow` girdisi dinamiktir. "a", "b" ve "c" adlı tek tek float girdileri gerektiği gibi eklenebilir veya kaldırılabilir. Sağlanan tüm değerler düğüm tarafından işlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sağlanan tüm float girdilerinin değerlerini içeren ve virgüllerle birleştirilmiş tek bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`

# Manuel Sigmalar

The ManualSigmas node allows you to manually define a custom sequence of noise levels (sigmas) for the sampling process. You input a list of numbers as a string, and the node converts them into a tensor that can be used by other sampling nodes. This is useful for testing or creating specific noise schedules.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Sigma değerlerini içeren bir dize. Düğüm, bu dizeden ondalık ve negatif değerler dahil tüm sayıları çıkarır. Örneğin, "1, 0.5, 0.1" veya "1 0.5 0.1". Varsayılan: "1, 0.5". | STRING | Evet | Virgül veya boşlukla ayrılmış herhangi bir sayısal değer |

Not: Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Girdi dizesinden çıkarılan sigma değerleri dizisini içeren bir tensör. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`

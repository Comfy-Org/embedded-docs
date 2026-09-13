# Manuel Sigmalar

ManualSigmas düğümü, örnekleme işlemi için özel bir gürültü seviyeleri (sigmalar) dizisini manuel olarak tanımlamanıza olanak tanır. Bir sayı listesini dize olarak girersiniz ve düğüm bunları diğer örnekleme düğümleri tarafından kullanılabilecek bir SIGMAS tensörüne dönüştürür. Bu, test etmek veya belirli gürültü çizelgeleri oluşturmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmas` | Sigma değerlerini içeren bir dize. Düğüm bu dizedeki tüm sayıları, ondalık ve negatif değerler dahil olmak üzere ayıklar. Örneğin, "1, 0.5, 0.1" veya "1 0.5 0.1". Varsayılan: "1, 0.5". | STRING | Evet | Virgülle veya boşlukla ayrılmış herhangi bir sayısal değerler |

Not: Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Girdi dizesinden ayıklanan sigma değerleri dizisini içeren bir tensör. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`

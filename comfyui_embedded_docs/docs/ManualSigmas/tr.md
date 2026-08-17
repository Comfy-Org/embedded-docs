# Manuel Sigmalar

ManualSigmas düğümü, örnekleme süreci için özel bir gürültü seviyeleri (sigma) dizisini manuel olarak tanımlamanıza olanak tanır. Bir dize olarak bir sayı listesi girersiniz ve düğüm bunları diğer örnekleme düğümleri tarafından kullanılabilir bir tensöre dönüştürür. Bu, belirli gürültü çizelgelerini test etmek veya oluşturmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmas` | Sigma değerlerini içeren bir dize. Düğüm bu dizedeki tüm sayıları çıkarır. Örneğin, "1, 0.5, 0.1" veya "1 0.5 0.1". Varsayılan değer "1, 0.5" şeklindedir. | STRING | Evet | Virgül veya boşlukla ayrılmış herhangi bir sayı |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Girdi dizesinden çıkarılan sigma değerleri dizisini içeren tensör. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`

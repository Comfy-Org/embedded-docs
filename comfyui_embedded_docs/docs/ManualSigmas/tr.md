> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/tr.md)

ManualSigmas düğümü, örnekleme süreci için özel bir gürültü seviyesi (sigma) dizisini manuel olarak tanımlamanıza olanak tanır. Bir sayı listesini dize olarak girersiniz ve düğüm bunları diğer örnekleme düğümleri tarafından kullanılabilecek bir tensöre dönüştürür. Bu, belirli gürültü programlarını test etmek veya oluşturmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `sigmalar` | STRING | Evet | Virgül veya boşlukla ayrılmış herhangi bir sayı | Sigma değerlerini içeren bir dize. Düğüm, bu dizedeki tüm sayıları çıkarır. Örneğin, "1, 0.5, 0.1" veya "1 0.5 0.1". Varsayılan değer "1, 0.5" şeklindedir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sigmalar` | SIGMAS | Giriş dizesinden çıkarılan sigma değerleri dizisini içeren tensör. |

---
**Source fingerprint (SHA-256):** `b815633dfea8f529f487f46b2d0464fa8c1045df8c4d4ef586bd36ad6f4a28db`

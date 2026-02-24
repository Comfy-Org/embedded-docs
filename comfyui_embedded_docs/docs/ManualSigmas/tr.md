> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/tr.md)

ManualSigmas düğümü, örnekleme süreci için özel bir gürültü seviyeleri (sigmalar) dizisini manuel olarak tanımlamanıza olanak tanır. Bir dize olarak bir sayı listesi girersiniz ve düğüm bunları diğer örnekleme düğümleri tarafından kullanılabilecek bir tensöre dönüştürür. Bu, test etmek veya belirli gürültü programları oluşturmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | STRING | Evet | Virgül veya boşlukla ayrılmış herhangi bir sayı | Sigma değerlerini içeren bir dize. Düğüm bu dizeden tüm sayıları çıkaracaktır. Örneğin: "1, 0.5, 0.1" veya "1 0.5 0.1". Varsayılan değer "1, 0.5" şeklindedir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Giriş dizesinden çıkarılan sigma değerleri dizisini içeren tensör. |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/tr.md)

Bu düğüm, Autogrow giriş özelliği için bir testtir. Belirli bir adla etiketlenmiş dinamik sayıda float girişi alır ve bunların değerlerini tek bir virgülle ayrılmış dize halinde birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | FLOAT | Evet | Yok | Dinamik bir giriş grubu. "a", "b" veya "c" listesinden önceden tanımlanmış bir adla birden fazla float girişi ekleyebilirsiniz. Düğüm, bu adlandırılmış girişlerin herhangi bir kombinasyonunu kabul edecektir. |

**Not:** `autogrow` girişi dinamiktir. İş akışınızın ihtiyacına göre ("a", "b" veya "c" adlı) bireysel float girişlerini ekleyebilir veya kaldırabilirsiniz. Düğüm, sağlanan tüm değerleri işler.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Sağlanan tüm float girişlerinden gelen değerlerin virgüllerle birleştirilmiş halini içeren tek bir dize. |

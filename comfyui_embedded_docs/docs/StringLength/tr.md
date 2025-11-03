> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringLength/tr.md)

StringLength düğümü, bir metin dizesindeki karakter sayısını hesaplar. Herhangi bir metin girişini alır ve boşluklar ve noktalama işaretleri dahil olmak üzere toplam karakter sayısını döndürür. Bu, metin uzunluğunu ölçmek veya dize boyutu gereksinimlerini doğrulamak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | Yok | Uzunluğu ölçülecek metin dizesi. Çok satırlı girişi destekler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `length` | INT | Giriş dizesindeki toplam karakter sayısı, boşluklar ve özel karakterler dahil. |
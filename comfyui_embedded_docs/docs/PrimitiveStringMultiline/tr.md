> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/tr.md)

**PrimitiveStringMultiline** düğümü, iş akışınızda kullanmak üzere çok satırlı metin girişi yapabileceğiniz bir metin giriş alanı sağlar. Birden fazla satırdan oluşan metin girişini kabul eder ve aynı dize değerini değiştirmeden çıktı olarak verir. Bu düğüm, daha uzun metin içeriği veya birden çok satıra yayılan biçimlendirilmiş metin girmeniz gerektiğinde kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `value` | STRING | Evet | Yok | Birden fazla satıra yayılabilen metin giriş değeri |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Giriş olarak sağlanan aynı dize değeri |
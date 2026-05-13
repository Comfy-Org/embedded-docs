> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/tr.md)

## Genel Bakış

PrimitiveStringMultiline düğümü, iş akışınızda dize değerleri girmek ve iletmek için çok satırlı bir metin giriş alanı sağlar. Birden çok satır içeren metin girdisini kabul eder ve aynı dize değerini değiştirmeden çıktı olarak verir. Bu düğüm, daha uzun metin içeriği veya birden çok satıra yayılan biçimlendirilmiş metin girmeniz gerektiğinde kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `değer` | STRING | Evet | Yok | Birden çok satıra yayılabilen metin giriş değeri |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Giriş olarak sağlanan aynı dize değeri |

---
**Source fingerprint (SHA-256):** `a2faaf366d6316d659b749ec6077b944f9b0f1ad702d699acc3897aef842b937`

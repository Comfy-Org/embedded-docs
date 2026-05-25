> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/tr.md)

## Genel Bakış

Bu düğüm, Python'un string format yöntemini kullanarak metin biçimlendirir. Yer tutucularla bir metin kalıbı tanımladığınız ve ardından bu yer tutucuları doldurmak için değerler sağladığınız bir şablon gibi çalışır. Python'un tüm format seçeneklerini ve özelliklerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `f_string` | STRING | Evet | Yok | Yer tutucuları içeren format dizesi şablonu (varsayılan: `{a}`). Çok satırlı girişi destekler. |
| `values` | STRING | Evet | Yok | Format dizesindeki yer tutucuları doldurmak için değerler sağlayan dinamik giriş. Gerektiğinde birden fazla değer girişi eklenebilir. |

**`values` girişi hakkında not:** Bu giriş dinamiktir ve birden fazla adlandırılmış değer içerecek şekilde genişletilebilir. Her değer girişi bir harfle (a, b, c vb.) etiketlenir ve format dizesindeki bir yer tutucuya (örneğin `{a}`, `{b}`, `{c}`) karşılık gelir. Gerektiğinde değer girişleri ekleyebilir veya kaldırabilirsiniz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `STRING` | STRING | Tüm yer tutucuların karşılık gelen değerlerle değiştirildiği biçimlendirilmiş metin dizesi. |

---
**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`

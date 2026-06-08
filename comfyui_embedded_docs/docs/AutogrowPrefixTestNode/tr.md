## Genel Bakış  
AutogrowPrefixTestNode, otomatik büyüme giriş özelliğini test etmek için tasarlanmış bir mantık düğümüdür. Dinamik sayıda float girişi kabul eder, bu değerleri virgülle ayrılmış bir dize halinde birleştirir ve bu dizeyi çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | 1 ile 10 arasında float değeri kabul edebilen dinamik bir giriş grubu. Gruptaki her giriş, minimum değeri 1 ve maksimum değeri 10 olan FLOAT türündedir. | AUTOGROW | Evet | 1 ila 10 giriş |

**Not:** `autogrow` girişi özel bir dinamik giriştir. Bu gruba en fazla 10 adede kadar birden fazla float girişi ekleyebilirsiniz. Düğüm, sağlanan tüm değerleri işleyecektir. Her bir float girişi 1 ila 10 aralığıyla sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm giriş float değerlerini virgülle ayırarak içeren tek bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `7ae65365f77399a2ad8358b5a1eab3f2caa39331e53dec474cdd7f2751bfff4b`

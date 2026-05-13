> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/tr.md)

## Genel Bakış

Bu düğüm, Otomatik Büyüme (Autogrow) giriş özelliği için bir test düğümüdür. Dinamik sayıda ondalık sayı (float) girişi alır, her biri belirli bir adla etiketlenir ve bu değerleri virgülle ayrılmış tek bir dize (string) halinde birleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | FLOAT | Evet | Yok | Dinamik bir giriş grubu. "a", "b" veya "c" listesinden önceden tanımlanmış bir ada sahip birden fazla ondalık sayı girişi ekleyebilirsiniz. Düğüm, bu adlandırılmış girişlerin herhangi bir kombinasyonunu kabul eder. |

**Not:** `autogrow` girişi dinamiktir. İş akışınız için gerektiği şekilde "a", "b" veya "c" adlı bireysel ondalık sayı girişlerini ekleyebilir veya kaldırabilirsiniz. Düğüm, sağlanan tüm değerleri işler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Sağlanan tüm ondalık sayı girişlerinden gelen değerlerin virgülle birleştirilmesiyle oluşturulan tek bir dize. |

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`

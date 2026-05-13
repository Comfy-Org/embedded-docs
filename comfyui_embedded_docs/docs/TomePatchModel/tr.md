> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/tr.md)

TomePatchModel düğümü, bir yayılma modeline Token Birleştirme (ToMe) uygulayarak çıkarım sırasında hesaplama gereksinimlerini azaltır. Dikkat mekanizmasındaki benzer tokenleri seçici bir şekilde birleştirerek çalışır ve modelin görüntü kalitesini korurken daha az token işlemesine olanak tanır. Bu teknik, önemli bir kalite kaybı olmadan üretimi hızlandırmaya yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | MODEL | Evet | - | Token birleştirmenin uygulanacağı yayılma modeli |
| `ratio` | FLOAT | Hayır | 0.0 - 1.0 | Birleştirilecek tokenlerin oranı (varsayılan: 0.3) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Token birleştirme uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`

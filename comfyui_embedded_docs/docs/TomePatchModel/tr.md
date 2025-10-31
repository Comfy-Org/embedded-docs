> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/tr.md)

TomePatchModel düğümü, çıkarım sırasında hesaplama gereksinimlerini azaltmak için bir difüzyon modeline Token Birleştirme (ToMe) uygular. Dikkat mekanizmasında benzer token'ları seçici bir şekilde birleştirerek çalışır ve modelin görsel kaliteyi korurken daha az token işlemesine olanak tanır. Bu teknik, önemli kalite kaybı olmadan üretim hızını artırmaya yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Token birleştirme uygulanacak difüzyon modeli |
| `ratio` | FLOAT | Hayır | 0.0 - 1.0 | Birleştirilecek token'ların oranı (varsayılan: 0.3) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Token birleştirme uygulanmış değiştirilmiş model |
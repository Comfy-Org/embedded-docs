# Tome Model Yaması

TomePatchModel, çıkarım sırasında hesaplama maliyetini azaltmak için bir difüzyon modeline Token Merging (ToMe) uygular. Modelin dikkat mekanizması içindeki benzer token'ları birleştirerek çalışır; böylece model, çıktı kalitesini büyük ölçüde korurken daha az token işler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Token birleştirmenin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `ratio` | Birleştirilecek token oranı (varsayılan: 0.3). Daha yüksek değerler daha fazla token birleştirir; bu daha büyük hızlanma sağlayabilir ancak potansiyel olarak kaliteyi düşürebilir. | FLOAT | Evet | 0.0 - 1.0 |

Not: Bir dikkat bloğundaki token sayısı, alt örnekleme gerekmeyecek kadar küçükse, birleştirme işlevleri no-op'larla değiştirilir ve model o blok için değişmeden çalışır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Token birleştirme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/tr.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`

# Tome Model Yaması

TomePatchModel düğümü, çıkarım sırasında hesaplama gereksinimlerini azaltmak için bir difüzyon modeline Token Birleştirme (ToMe) uygular. Dikkat mekanizmasındaki benzer tokenleri seçici olarak birleştirerek çalışır ve modelin görüntü kalitesini korurken daha az token işlemesine olanak tanır. Bu teknik, önemli kalite kaybı olmadan üretimi hızlandırmaya yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Token birleştirmenin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `ratio` | Birleştirilecek tokenlerin oranı (varsayılan: 0.3, adım: 0.01). Daha yüksek değerler daha fazla tokeni birleştirir, bu da daha fazla hız artışı sağlar ancak potansiyel olarak daha düşük kaliteye neden olur. | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Token birleştirme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/tr.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`

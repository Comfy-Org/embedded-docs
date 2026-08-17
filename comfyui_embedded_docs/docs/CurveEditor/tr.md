# Eğri Düzenleyici

Curve Editor düğümü, bir eğriyi ayarlamak ve ince ayar yapmak için görsel bir arayüz sağlar. Giriş eğrisinin şeklini değiştirmenize ve isteğe bağlı olarak histogram ile dağılımını görselleştirmenize olanak tanır. Düğüm, değiştirilmiş eğriyi iş akışınızın diğer bölümlerinde kullanmak üzere çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `curve` | Düzenlenecek giriş eğrisi. | CURVE | Evet | N/A |
| `histogram` | Görsel referans için eğrinin yanında görüntülenecek isteğe bağlı histogram. | HISTOGRAM | Hayır | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `curve` | Düğümün arayüzünde ayarlamalar yapıldıktan sonra düzenlenmiş eğri. | CURVE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/tr.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`

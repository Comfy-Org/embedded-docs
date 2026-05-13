> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/tr.md)

Eğri Düzenleyici düğümü, bir eğriyi ayarlamak ve ince ayar yapmak için görsel bir arayüz sağlar. Giriş eğrisinin şeklini değiştirmenize ve isteğe bağlı olarak histogram ile dağılımını görselleştirmenize olanak tanır. Düğüm, iş akışınızın diğer bölümlerinde kullanılmak üzere değiştirilmiş eğriyi çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `eğri` | CURVE | Evet | Yok | Düzenlenecek giriş eğrisi. |
| `histogram` | HISTOGRAM | Hayır | Yok | Görsel referans için eğrinin yanında görüntülenecek isteğe bağlı histogram. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `eğri` | CURVE | Düğüm arayüzünde yapılan ayarlamalar sonrasında düzenlenmiş eğri. |

---
**Source fingerprint (SHA-256):** `34cf36a5b934c44ebfce0b81e7c515f1b31fb17f3b7e1ad52255d1d72f68240b`

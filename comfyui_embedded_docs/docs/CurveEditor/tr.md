> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/tr.md)

ComfyUI Düğüm Belgeleri - Eğri Düzenleyici (Curve Editor)

Eğri Düzenleyici düğümü, bir eğriyi ayarlamak ve ince ayar yapmak için görsel bir arayüz sağlar. Giriş eğrisinin şeklini değiştirmenize ve isteğe bağlı olarak histogram ile dağılımını görselleştirmenize olanak tanır. Düğüm, iş akışınızın diğer bölümlerinde kullanılmak üzere düzenlenmiş eğriyi çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `curve` | CURVE | Evet | Yok | Düzenlenecek giriş eğrisi. |
| `histogram` | HISTOGRAM | Hayır | Yok | Görsel referans için eğrinin yanında görüntülenecek isteğe bağlı histogram. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `curve` | CURVE | Düğüm arayüzünde yapılan ayarlamalar sonrasında düzenlenmiş eğri. |
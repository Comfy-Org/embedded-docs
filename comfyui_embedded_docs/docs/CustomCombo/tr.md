> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/tr.md)

Custom Combo düğümü, kendi metin seçeneklerinizden oluşan özel bir açılır menü oluşturmanıza olanak tanır. İş akışınız içinde uyumluluğu sağlamak için bir arka plan temsili sunan, ön yüze odaklanmış bir düğümdür. Açılır menüden bir seçenek belirlediğinizde, düğüm bu metni bir dize olarak çıktı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `choice` | COMBO | Evet | Kullanıcı tanımlı | Özel açılır menüden seçilen metin seçeneği. Kullanılabilir seçeneklerin listesi, kullanıcı tarafından düğümün ön yüz arayüzünde tanımlanır. |

**Not:** Bu düğümün giriş doğrulaması kasıtlı olarak devre dışı bırakılmıştır. Bu, seçiminizin önceden tanımlanmış bir listeden olup olmadığını arka planın kontrol etmesine gerek kalmadan, ön yüzde istediğiniz herhangi bir özel metin seçeneğini tanımlamanıza olanak tanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Özel birleşik kutudan seçilen seçeneğin metin dizesi. |

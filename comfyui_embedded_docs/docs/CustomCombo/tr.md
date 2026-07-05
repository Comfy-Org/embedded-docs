# Özel Kombinasyon

Özel Bileşen düğümü, kendi metin seçenek listenizle özel bir açılır menü oluşturmanıza olanak tanır. İş akışınızda uyumluluğu sağlamak için bir arka uç temsili sağlayan, ön uç odaklı bir düğümdür. Açılır menüden bir seçenek belirlediğinizde, düğüm bu metni bir dize ve dizin konumu olarak çıktılar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seçim` | Özel açılır menüden seçilen metin seçeneği. Kullanılabilir seçeneklerin listesi, düğümün ön uç arayüzünde kullanıcı tarafından tanımlanır. | COMBO | Evet | Kullanıcı tanımlı |
| `index` | Bir dizin belirtmek için kullanılabilen bir tamsayı değeri. Varsayılan: 0. | INT | Hayır | 0 |

**Not:** Bu düğümün girişi için doğrulama kasıtlı olarak devre dışı bırakılmıştır. Bu, arka uç seçiminizin önceden tanımlanmış bir listeden olup olmadığını kontrol etmeden ön uçta istediğiniz herhangi bir özel metin seçeneğini tanımlamanıza olanak tanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `INDEX` | Özel bileşen kutusundan seçilen seçeneğin metin dizesi. | STRING |
| `INDEX` | Seçilen seçeneğin açılır listedeki dizin konumu. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/tr.md)

---
**Source fingerprint (SHA-256):** `d950207b94deee37abce294eb3dab035e622925dc1118fe37f9c874784dc1672`

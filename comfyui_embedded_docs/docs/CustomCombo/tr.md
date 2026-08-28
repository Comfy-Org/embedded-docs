# Özel Kombinasyon

Custom Combo düğümü, kendi metin seçenekleri listenizle özel bir açılır menü oluşturmanızı sağlar. İş akışınızı uyumlu tutmak için bir arka uç temsili içeren, ön uç odaklı bir düğümdür. Açılır menüden bir seçenek seçtiğinizde, düğüm bu metni bir dize ve dizin konumu olarak çıktı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seçim` | Özel açılır menüden seçilen metin seçeneği. Kullanılabilir seçeneklerin listesi, kullanıcı tarafından düğümün ön uç arayüzünde tanımlanır. | COMBO | Evet | Kullanıcı tanımlı |
| `index` | Bir dizin belirtmek için kullanılabilen bir tam sayı değeri. Varsayılan: 0. | INT | Hayır | Herhangi bir tam sayı (varsayılan: 0) |

**Not:** Bu düğümün girdileri için doğrulama kasıtlı olarak devre dışı bırakılmıştır. Bu, arka ucun seçiminizin önceden tanımlanmış bir listeyle eşleşip eşleşmediğini kontrol etmeden ön uçta herhangi bir özel metin seçeneği yazmanıza olanak tanır. Açılır menü dışındaki widget'lar tamamen ön uçta tanımlanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Özel açılır listeden seçilen seçeneğin metin dizesi. | STRING |
| `INDEX` | Seçilen seçeneğin açılır listedeki dizin konumu. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/tr.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`

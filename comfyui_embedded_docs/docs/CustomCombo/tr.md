# Özel Kombinasyon

Custom Combo düğümü, kendi metin seçeneklerinizden oluşan bir listeyle özel bir açılır menü oluşturmanızı sağlar. Ön uç odaklı bir düğümdür; iş akışınızda uyumluluk sağlamak için bir arka uç temsili sunar. Açılır menüden bir seçenek seçtiğinizde, düğüm bu metni bir dize (string) olarak ve seçeneğin dizin konumunu çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `choice` | Özel açılır menüden seçilen metin seçeneği. Kullanılabilir seçeneklerin listesi, kullanıcı tarafından düğümün ön uç arayüzünde tanımlanır. | COMBO | Evet | Kullanıcı tanımlı |
| `index` | Bir dizin belirtmek için kullanılabilen bir tamsayı değeri. Varsayılan: 0. | INT | Hayır | Herhangi bir tamsayı |

**Not:** Bu düğümün girdi doğrulaması bilinçli olarak devre dışı bırakılmıştır. Bu sayede arka uç, seçiminizin önceden tanımlanmış bir listeden olup olmadığını denetlemeden, ön uçta istediğiniz her türlü özel metin seçeneğini tanımlayabilirsiniz. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `STRING` | Özel açılır kutudan seçilen seçeneğin metin dizesi. | STRING |
| `INDEX` | Seçilen seçeneğin açılır listedeki dizin konumu. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/tr.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`

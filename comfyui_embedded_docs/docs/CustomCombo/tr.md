# Özel Kombinasyon

Custom Combo düğümü, sabit değerler arasından seçim yapmak yerine bir açılır menü için kendi metin seçenekleri listenizi tanımlamanıza olanak tanır. Aynı zamanda arka uç temsili de olan, ön uç odaklı bir düğümdür; böylece onu içeren iş akışları uyumlu kalır. Bir seçenek seçtiğinizde düğüm, seçilen metni ve dizin konumunu çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `choice` | Özel açılır menüden seçilen metin seçeneği. Kullanılabilir seçenekler listesi, düğümün ön uç arayüzünde kullanıcı tarafından tanımlanır. | COMBO | Evet | Kullanıcı tanımlı |
| `index` | Bir dizin belirtmek için kullanılabilecek tam sayı değeri. Varsayılan: 0. | INT | Hayır | Herhangi bir tam sayı (varsayılan: 0) |

**Not:** Bu düğümün girdileri için doğrulama kasıtlı olarak devre dışı bırakılmıştır. Bu, ön uçta herhangi bir özel metin seçeneği yazmanıza olanak tanır; arka uç, seçiminizin önceden tanımlanmış bir listeyle eşleşip eşleşmediğini kontrol etmez. Combo açılır menüsü dışındaki widget'lar tamamen ön uçta tanımlanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Özel combo kutusundan seçilen seçeneğin metin dizesi. | STRING |
| `INDEX` | Seçilen seçeneğin açılır liste içindeki dizin konumu. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/tr.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`

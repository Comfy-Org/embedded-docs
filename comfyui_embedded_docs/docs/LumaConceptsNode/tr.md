# Luma Kavramları

Luma Metinden Videoya ve Luma Görüntüden Videoya düğümleriyle kullanılmak üzere bir veya daha fazla Kamera Konseptini tutar. Bu düğüm, en fazla dört kamera konsepti seçmenize ve isteğe bağlı olarak bunları mevcut konsept zincirleriyle birleştirmenize olanak tanır.

**Not:** Bu düğüm kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kavram1` | Mevcut Luma konseptlerinden ilk kamera konsepti seçimi | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir |
| `kavram2` | Mevcut Luma konseptlerinden ikinci kamera konsepti seçimi | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir |
| `kavram3` | Mevcut Luma konseptlerinden üçüncü kamera konsepti seçimi | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir |
| `kavram4` | Mevcut Luma konseptlerinden dördüncü kamera konsepti seçimi | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir |
| `luma_kavramları` | Burada seçilenlere eklenecek isteğe bağlı Kamera Konseptleri | LUMA_CONCEPTS | Hayır | Yok |

**Not:** Dört konsept yuvasının tamamını kullanmak istemiyorsanız, tüm konsept parametreleri (`concept1` ile `concept4` arası) "Yok" olarak ayarlanabilir. Düğüm, sağlanan `luma_concepts` değerlerini seçilen konseptlerle birleştirerek birleşik bir konsept zinciri oluşturacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `luma_kavramları` | Seçilen tüm konseptleri içeren birleşik kamera konsept zinciri | LUMA_CONCEPTS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/tr.md)

---
**Source fingerprint (SHA-256):** `fc9da6288e29d89519f13e2412381ad8d689fc48353a80546a380dbe8f979037`

PixVerse API'sini kullanarak iki giriş görüntüsü arasında bir geçiş videosu oluşturur. Bir başlangıç görüntüsü ve bir bitiş görüntüsü sağlarsınız; düğüm, metin isteminiz ve seçtiğiniz ayarlar doğrultusunda birinden diğerine yumuşak bir geçiş yapan bir video oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ilk_kare` | Video geçişi için başlangıç görüntüsü | IMAGE | Evet | - |
| `son_kare` | Video geçişi için bitiş görüntüsü | IMAGE | Evet | - |
| `istem` | Video oluşturma için istem (varsayılan: boş dize) | STRING | Evet | - |
| `kalite` | Video kalite ayarı (varsayılan: `"540p"`) | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `süre_saniye` | Video süresi (saniye cinsinden) | COMBO | Evet | `5`<br>`8` |
| `hareket_modu` | Geçiş için hareket stili (varsayılan: `"normal"`) | COMBO | Evet | `"normal"`<br>`"fast"` |
| `tohum` | Video oluşturma için tohum değeri (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |

**Parametre kısıtlamalarına ilişkin not:** 1080p kalitesi kullanıldığında, hareket modu otomatik olarak `"normal"` olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki herhangi bir süre için hareket modu da otomatik olarak `"normal"` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan geçiş videosu | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`

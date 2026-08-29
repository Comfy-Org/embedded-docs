# PixVerse Geçiş Videosu

PixVerse API kullanarak iki girdi görüntüsü arasında geçiş videosu oluşturur. Bir başlangıç görüntüsü ve bir bitiş görüntüsü sağlarsınız; düğüm, metin isteminiz ve seçtiğiniz ayarlar doğrultusunda birinden diğerine geçiş yapan akıcı bir video oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ilk_kare` | Video geçişi için başlangıç görüntüsü | IMAGE | Evet | - |
| `son_kare` | Video geçişi için bitiş görüntüsü | IMAGE | Evet | - |
| `istem` | Video oluşturma için istem (varsayılan: boş dize) | STRING | Evet | - |
| `kalite` | Video kalitesi ayarı (varsayılan: `"540p"`) | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `süre_saniye` | Video süresi (saniye) | COMBO | Evet | `5`<br>`8` |
| `hareket_modu` | Geçiş için hareket stili (varsayılan: `"normal"`) | COMBO | Evet | `"normal"`<br>`"fast"` |
| `tohum` | Video oluşturma için tohum (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `negatif_istem` | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |

**Parametre kısıtlamalarına ilişkin not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak `"normal"` olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki herhangi bir süre için, hareket modu da otomatik olarak `"normal"` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan geçiş videosu | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9774f15ae93377d4768cee9f51ce004a791ecaad3cadd0a2467d354c4dbc6f23`

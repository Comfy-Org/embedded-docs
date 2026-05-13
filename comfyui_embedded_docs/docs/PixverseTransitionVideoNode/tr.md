> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/tr.md)

PixVerse API'sini kullanarak iki giriş görüntüsü arasında bir geçiş videosu oluşturur. Bir başlangıç görüntüsü ve bir bitiş görüntüsü sağlarsınız; düğüm, metin isteminiz ve seçtiğiniz ayarlar doğrultusunda birinden diğerine yumuşak bir geçiş yapan bir video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ilk_kare` | IMAGE | Evet | - | Video geçişi için başlangıç görüntüsü |
| `son_kare` | IMAGE | Evet | - | Video geçişi için bitiş görüntüsü |
| `istem` | STRING | Evet | - | Video oluşturma için istem (varsayılan: boş dize) |
| `kalite` | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` | Video kalite ayarı (varsayılan: `"540p"`) |
| `süre_saniye` | COMBO | Evet | `5`<br>`8` | Video süresi (saniye cinsinden) |
| `hareket_modu` | COMBO | Evet | `"normal"`<br>`"fast"` | Geçiş için hareket stili (varsayılan: `"normal"`) |
| `tohum` | INT | Evet | 0 ile 2147483647 arası | Video oluşturma için tohum değeri (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) |

**Parametre kısıtlamalarına ilişkin not:** 1080p kalitesi kullanıldığında, hareket modu otomatik olarak `"normal"` olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki herhangi bir süre için hareket modu da otomatik olarak `"normal"` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan geçiş videosu |

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`

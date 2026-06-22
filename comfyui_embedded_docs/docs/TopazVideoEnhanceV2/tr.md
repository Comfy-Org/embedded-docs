# Topaz Video Enhance

**Topaz Video Enhance V2** düğümü, Topaz Labs'ın yapay zeka modellerini kullanarak videoları yükseltmenize ve iyileştirmenize olanak tanır. Çözünürlüğü artırabilir, kare hızını enterpolasyon yoluyla ayarlayabilir ve video görüntülerinize yaratıcı veya gerçekçi iyileştirmeler uygulayarak yeni bir soluk getirebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | İşlenecek giriş videosu. MP4 konteyner formatında olmalıdır. | VIDEO | Evet | - |
| `yükseltici_model` | Videoyu yükseltmek için kullanılan yapay zeka modeli. "Disabled" seçilmesi, herhangi bir yükseltme uygulanmayacağı anlamına gelir. | COMBO | Evet | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `upscaler_model.upscaler_resolution` | Yükseltici için hedef çıkış çözünürlüğü. Bu parametre, bir yükseltici modeli seçildiğinde ("Disabled" değil) zorunludur. | COMBO | Koşullu | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Yükseltmenin yaratıcılık gücü. Yalnızca "Astra 2" ve "Starlight (Astra) Creative" modelleri için kullanılabilir. Astra 2 için bir kaydırıcıdır (varsayılan: 0.5). Starlight Creative için bir kombinasyon kutusudur (varsayılan: "low"). | FLOAT / COMBO | Koşullu | Astra 2: 0.0 ila 1.0 (adım 0.1)<br>Starlight Creative: `"low"`<br>`"middle"`<br>`"high"` |
| `upscaler_model.prompt` | İsteğe bağlı tanımlayıcı (yönlendirici değil) sahne istemi. Yalnızca "Astra 2" modeli için kullanılabilir. Ayarlandığında 500 giriş karesiyle (~15sn @ 30fps) sınırlıdır. Varsayılan: boş. | STRING | Hayır | - |
| `upscaler_model.sharp` | Ön iyileştirme keskinliği: 0.0=Gauss bulanıklığı, 0.5=doğrudan geçiş (varsayılan), 1.0=USM keskinleştirme. Yalnızca "Astra 2" modeli için kullanılabilir. Varsayılan: 0.5. | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.01) |
| `upscaler_model.realism` | Çıktıyı fotografik gerçekçiliğe doğru çeker. Model varsayılanı için 0'da bırakın. Yalnızca "Astra 2" modeli için kullanılabilir. Varsayılan: 0.0. | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.01) |
| `enterpolasyon_modeli` | Kare enterpolasyonu için kullanılan yapay zeka modeli. "Disabled" seçilmesi, herhangi bir enterpolasyon uygulanmayacağı anlamına gelir. | COMBO | Evet | `"Disabled"`<br>`"apo-8"` |
| `interpolation_model.interpolation_frame_rate` | Çıkış kare hızı. Enterpolasyon modeli "apo-8" olduğunda zorunludur. Varsayılan: 60. | INT | Koşullu | 15 ila 240 |
| `interpolation_model.interpolation_slowmo` | Giriş videosuna uygulanan ağır çekim faktörü. Örneğin, 2 çıkışı iki kat daha yavaş yapar ve süreyi iki katına çıkarır. Varsayılan: 1. | INT | Hayır | 1 ila 16 |
| `interpolation_model.interpolation_duplicate` | Yinelenen kareler için girişi analiz eder ve bunları kaldırır. Varsayılan: False. | BOOLEAN | Hayır | True/False |
| `interpolation_model.interpolation_duplicate_threshold` | Yinelenen kareler için algılama hassasiyeti. Varsayılan: 0.01. | FLOAT | Hayır | 0.001 ila 0.1 (adım 0.001) |
| `dinamik_sıkıştırma_seviyesi` | Video sıkıştırma için CQP seviyesi. Varsayılan: "Low". | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` |

**Önemli Kısıtlamalar:**
- `upscaler_model` veya `interpolation_model` öğelerinden en az biri etkinleştirilmelidir ("Disabled" değil), aksi takdirde hata oluşur.
- Giriş videosu MP4 konteyner formatında olmalıdır.
- İstem içeren "Astra 2" modeli 500 giriş karesiyle (~30fps'de ~15 saniye) sınırlıdır. İstem olmadan daha yüksek sayıda kareyle sınırlıdır.
- `upscaler_model` "Disabled" olmadığında, `upscaler_resolution` alt parametresi zorunludur.
- `interpolation_model` "Disabled" olmadığında, `interpolation_frame_rate` alt parametresi zorunludur.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Seçilen yükseltme ve/veya enterpolasyon filtreleri uygulandıktan sonra iyileştirilmiş video çıkışı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/tr.md)

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`

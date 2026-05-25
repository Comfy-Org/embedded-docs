> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/tr.md)

## Genel Bakış

Bu düğüm, örnekleme sürecinin sonraki aşamasında model çıktısını birden fazla kaydırılmış yama ızgarası konumunda ortalamasını alarak HiDream-O1 modeli tarafından oluşturulan görsellerdeki görünür dikişleri azaltır. Modeli, hafifçe farklı görüntü hizalamalarıyla birkaç kez çalıştırıp sonuçları birleştirerek çalışır; bu da yama sınırlarında oluşabilen ızgara benzeri yapaylıkların giderilmesine yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Dikiş yumuşatma uygulanacak HiDream-O1 modeli. |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) | Yumuşatma efektinin AÇILDIĞI örnekleme ilerlemesi (0=başlangıç, 1=bitiş) (varsayılan: 0.8). |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) | Yumuşatma efektinin KAPANDIĞI örnekleme ilerlemesi (varsayılan: 1.0). |
| `desen` | COMBO | Evet | `"single_shift"`<br>`"symmetric"` | Kaydırılmış ızgara konumlarının düzeni. `single_shift`: doğal yama ızgarasında bir geçiş artı diğer kaydırmalar. `symmetric`: tüm geçişler ızgara dışındadır, kaydırmalar orijin etrafında bölünmüştür (varsayılan: `"single_shift"`). |
| `geçişler` | COMBO | Evet | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` | Kapılı adım başına geçiş sayısı (model çalıştırma). `2` veya `4` sabit sayılardır. `ramp_2_4` ve `ramp_2_4_8`, örnekleme sona yaklaştıkça geçiş sayısını artırarak dikişlerin en görünür olduğu yerlerde daha fazla yumuşatma sağlar (varsayılan: `"2"`). |
| `karıştırma` | COMBO | Evet | `"average"`<br>`"window"`<br>`"median"` | Her geçişten elde edilen sonuçları birleştirmek için kullanılan yöntem. `average`: tüm geçişlerin eşit ağırlıklı ortalaması. `window`: her geçişin merkezine daha fazla ağırlık vermek için Hann penceresi kullanır, sınır yapaylıklarını azaltır. `median`: piksel bazında medyan alır, sarma kaynaklı aykırı geçişleri eleyebilir (varsayılan: `"average"`). |
| `güç` | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) | Orijinal model çıktısı (0.0) ile tamamen yumuşatılmış sonuç (1.0) arasındaki enterpolasyonu kontrol eder (varsayılan: 1.0). |

**Parametre Kısıtlamalarına İlişkin Not:**
- `strength` değeri 0.0 veya daha düşükse ya da `end_percent` değeri `start_percent` değerinden küçük veya eşitse yumuşatma efekti uygulanmaz.
- `passes` parametresinin rampa seçenekleri (`ramp_2_4`, `ramp_2_4_8`), yalnızca `start_percent` ve `end_percent` bir aralık tanımladığında anlamlıdır; çünkü geçiş sayısı, örnekleme bu aralıkta ilerledikçe artar.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Dikiş yumuşatma sarmalayıcısı uygulanmış değiştirilmiş model. |

---
**Source fingerprint (SHA-256):** `f4d1a617d88f880dcae3afda25699333df023d7b4ec13a22a73512713d6ef18c`

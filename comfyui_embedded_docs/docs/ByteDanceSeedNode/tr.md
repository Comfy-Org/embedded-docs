# ByteDance Seed

ByteDance'in Seed 2.0 modelleriyle metin yanıtları oluşturun. Bir metin istemi sağlayın ve isteğe bağlı olarak modele ek bağlam vermek için görüntüleri veya videoları bağlayın. Model, mevcut Seed 2.0 varyantları arasından seçilir ve düğüm, modelin metin yanıtını döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girişi. (varsayılan: "") | STRING | Evet | N/A |
| `model` | Yanıtı oluşturmak için kullanılan Seed modeli. Bu seçici ayrıca modelin alt parametrelerini de gösterir. | DYNAMIC_COMBO | Evet | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 - 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | N/A |

### Model Girdileri (Seed 2.0 Pro, Seed 2.0 Lite ve Seed 2.0 Mini Tarafından Paylaşılır)

Seçildiğinde üç Seed modeli de aynı alt parametreleri sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, daha yüksek değerler daha rastgeledir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 2.0 (adım: 0.01) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görüntü(ler). En fazla 20 görüntü. Genişletilebilir yuva: 1..20 öğe bağlayın, örn. `image_1` ile `image_20` arası. | IMAGE | Hayır | 0 - 20 görüntü |
| `videos` | Model için bağlam olarak kullanılacak isteğe bağlı video(lar). En fazla 4 video. Genişletilebilir yuva: 1..4 öğe bağlayın, örn. `video_1` ile `video_4` arası. | VIDEO | Hayır | 0 - 4 video |

**Not:** `model` parametresi, bir model seçildiğinde referans ve temperature alt parametrelerini gösteren dinamik bir birleşik seçenektir. `images` ve `videos` yuvaları genişletilebilir, böylece çok modlu bağlam için birkaç girdi bağlayabilirsiniz.

- `prompt` gereklidir ve en az bir boşluk olmayan karakter içermelidir; aksi halde hata oluşur.
- İstek başına en fazla 20 görüntü desteklenir. Bu sınır, bağlı gruplardaki tüm görüntüleri sayar.
- İstek başına en fazla 4 video desteklenir.
- Model boş bir yanıt döndürürse veya model yanıt vermeyi reddederse hata oluşur (reddetme metni bildirilir).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Seed modelinden oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`

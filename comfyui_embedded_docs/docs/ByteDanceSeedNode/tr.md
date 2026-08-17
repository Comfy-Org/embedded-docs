# ByteDance Seed

ByteDance Seed, ByteDance'ın Seed 2.0 modellerini kullanarak metin yanıtları üretir. Bir metin istemi sağlayın ve isteğe bağlı olarak çok modlu bağlam için bir veya daha fazla görsel veya video ekleyin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı üretmek için kullanılan Seed modeli. | DYNAMIC_COMBO | Evet | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Modele metin girdisi. (varsayılan: "") | STRING | Evet | N/A |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | N/A |

### Seed 2.0 Pro, Seed 2.0 Lite ve Seed 2.0 Mini Girdileri

Bu ayar her üç model seçeneğinde de ortaktır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, daha yüksek değerler daha rastgeledir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 2.0 |

### Referans Girdileri

`model` seçici, modele çok modlu bağlam sağlamak için görselleri ve videoları bağlayan bu genişletilebilir yuvaları sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 20 görsel. Genişletilebilir yuva: 1..20 öğe bağlayın (örn. `image_1`...`image_20`). | IMAGE | Hayır | `image_1` ila `image_20` |
| `videos` | Model için bağlam olarak kullanılacak isteğe bağlı video(lar). En fazla 4 video. Genişletilebilir yuva: 1..4 öğe bağlayın (örn. `video_1`...`video_4`). | VIDEO | Hayır | `video_1` ila `video_4` |

**Not:** `model` seçici, yanıtı üretmek için hangi Seed modelinin kullanılacağını belirler. Her seçenek belirli bir model kimliğine karşılık gelir: `"Seed 2.0 Pro"` → `seed-2-0-pro-260328`, `"Seed 2.0 Lite"` → `seed-2-0-lite-260228` ve `"Seed 2.0 Mini"` → `seed-2-0-mini-260215`.

**Kısıtlamalar hakkında not:** İstek başına en fazla 20 görsel ve 4 video desteklenir. `prompt` boş olmayan bir dize olmalıdır.

**Fiyatlandırma hakkında not:** Fiyatlandırma token tabanlıdır ve düğüm arayüzünde 1K token başına yaklaşık bir aralık olarak gösterilir: Seed 2.0 Mini: $0.00025-$0.0009; Seed 2.0 Lite: $0.0003-$0.002; Seed 2.0 Pro: $0.0005-$0.003.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Seed modelinden üretilen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`

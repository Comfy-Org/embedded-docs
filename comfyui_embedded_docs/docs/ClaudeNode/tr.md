# Anthropic Claude

Bir Anthropic Claude modelinden metin yanıtları oluşturur. Bu düğüm, bir metin istemi ve isteğe bağlı görselleri bir Claude modeline gönderir ve üretilen metin yanıtını döndürür.

## Girdiler

`model` parametresi dinamik bir seçicidir: bir model seçtiğinizde, token limiti, sıcaklık ve akıl yürütme çabası gibi modele özgü ek ayarlar bunun altında görünür.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. Boşluk karakterleri kaldırıldıktan sonra boş olmamalıdır. (varsayılan: boş dize) | STRING | Evet | N/A |
| `model` | Yanıtı oluşturmak için kullanılan Claude modeli. | DYNAMIC_COMBO | Evet | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 to 2147483647 |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Genişletilebilir yuva: `image_1` ile `image_20` arasındaki yuvalara bağlayın; en fazla 20 görsel. (varsayılan: yok) | IMAGE | Hayır | 0 to 20 images |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: boş dize) | STRING | Hayır | N/A |

### Opus 5 ve Fable 5 Girdileri

Bu girdiler Opus 5 ve Fable 5 tarafından paylaşılır. Bu modeller her zaman genişletilmiş düşünme kullanır ve sıcaklık ayarı sunmaz.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirilmişse akıl yürütme token'larını da içerir). (varsayılan: 32768) | INT | Evet | 4096 to 64000 |
| `reasoning_effort` | Genişletilmiş düşünme çabası. Bu model için akıl yürütme her zaman etkindir. (varsayılan: "high") | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 ve Sonnet 5 Girdileri

Bu girdiler Opus 4.8 ve Sonnet 5 tarafından paylaşılır. Bu modeller sıcaklık ayarı sunmaz.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirilmişse akıl yürütme token'larını da içerir). (varsayılan: 32768) | INT | Evet | 4096 to 64000 |
| `reasoning_effort` | Genişletilmiş düşünme çabası. "off" akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6 ve Sonnet 4.5 Girdileri

Bu girdiler Opus 4.7, Opus 4.6, Sonnet 4.6 ve Sonnet 4.5 tarafından paylaşılır. Opus 4.7 için sıcaklık girdisi gösterilir ancak yok sayılır ve API varsayılan değer olan 1.0'ı kullanır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirilmişse akıl yürütme token'larını da içerir). (varsayılan: 32768) | INT | Evet | 4096 to 64000 |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en yüksek rastgeleliği sağlar. Opus 4.7 ve `reasoning_effort` etkinleştirilmiş herhangi bir model için yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 (step 0.01) |
| `reasoning_effort` | Genişletilmiş düşünme çabası. "off" akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 Girdileri

Bu model genişletilmiş düşünmeyi desteklemez, bu nedenle `reasoning_effort` ayarı mevcut değildir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirilmişse akıl yürütme token'larını da içerir). (varsayılan: 32768) | INT | Evet | 4096 to 64000 |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en yüksek rastgeleliği sağlar. (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 (step 0.01) |

### Parametre Kısıtlamaları

- İstek başına en fazla 20 görsel sağlanabilir. Yüklenen görsellerin toplam piksel sayısı 1568 × 1568 piksel ile sınırlıdır.
- Sıcaklık, Opus 5, Fable 5, Opus 4.8 ve Sonnet 5 için yapılandırılamaz. Sıcaklık girdisi mevcut olduğunda, Opus 4.7 için ve `reasoning_effort` değeri "off" dışında bir değere ayarlanmış herhangi bir model için yok sayılır.
- Akıl yürütme, Opus 5 ve Fable 5 için her zaman etkin olduğundan, bu modellerin `reasoning_effort` seçenekleri "off" içermez. Haiku 4.5 modeli genişletilmiş düşünmeyi desteklemez ve bu nedenle `reasoning_effort` ayarı yoktur.
- Claude bir isteği güvenlik nedenleriyle yanıtlamayı reddederse, düğüm metin döndürmek yerine bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Claude modelinden üretilen metin yanıtı. Hiçbir görünür metin üretilmezse, çıktı `"Empty response from Claude model."` olur. Düşünme veya akıl yürütme blokları çıktıya dahil edilmez. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`

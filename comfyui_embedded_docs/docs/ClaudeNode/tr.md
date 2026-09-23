# Anthropic Claude

Anthropic'in Claude modellerinden metin yanıtları oluşturun. Bir metin istemi ve isteğe bağlı olarak çok modlu bağlam için bir veya daha fazla görsel sağlayın; düğüm, modelin oluşturduğu metin yanıtını döndürür.

## Girdiler

Girdiler ortak ayarlar, bir model seçildiğinde görünen modele özgü ayarlar ve isteğe bağlı referans görselleri olarak gruplandırılır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Claude modeli. Bir model seçmek, aşağıda modele özgü ayarları görünür kılar. | DYNAMIC_COMBO | Evet | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `istem` | Modele metin girdisi. (varsayılan: boş dize) | STRING | Evet | N/A |
| `tohum` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `sistem_istemi` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: boş dize) | STRING | Hayır | N/A |

### Opus 5.5, Opus 5, Fable 5.1 ve Fable 5 Girdileri

Bu dört model aynı ayarları paylaşır. Bir sıcaklık ayarı sunmazlar ve akıl yürütme her zaman etkindir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ile 64000 arası |
| `reasoning_effort` | Genişletilmiş düşünme çabası. Bu modelde akıl yürütme her zaman etkindir. (varsayılan: "high") | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.8 ve Sonnet 5 Girdileri

Bu iki model aynı ayarları paylaşır. Bir sıcaklık ayarı sunmazlar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ile 64000 arası |
| `reasoning_effort` | Genişletilmiş düşünme çabası. `"off"` akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6 ve Sonnet 4.5 Girdileri

Bu dört model aynı ayarları paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ile 64000 arası |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en rastgeledir. Opus 4.7 ve `reasoning_effort` ayarlandığında herhangi bir model için yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `reasoning_effort` | Genişletilmiş düşünme çabası. `"off"` akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

`reasoning_effort`, dört modelin tümünde `"off"`, `"low"`, `"medium"` ve `"high"` seçeneklerini sunar. Opus 4.7, Opus 4.6 ve Sonnet 4.6 ek olarak `"max"` kabul eder; Opus 4.7 ayrıca `"xhigh"` kabul eder.

### Haiku 4.5 Girdileri

Bu model bir `reasoning_effort` ayarı sunmaz.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ile 64000 arası |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en rastgeledir. Opus 4.7 ve `reasoning_effort` ayarlandığında herhangi bir model için yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 20 görsel. Genişletilebilir yuva: 1 ile 20 öğe bağlayın (`image_1` ... `image_20`). | IMAGE | Hayır | 0 ile 20 arası images |

### Parametre Kısıtlamaları

- **Görsel sınırı:** İstek başına en fazla 20 görsel sağlanabilir. 20'den fazla görsel bağlamak bir hata oluşturur.
- **İstem gerekli:** İstem en az bir boşluk olmayan karakter içermelidir. Boş bir istem doğrulama hatası oluşturur.
- **Sıcaklık işleme:** Düşünme etkinleştirildiğinde, Anthropic API'si temperature'ın ayarlanmamış olmasını gerektirir (varsayılan olarak 1.0'dır). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5 ve Sonnet 5 bir sıcaklık ayarı sunmaz. Opus 4.7 `temperature` değerini yok sayar ve `reasoning_effort` değeri `"off"` dışında bir şeye ayarlanmış herhangi bir model de bunu yok sayar.
- **Akıl yürütme/düşünme davranışı:** `reasoning_effort` ayarı, düşünmenin etkinleştirilip etkinleştirilmeyeceğini kontrol eder. Opus 5.5, Opus 5, Fable 5.1 ve Fable 5'te akıl yürütme her zaman etkindir. Haiku 4.5 akıl yürütmeyi desteklemez. Düşünme etkinleştirildiğinde, düğüm seçilen model için uygun düşünme modunu kullanır: uyarlamalı veya bütçe tabanlı. Bütçe modunda, akıl yürütme token bütçesi, gerçek yanıt için en az 1024 token bırakacak şekilde sınırlandırılır.
- **Güvenlik reddi:** Claude güvenlik nedenleriyle isteği yanıtlamayı reddederse, düğüm sizden istemi yeniden ifade etmenizi veya farklı bir model denemenizi isteyen bir hata oluşturur.
- **Çıktı metni:** Düşünme ve akıl yürütme blokları çıktıya dahil edilmez; yalnızca oluşturulan metin döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Claude modelinden oluşturulan metin yanıtı. Düşünme/akıl yürütme blokları dahil edilmez. Metin oluşturulmazsa, "Empty response from Claude model." döndürür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/tr.md)

---
**Source fingerprint (SHA-256):** `f6d9353025598bbed1aca7bdeb56ac59f5e4c26dd5b8e29359e97ef29e35bee7`

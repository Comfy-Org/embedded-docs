# Anthropic Claude

Anthropic'in Claude modellerinden metin yanıtları oluşturun. Bir metin promptu ve isteğe bağlı olarak çok modlu bağlam için bir veya daha fazla görsel sağlayın; düğüm, modelin oluşturduğu metin yanıtını döndürür.

## Girdiler

Girdiler; ortak ayarlar, bir model seçildiğinde görünen modele özel ayarlar ve isteğe bağlı referans görselleri olarak gruplandırılmıştır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Claude modeli. Bir model seçmek, aşağıda modele özel ayarları ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `istem` | Modele metin girişi. (varsayılan: boş dize) | STRING | Evet | N/A |
| `tohum` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |
| `sistem_istemi` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: boş dize) | STRING | Hayır | N/A |

### Opus 5 ve Fable 5 Girdileri

Bu iki model aynı ayarları paylaşır. Sıcaklık (temperature) ayarı sunmazlar ve akıl yürütme her zaman etkindir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ila 64000 |
| `reasoning_effort` | Genişletilmiş düşünme çabası. Bu model için akıl yürütme her zaman etkindir. (varsayılan: "high") | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 ve Sonnet 5 Girdileri

Bu iki model aynı ayarları paylaşır. Sıcaklık ayarı sunmazlar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ila 64000 |
| `reasoning_effort` | Genişletilmiş düşünme çabası. `"off"` akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6 ve Sonnet 4.5 Girdileri

Bu dört model aynı ayarları paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ila 64000 |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en rastgeledir. Opus 4.7 için ve `reasoning_effort` ayarlandığında herhangi bir model için yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |
| `reasoning_effort` | Genişletilmiş düşünme çabası. `"off"` akıl yürütmeyi devre dışı bırakır. (varsayılan: "off") | COMBO | Evet | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 Girdileri

Bu model bir `reasoning_effort` ayarı sunmaz.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Oluşturulacak maksimum token sayısı (etkinleştirildiğinde akıl yürütme token'larını içerir). (varsayılan: 32768) | INT | Evet | 4096 ila 64000 |
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, 1.0 en rastgeledir. Opus 4.7 için ve `reasoning_effort` ayarlandığında herhangi bir model için yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 20 görsel. Büyütülebilir yuva: 1 ila 20 öğe bağlayın (`image_1` ... `image_20`). | IMAGE | Hayır | 0 ila 20 görsel |

### Parametre Kısıtlamaları

- **Görsel limiti:** Her istek için en fazla 20 görsel sağlanabilir. 20'den fazla görsel bağlamak hata verir.
- **Prompt gerekli:** Prompt en az bir boşluk dışı karakter içermelidir. Boş bir prompt doğrulama hatası verir.
- **Sıcaklık işleme:** Düşünme etkinleştirildiğinde, Anthropic API sıcaklık değerinin ayarlanmamış olmasını gerektirir (varsayılan 1.0'dır). Opus 5, Opus 4.8, Fable 5 ve Sonnet 5 bir sıcaklık ayarı sunmaz. Opus 4.7 `temperature` değerini yok sayar ve `reasoning_effort` ayarı `"low"`, `"medium"` veya `"high"` olarak ayarlanmış herhangi bir model de onu yok sayar.
- **Akıl yürütme/düşünme davranışı:** `reasoning_effort` ayarı, düşünmenin etkin olup olmadığını kontrol eder. Opus 5 ve Fable 5'te akıl yürütme her zaman etkindir. Haiku 4.5 akıl yürütmeyi desteklemez. Düşünme etkinleştirildiğinde, düğüm seçilen model için uygun düşünme modunu kullanır: uyarlanabilir veya bütçe tabanlı. Bütçe modunda, akıl yürütme token bütçesi, gerçek yanıt için en az 1024 token bırakacak şekilde sınırlandırılır.
- **Güvenlik reddi:** Claude, güvenlik nedenleriyle isteği yanıtlamayı reddederse, düğüm prompt'u yeniden ifade etmenizi veya farklı bir model denemenizi isteyen bir hata verir.
- **Çıktı metni:** Düşünme ve akıl yürütme blokları çıktıya dahil edilmez; yalnızca oluşturulan metin döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Claude modelinden oluşturulan metin yanıtı. Düşünme/akıl yürütme blokları dahil edilmez. Metin oluşturulmazsa, "Empty response from Claude model." döndürür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`

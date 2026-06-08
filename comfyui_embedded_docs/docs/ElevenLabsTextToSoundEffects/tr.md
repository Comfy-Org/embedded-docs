ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

ElevenLabs Metinden Ses Efektlerine düğümü, bir metin açıklamasından ses efektleri üretir. Ses efektlerini isteminize göre oluşturmak için ElevenLabs API'sini kullanır; süreyi, döngü davranışını ve sesin metni ne kadar yakından takip edeceğini kontrol etmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `metin` | Oluşturulacak ses efektinin metin açıklaması. Bu zorunlu bir alandır. | STRING | Evet | Yok |
| `model` | Ses efekti oluşturmak için kullanılacak model. Bu modelin seçilmesi ek parametreleri ortaya çıkarır: `duration` (varsayılan: 5.0, aralık: 0.5 ila 30.0 saniye), `loop` (varsayılan: False) ve `prompt_influence` (varsayılan: 0.3, aralık: 0.0 ila 1.0). | COMBO | Evet | `"eleven_sfx_v2"` |
| `çıktı_formatı` | Ses çıktı formatı. | COMBO | Evet | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Parametre Detayları:**

* **`model["duration"]`**: Oluşturulan sesin saniye cinsinden süresi. Varsayılan 5.0 olup, minimum 0.5 ve maksimum 30.0'dır.
* **`model["loop"]`**: Etkinleştirildiğinde, sorunsuz bir şekilde döngü yapan bir ses efekti oluşturur. Varsayılan False'dur.
* **`model["prompt_influence"]`**: Oluşturmanın metin istemini ne kadar yakından takip edeceğini kontrol eder. Daha yüksek değerler, sesin metni daha yakından takip etmesini sağlar. Varsayılan 0.3 olup, aralık 0.0 ile 1.0 arasındadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Oluşturulan ses efekti ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/tr.md)

---
**Source fingerprint (SHA-256):** `c23c4dd3c9c12f0e891d40683265c5b74b5c6320601aaadb686489510db9f107`

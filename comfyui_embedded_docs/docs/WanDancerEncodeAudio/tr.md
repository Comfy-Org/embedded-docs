# WanDancerEncodeAudio

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

## Genel Bakış

Bu düğüm, bir video oluşturma modelini yönlendirmek için kullanılabilecek özellikleri çıkarmak amacıyla bir ses girişini işler. Tempoyu, vuruşları ve diğer müzikal özellikleri tespit etmek için sesi analiz eder, ardından bu bilgiyi bir video modelini koşullandırmaya uygun bir formatta paketleyerek oluşturulan videonun sesle senkronize olmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Analiz edilecek ve kodlanacak ses girişi. | AUDIO | Evet | - |
| `video_kareleri` | Hedef videodaki kare sayısı. Senkronizasyon için kare hızını hesaplamak amacıyla kullanılır (varsayılan: 149). | INT | Evet | Min: 1, Maks: 268435456 (MAX_RESOLUTION), Adım: 4 |
| `ses_enjeksiyon_ölçeği` | Ses özelliklerinin video modeline enjekte edilirkenki ölçeği (varsayılan: 1.0). | FLOAT | Evet | Min: 0.0, Maks: 10.0, Adım: 0.01 |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder_output` | İşlenmiş ses özelliklerini, hesaplanan kare hızını (fps) ve ses enjeksiyon ölçeğini içeren bir sözlük. Bu çıktı, video oluşturma modelini koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Ses uzunluğu ve video kare sayısına göre hesaplanan kare hızını (fps) tanımlayan bir metin dizesi. Bu dize, video modeli için istemde (prompt) kullanılmak üzere tasarlanmıştır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ef230c92b23a04369708041b2e5d03c1b2928edf746dc43020bae777f9f0b589`

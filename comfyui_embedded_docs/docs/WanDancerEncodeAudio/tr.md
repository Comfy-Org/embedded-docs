> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/tr.md)

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

Bu düğüm, bir video oluşturma modelini yönlendirmek için kullanılabilecek özellikleri çıkarmak amacıyla bir ses girişini işler. Sesi analiz ederek tempo, vuruşlar ve diğer müzikal özellikleri tespit eder, ardından bu bilgileri bir video modelini koşullandırmaya uygun bir formatta paketleyerek oluşturulan videonun sesle senkronize olmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Analiz edilecek ve kodlanacak ses girişi. |
| `video_frames` | INT | Evet | Min: 1, Maks: 268435456 (MAX_RESOLUTION), Adım: 4 | Hedef videodaki kare sayısı. Senkronizasyon için kare hızını hesaplamak amacıyla kullanılır (varsayılan: 149). |
| `audio_inject_scale` | FLOAT | Evet | Min: 0.0, Maks: 10.0, Adım: 0.01 | Ses özelliklerinin video modeline enjekte edilirkenki ölçeği (varsayılan: 1.0). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | İşlenmiş ses özelliklerini, hesaplanan kare hızını (fps) ve ses enjeksiyon ölçeğini içeren bir sözlük. Bu çıkış, video oluşturma modelini koşullandırmak için kullanılır. |
| `fps_string` | STRING | Ses uzunluğu ve video kare sayısına göre hesaplanan kare hızını (fps) tanımlayan bir metin dizesi. Bu dize, video modeli için prompt'ta kullanılmak üzere tasarlanmıştır. |
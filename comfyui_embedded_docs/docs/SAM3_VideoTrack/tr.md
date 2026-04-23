> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/tr.md)

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

SAM3'ün bellek tabanlı izleyicisini kullanarak video kareleri arasında nesneleri takip edin. Bu düğüm, bir dizi video karesini işler ve nesne kimliklerini kareler arasında korur; neyin izleneceğini tanımlamak için başlangıç maskelerini veya metin istemlerini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Toplu video kareleri | Toplu görüntüler olarak video kareleri |
| `model` | MODEL | Evet | SAM3 modeli | İzleme için kullanılacak SAM3 modeli |
| `initial_mask` | MASK | Hayır | Nesne başına bir maske | İzlenecek ilk kare için maske(ler) (nesne başına bir tane). `conditioning` sağlanmamışsa zorunludur. |
| `conditioning` | CONDITIONING | Hayır | Metin koşullandırması | İzleme sırasında yeni nesneleri algılamak için metin koşullandırması. `initial_mask` sağlanmamışsa zorunludur. |
| `detection_threshold` | FLOAT | Hayır | 0.0 ile 1.0 arası (varsayılan: 0.5) | Metin istemiyle algılama için puan eşiği |
| `max_objects` | INT | Hayır | 0 ile sınırsız (varsayılan: 0) | Maksimum izlenen nesne sayısı (0=sınırsız). Başlangıç maskeleri bu sınıra dahildir. |
| `detect_interval` | INT | Hayır | 1 ile sınırsız (varsayılan: 1) | Her N karede bir algılama çalıştır (1=her kare). Daha yüksek değerler hesaplama tasarrufu sağlar. |

**Not:** `initial_mask` veya `conditioning`'den en az biri sağlanmalıdır. İkisi de atlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | Tüm video karelerindeki nesne maskelerini ve meta verilerini içeren izleme verileri |
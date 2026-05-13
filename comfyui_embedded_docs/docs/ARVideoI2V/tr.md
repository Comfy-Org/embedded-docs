> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/tr.md)

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

Bu düğüm, AR (Otoregresif) video modelleri için bir görüntüden videoya oluşturma düzeneği hazırlar. Bir başlangıç görüntüsü alır, bir VAE kullanarak bunu gizli uzaya kodlar ve kodlanmış görüntüyü modelin yapılandırmasında saklar. Bu, video örnekleme sürecinin görüntüyü ilk kare olarak kullanmasını sağlayarak, ayrı bir görüntüden videoya model mimarisine ihtiyaç duymadan oluşturmayı etkili bir şekilde başlatır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Oluşturma için kullanılacak AR video modeli. |
| `vae` | VAE | Evet | - | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `başlangıç_görseli` | IMAGE | Evet | - | Oluşturulan videonun ilk karesi olarak hizmet edecek başlangıç görüntüsü. |
| `genişlik` | INT | Evet | 16 ila 8192 (adım: 16) | Oluşturulan video karelerinin genişliği (varsayılan: 832). |
| `yükseklik` | INT | Evet | 16 ila 8192 (adım: 16) | Oluşturulan video karelerinin yüksekliği (varsayılan: 480). |
| `uzunluk` | INT | Evet | 1 ila 1024 (adım: 4) | Oluşturulan videodaki toplam kare sayısı (varsayılan: 81). |
| `toplu_boyut` | INT | Evet | 1 ila 64 | Tek bir grupta oluşturulacak video dizisi sayısı (varsayılan: 1). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Video oluşturma için yapılandırmasında kodlanmış başlangıç görüntüsü bulunan klonlanmış model. |
| `LATENT` | LATENT | Video oluşturma süreci için doğru boyutlara sahip boş bir gizli tensör. |

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`

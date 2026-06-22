# OpenAI Sora - Video

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

OpenAIVideoSora2 düğümü, OpenAI'nin Sora modellerini kullanarak videolar oluşturur. Metin istemlerine ve isteğe bağlı giriş görüntülerine dayalı video içeriği oluşturur ve ardından oluşturulan video çıktısını döndürür. Düğüm, seçilen modele bağlı olarak farklı video sürelerini ve çözünürlüklerini destekler.

**KULLANIMDAN KALDIRMA BİLDİRİMİ:** OpenAI, Eylül 2026'da Sora v2 API'sine hizmet vermeyi durduracaktır. Bu düğüm, o zaman ComfyUI'den kaldırılacaktır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak OpenAI Sora modeli (varsayılan: "sora-2") | COMBO | Evet | "sora-2"<br>"sora-2-pro" |
| `komut istemi` | Yönlendirici metin; bir giriş görüntüsü varsa boş olabilir (varsayılan: boş) | STRING | Evet | - |
| `boyut` | Oluşturulan video için çözünürlük (varsayılan: "1280x720") | COMBO | Evet | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `süre` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 8) | COMBO | Evet | 4<br>8<br>12 |
| `görsel` | Video oluşturma için isteğe bağlı giriş görüntüsü | IMAGE | Hayır | - |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar, tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

**Kısıtlamalar ve Sınırlamalar:**

- "sora-2" modeli yalnızca "720x1280" ve "1280x720" çözünürlüklerini destekler
- Görüntü parametresi kullanılırken yalnızca bir giriş görüntüsü desteklenir
- Sonuçlar, tohum değerinden bağımsız olarak deterministik değildir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video çıktısı | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/tr.md)

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`

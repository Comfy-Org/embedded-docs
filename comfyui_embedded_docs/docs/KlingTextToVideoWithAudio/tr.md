> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/tr.md)

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

Kling Metinden Videoya Sesli düğümü, bir metin açıklamasından kısa bir video oluşturur. İsteği işleyen ve bir video dosyası döndüren Kling AI hizmetine bir istek gönderir. Düğüm, metne dayalı olarak video için eşlik eden ses de oluşturabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v2-6"` | Video oluşturma için kullanılacak belirli AI modeli. |
| `prompt` | STRING | Evet | - | Olumlu metin istemi. Videoyu oluşturmak için kullanılan açıklama. 1 ile 2500 karakter arasında olmalıdır. |
| `mode` | COMBO | Evet | `"pro"` | Video oluşturma için çalışma modu. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan video için istenen genişlik-yükseklik oranı. |
| `duration` | COMBO | Evet | `5`<br>`10` | Videonun saniye cinsinden uzunluğu. |
| `generate_audio` | BOOLEAN | Hayır | - | Video için ses oluşturulup oluşturulmayacağını kontrol eder. Etkinleştirildiğinde, AI isteme dayalı olarak ses oluşturur. (varsayılan: `True`) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `eff4549816c347a090e2f6e8ae8ba832bd2c5b7aef7c729b51c9d72b7a814d5a`

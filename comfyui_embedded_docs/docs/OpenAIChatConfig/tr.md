# OpenAI ChatGPT Gelişmiş Seçenekler

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

OpenAIChatConfig düğümü, OpenAI Sohbet Düğümü için ek yapılandırma seçenekleri ayarlamanıza olanak tanır. Modelin yanıtları nasıl oluşturacağını kontrol eden, kırpma davranışı, çıktı uzunluğu sınırları ve özel talimatlar dahil olmak üzere gelişmiş ayarlar sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kırpma` | Model yanıtı için kullanılacak kırpma stratejisi. auto: Bu yanıtın ve öncekilerin bağlamı, modelin bağlam penceresi boyutunu aşarsa, model, konuşmanın ortasındaki giriş öğelerini bırakarak yanıtı bağlam penceresine sığacak şekilde kırpar. disabled: Bir model yanıtı, bir model için bağlam penceresi boyutunu aşarsa, istek 400 hatasıyla başarısız olur (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"disabled"` |
| `maksimum_çıktı_tokenları` | Bir yanıt için oluşturulabilecek token sayısı için üst sınır; görünür çıktı tokenlerini içerir (varsayılan: 4096) | INT | Hayır | 16 ila 16384 |
| `talimatlar` | Modelin yanıtı nasıl oluşturacağına dair talimatlar (çok satırlı giriş desteklenir) | STRING | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OPENAI_CHAT_CONFIG` | OpenAI Sohbet Düğümleri ile kullanılmak üzere belirtilen ayarları içeren yapılandırma nesnesi | OPENAI_CHAT_CONFIG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

---
**Source fingerprint (SHA-256):** `6d956aa1bc7f822c18ddaa55cd2345dad947fd93833de25a957f49878484af97`

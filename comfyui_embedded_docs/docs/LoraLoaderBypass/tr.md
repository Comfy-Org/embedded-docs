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

LoraLoaderBypass düğümü, bir difüzyon modeline ve bir CLIP modeline özel bir "bypass" modunda LoRA (Düşük Dereceli Uyarlama) uygular. Standart bir LoRA yükleyicisinden farklı olarak, bu yöntem temel modelin ağırlıklarını kalıcı olarak değiştirmez. Bunun yerine, LoRA'nın etkisini modelin normal ileri geçişine ekleyerek çıktıyı hesaplar; bu, eğitim sırasında veya ağırlıkları boşaltılmış modellerle çalışırken kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `clip` | LoRA'nın uygulanacağı CLIP modeli. | CLIP | Evet | - |
| `lora_name` | Uygulanacak LoRA dosyasının adı. Seçenekler `loras` klasöründen yüklenir. | COMBO | Evet | *Mevcut LoRA dosyalarının listesi* |
| `strength_model` | Difüzyon modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ila 100.0 |
| `strength_clip` | CLIP modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ila 100.0 |

**Not:** Hem `strength_model` hem de `strength_clip` 0 olarak ayarlanırsa, düğüm işleme yapmadan orijinal, değiştirilmemiş `model` ve `clip` girişlerini döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | LoRA'nın bypass modunda uygulandığı difüzyon modeli. | MODEL |
| `CLIP` | LoRA'nın bypass modunda uygulandığı CLIP modeli. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/tr.md)

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`

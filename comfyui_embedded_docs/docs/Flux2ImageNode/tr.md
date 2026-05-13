> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/tr.md)

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

Bir metin istemi ve isteğe bağlı referans görselleri kullanarak Flux.2 [pro] veya Flux.2 [max] modeli ile görseller oluşturun. Bu düğüm, isteğinizi BFL API'sine gönderir, sonucu sorgular ve oluşturulan görseli bir tensör olarak döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Görsel oluşturma veya düzenleme için istem (varsayılan: boş dize). |
| `model` | COMBO | Evet | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` | Kullanılacak Flux.2 model sürümü. Bir model seçmek, genişlik, yükseklik ve isteğe bağlı referans görselleri için ek parametrelerin kilidini açar. |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Gürültü oluşturmak için kullanılan rastgele tohum. Her oluşturmadan sonra rastgele hale getirilecek şekilde ayarlanabilir (varsayılan: 0). |

**Ek Parametreler (`model` seçimiyle etkinleştirilir):**

Bir model seçtiğinizde aşağıdaki parametreler kullanılabilir hale gelir:

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model.width` | INT | Evet | 256 ile 1440 arası | Oluşturulan görselin piksel cinsinden genişliği. |
| `model.height` | INT | Evet | 256 ile 1440 arası | Oluşturulan görselin piksel cinsinden yüksekliği. |
| `model.images` | IMAGE | Hayır | 0 ile 8 görsel arası | Oluşturmayı yönlendirmek için isteğe bağlı referans görselleri. En fazla 8 görsel desteklenir. |

**Kısıtlamalar:**
- Maksimum referans görseli sayısı 8'dir. 8'den fazla görsel sağlanırsa bir hata oluşur.
- `model.width` ve `model.height` değerleri, oluşturma maliyetini etkiler (kaynak kodundaki fiyat rozeti mantığına bakın).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | BFL API sonucundan indirilen, tensör olarak oluşturulan görsel. |

---
**Source fingerprint (SHA-256):** `664ddf45d42f64e4882cc959018f7874915325f2d46519c6bb9a0c5a501228f7`

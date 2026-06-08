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

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Görsel oluşturma veya düzenleme için istem (varsayılan: boş dize). | STRING | Evet | Yok |
| `model` | Kullanılacak Flux.2 model sürümü. Bir model seçmek, genişlik, yükseklik ve isteğe bağlı referans görselleri için ek parametrelerin kilidini açar. | COMBO | Evet | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum. Her oluşturmadan sonra rastgele hale getirilecek şekilde ayarlanabilir (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |

**Ek Parametreler (`model` seçimiyle etkinleştirilir):**

Bir model seçtiğinizde aşağıdaki parametreler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.width` | Oluşturulan görselin piksel cinsinden genişliği. | INT | Evet | 256 ile 1440 arası |
| `model.height` | Oluşturulan görselin piksel cinsinden yüksekliği. | INT | Evet | 256 ile 1440 arası |
| `model.images` | Oluşturmayı yönlendirmek için isteğe bağlı referans görselleri. En fazla 8 görsel desteklenir. | IMAGE | Hayır | 0 ile 8 görsel arası |

**Kısıtlamalar:**
- Maksimum referans görseli sayısı 8'dir. 8'den fazla görsel sağlanırsa bir hata oluşur.
- `model.width` ve `model.height` değerleri, oluşturma maliyetini etkiler (kaynak kodundaki fiyat rozeti mantığına bakın).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | BFL API sonucundan indirilen, tensör olarak oluşturulan görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `664ddf45d42f64e4882cc959018f7874915325f2d46519c6bb9a0c5a501228f7`

# Reve Görsel Oluştur

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

Reve Image Create düğümü, Reve AI modelini kullanarak metin açıklamalarından görseller oluşturur. Bir metin istemini Reve API'sine gönderir ve oluşturulan görseli döndürür. Görselin en boy oranını kontrol edebilir ve yükseltme gibi isteğe bağlı işlem sonrası efektler uygulayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | İstenen görselin metin açıklaması. Maksimum 2560 karakter. | STRING | Evet | Yok |
| `model` | Oluşturma için kullanılacak model sürümü ve en boy oranı. İlk seçenek modeli seçer, sonraki seçenekler görselin en boy oranını tanımlar. | COMBO | Evet | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `upscale` | Yükseltme işlem sonrası adımını etkinleştirir veya devre dışı bırakır. Etkinleştirildiğinde, bir yükseltme faktörü de seçmelisiniz. | COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `upscale_factor` | Görselin çözünürlüğünü artırma faktörü. Bu parametre yalnızca `upscale` `"enabled"` olarak ayarlandığında etkindir. | COMBO | Hayır | `2`<br>`3`<br>`4` |
| `remove_background` | Etkinleştirildiğinde, oluşturulan görsele arka plan kaldırma işlem sonrası adımı uygular. | BOOLEAN | Hayır | Yok |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden bir tohum değeri. Not: Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. Varsayılan: 0. | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `upscale_factor` parametresi, `upscale` parametresinin `"enabled"` olarak ayarlanmasına bağlıdır. `seed` parametresi deterministik çıktıları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Giriş istemine dayalı olarak Reve modeli tarafından oluşturulan görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/tr.md)

---
**Source fingerprint (SHA-256):** `56cb32ad254d39609d9795ca29f1ccba1db2c5a7ac5bb530475298306ec4ea19`

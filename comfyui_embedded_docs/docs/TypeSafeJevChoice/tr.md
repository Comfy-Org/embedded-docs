# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) düğümü, bağlı metin, görüntü veya her ikisi için kendi seçeneklerinizden birini seçer. `choice` çıktısını, girdileri seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya seçilen seçeneğin konumuna göre geçiş yapmak için `option_index` kullanın. Bir Branch düğümü en fazla 32 girdi alır; bu nedenle bundan daha fazla seçenek içeren bir liste yalnızca `option_index` ile yönlendirilebilir. Bu bir API düğümüdür: Comfy'nin sunucularında çalışır ve kredili bir Comfy.org hesabı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcut: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Seçeneklerin yanıtladığı soru. Birden çok görüntü yuvası olduğunda, adlarını kullanın, örneğin `Which season is shown in image_1?` (varsayılan: `What style is the image?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `options` | Aralarından seçim yapılacak seçenekler, her satırda bir tane. Her satırın başındaki ve sonundaki boşluklar kırpılır ve seçenekler büyük/küçük harf gözetmeksizin benzersiz olmalıdır; bu nedenle yinelenen bir seçenek veya yalnızca büyük/küçük harfte farklılık gösteren iki seçenek reddedilir. Hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch` ve `other`, her satırda bir tane). | STRING | Evet | 2 ile 50 seçenek arası, her biri en fazla 40 karakter |
| `images` | Sorunun hakkında olduğu görüntüler. Toplamda en fazla 32 görüntü; toplu bir girdi her görüntü için bir kez sayılır. Her görüntünün uzun kenarı, toplam görüntü sayısına göre sınırlandırılır: 4 görüntüye kadar 1568 px, 8 görüntüye kadar 1024 px, 16 görüntüye kadar 768 px ve 32 görüntüye kadar 512 px; bu nedenle daha büyük bir toplu girdi her görüntüdeki ayrıntıyı azaltabilir. | AUTOGROW | Hayır | 0 ile 32 görsel arası |
| `text` | Soruyla ilgili metin; örneğin bir istem veya LLM yanıtı. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Metin veya en az bir görüntü bağlayın; her ikisi de boş olduğunda düğüm hata verir.
- Düğüm, 2'den az veya 50'den fazla seçenek verildiğinde, bir seçenek 40 karakterden uzun olduğunda veya iki seçenek büyük/küçük harf gözetmeksizin aynı olduğunda hata verir.
- `option_index` 0'dan başlar; dolayısıyla listedeki ilk seçeneğin dizini 0'dır.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti 1 milyon token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `choice` | Seçilen seçenek; başındaki ve sonundaki boşluklar kırpılmıştır. Adı bu boşlukları koruyan bir Branch girdisi eşleşmez. | STRING |
| `option_index` | Seçilen seçeneğin seçenekler listesindeki konumu, 0'dan başlayarak. | INT |
| `confidence` | Jev'in ne kadar emin olduğu; 0 (net bir kazanan yok) ile 1 (kesin) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/tr.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`

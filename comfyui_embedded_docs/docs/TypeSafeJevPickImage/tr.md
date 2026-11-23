# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) düğümü, bir görüntü grubundan bir görüntü seçer. Seçilen görüntüyü korumak için aynı görüntü grubunu `index` ile birlikte Get Image from Batch düğümüne bağlayın veya seçimin yeterince iyi olup olmadığına karar vermek için `confidence` değerini okuyun. Bu bir API düğümüdür: Comfy sunucularında çalışır ve kredili bir Comfy.org hesabı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcut: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Hangi görüntünün seçileceği. İstem metnini `text` öğesine bağlayarak onunla en iyi eşleşen görüntüyü seçin (varsayılan: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `images` | Aralarından seçim yapılacak görüntüler. Gruplanmış bir girdi her görüntü için bir kez sayılır; bu nedenle gruptaki her görüntü bir adaydır. Yüklemeden önce her görüntünün uzun kenarı, grubun boyutuna göre sınırlandırılır: 4 görsele kadar 1568 piksel, 8'e kadar 1024 piksel, 16'ya kadar 768 piksel ve 32'ye kadar 512 piksel; bu nedenle daha büyük bir grup, her görüntüdeki ayrıntıyı azaltabilir. | IMAGE | Evet | 2 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin; örneğin görüntülerin oluşturulduğu istem. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- 2'den az veya 32'den fazla görüntü bağlandığında düğüm hata verir.
- `index` 0'dan başlar; bu, Get Image from Batch düğümünün beklediği konumdur.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti, 1M token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `index` | Seçilen görüntünün gruptaki konumu; 0'dan başlar. | INT |
| `confidence` | Jev'in ne kadar emin olduğu; 0 (net bir kazanan yok) ile 1 (kesin) arasındadır. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/tr.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`

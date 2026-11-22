# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) düğümü bir görsel yığınından bir görüntü seçer. Seçilen görüntüyü korumak için aynı görsel yığınını `index` ile birlikte Get Image from Batch düğümüne bağlayın veya seçimin yeterince iyi olup olmadığına karar vermek için `confidence` değerini okuyun. Bu bir API düğümüdür: Comfy'nin sunucularında çalışır ve kredili bir Comfy.org hesabı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcuttur: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Hangi görselin seçileceği. Metin istemini `text` öğesine bağlayarak ona en iyi uyan görseli seçin (varsayılan: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `images` | Aralarından seçim yapılacak görseller. Toplu bir girdi her görsel için bir kez sayılır, bu nedenle toplu girdideki her görsel bir adaydır. Yüklemeden önce her görüntünün uzun kenarı toplu işin boyutuna göre sınırlandırılır: 4 görsele kadar 1568 px, 8 görsele kadar 1024 px, 16 görsele kadar 768 px ve 32 görsele kadar 512 px; bu nedenle daha büyük bir toplu iş, her görüntüde daha az ayrıntı anlamına gelir. | IMAGE | Evet | 2 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin; örneğin görsellerin oluşturulduğu istem. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- Düğüm, 2'den az veya 32'den fazla görsel bağlandığında hata verir.
- `index` 0'dan başlar; bu, Get Image from Batch düğümünün beklediği konumdur.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti, 1M token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `index` | Seçilen görüntünün toplu işteki konumu; 0'dan başlar. | INT |
| `confidence` | Jev'in ne kadar emin olduğu; 0 (net bir kazanan yok) ile 1 (kesin) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/tr.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`

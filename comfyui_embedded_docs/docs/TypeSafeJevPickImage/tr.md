# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) düğümü, bir toplu iş içinden bir görüntü seçer. Seçilen görüntüyü korumak için `index` değerini Get Image from Batch düğümüne bağlayın veya seçimin yeterince iyi olup olmadığına karar vermek için `confidence` değerini okuyun. Bu bir API düğümüdür ve Comfy.org hesabı ile API anahtarı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Jev modeli. Şu anda yalnızca bir model mevcut: `jev-1.14.0`. | COMBO | Evet | `"jev-1.14.0"` |
| `question` | Hangi görüntünün seçileceği. En iyi eşleşen görüntüyü seçmek için istemi `text` parametresine bağlayın (varsayılan: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Evet | 1 ile 1000 karakter arası |
| `images` | Aralarından seçim yapılacak görüntüler. Toplu bir girdi, her görüntü için bir kez sayılır; böylece toplu işteki her görüntü bir adaydır. | IMAGE | Evet | 2 ile 32 görsel arası |
| `text` | Sorunun hakkında olduğu metin; örneğin görüntülerin oluşturulduğu istem. | STRING | Hayır | 0 ile 3000 karakter arası |

**Notlar:**

- 2'den az veya 32'den fazla görüntü bağlandığında düğüm bir hata verir.
- `index` 0'dan başlar; bu, Get Image from Batch düğümünün beklediği konumdur.
- Faturalandırma token tabanlıdır; düğümdeki fiyat rozeti, 1 milyon token başına yaklaşık ücreti gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `index` | Seçilen görüntünün toplu iş içindeki konumu; 0'dan başlar. | INT |
| `confidence` | Jev'in ne kadar emin olduğu; 0 (net bir kazanan yok) ile 1 (kesin) arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/tr.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`

# ColorTransfer

**Renk Aktarımı (ColorTransfer)**

Renk Aktarımı düğümü, hedef görüntünün renk paletini bir referans görüntünün renkleriyle eşleşecek şekilde ayarlar. Parlaklık, kontrast ve renk tonu dağılımı gibi renk özelliklerini analiz etmek ve referanstan hedefe aktarmak için farklı matematiksel algoritmalar kullanır. Bu, birden çok görüntüde görsel tutarlılık oluşturmak veya belirli bir renk derecelendirmesi uygulamak için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image_target` | Renk dönüşümünün uygulanacağı görüntü(ler). | IMAGE | Evet | - |
| `image_ref` | Renklerin eşleştirileceği referans görüntü(ler). | IMAGE | Evet | - |
| `method` | Kullanılacak renk aktarım algoritması. | COMBO | Evet | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` |
| `source_stats` | Kaynak (hedef) görüntü(ler)den renk istatistiklerinin nasıl hesaplanacağını belirler. | DYNAMICCOMBO | Evet | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` |
| `strength` | Renk aktarım efektinin yoğunluğu. 1,0 değeri tam dönüşümü uygularken, 0,0 orijinal görüntüyü döndürür. Varsayılan: 1,0 | FLOAT | Evet | 0,0 ile 10,0 |

**Parametre Detayları:**
*   **`source_stats` Seçenekleri:**
    *   **`per_frame`**: Bir topluluktaki her kare, `image_ref` ile ayrı ayrı eşleştirilir.
    *   **`uniform`**: Renk istatistikleri, tüm kaynak kareler arasında birleştirilerek tek bir temel çizgi oluşturulur ve bu temel çizgi daha sonra `image_ref` ile eşleştirilir.
    *   **`target_frame`**: `image_ref`'e dönüşümü hesaplamak için temel çizgi olarak hedef topluluktan seçilen bir kare kullanılır. Bu dönüşüm daha sonra tüm karelere tek tip olarak uygulanır, bu da aralarındaki göreceli renk farklılıklarını korur. Bu seçenek seçildiğinde, ek bir `target_index` parametresi kullanılabilir hale gelir.
*   **`target_index`** (`source_stats` `"target_frame"` olduğunda görünür): Dönüşümü hesaplamak için kaynak temel çizgi olarak kullanılan kare indeksi (0'dan başlar). Varsayılan: 0. 0 ile 10000 arasında olmalıdır.

**Kısıtlamalar:**
*   `strength` 0,0 olarak ayarlanırsa veya `image_ref` `None` ise, düğüm işleme yapmadan orijinal `image_target`'i döndürür.
*   `source_stats` `"target_frame"` olarak ayarlandığında, `target_index` `image_target` topluluğu içinde geçerli bir indeks olmalıdır. Kare sayısını aşarsa, son kare kullanılır.
*   `source_stats` `"per_frame"` olarak ayarlanmış `histogram` yöntemi için, `image_ref`'in topluluk boyutu 1'den büyükse, her hedef kare, indekse göre karşılık gelen referans kareyle eşleştirilir. Referans topluluğunun yalnızca bir karesi varsa, tüm hedef kareler için kullanılır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Renk aktarımı uygulandıktan sonra elde edilen görüntü(ler). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/tr.md)

---
**Source fingerprint (SHA-256):** `93a8447def4d2263a8a859c0474de694e6567dc6d32377032c2ddae2420bb10c`

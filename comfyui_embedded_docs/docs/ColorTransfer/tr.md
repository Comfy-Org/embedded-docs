> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/tr.md)

# ColorTransfer Düğümü

ColorTransfer düğümü, hedef görüntünün renk paletini referans görüntünün renkleriyle eşleşecek şekilde ayarlar. Parlaklık, kontrast ve renk tonu dağılımı gibi renk özelliklerini analiz etmek ve referanstan hedefe aktarmak için farklı matematiksel algoritmalar kullanır. Bu, birden çok görüntü arasında görsel tutarlılık oluşturmak veya belirli bir renk derecelendirmesi uygulamak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image_target` | IMAGE | Evet | - | Renk dönüşümünün uygulanacağı görüntü(ler). |
| `image_ref` | IMAGE | Hayır | - | Renklerin eşleştirileceği referans görüntü(ler). Sağlanmazsa, işlem atlanır ve hedef görüntü değiştirilmeden döndürülür. |
| `method` | COMBO | Evet | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` | Kullanılacak renk aktarım algoritması. |
| `source_stats` | DYNAMICCOMBO | Evet | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` | Kaynak (hedef) görüntü(ler)den renk istatistiklerinin nasıl hesaplanacağını belirler. |
| `strength` | FLOAT | Evet | 0.0 ile 10.0 arası | Renk aktarım efektinin yoğunluğu. 1.0 değeri tam dönüşümü uygularken, 0.0 orijinal görüntüyü döndürür. Varsayılan: 1.0 |

**Parametre Detayları:**
*   **`source_stats` Seçenekleri:**
    *   **`per_frame`**: Bir gruptaki her kare, `image_ref` ile ayrı ayrı eşleştirilir.
    *   **`uniform`**: Renk istatistikleri, tüm kaynak kareler arasında birleştirilerek tek bir temel oluşturulur ve bu temel `image_ref` ile eşleştirilir.
    *   **`target_frame`**: `image_ref`'e dönüşümü hesaplamak için temel olarak hedef gruptan seçilen bir kare kullanılır. Bu dönüşüm daha sonra tüm karelere tek tip olarak uygulanır ve kareler arasındaki göreceli renk farklılıklarını korur. Bu seçenek seçildiğinde, ek bir `target_index` parametresi kullanılabilir hale gelir.
*   **`target_index`** (`source_stats` `"target_frame"` olduğunda görünür): Dönüşümü hesaplamak için kaynak temel olarak kullanılan kare indeksi (0'dan başlayarak). Varsayılan: 0. 0 ile 10000 arasında olmalıdır.

**Kısıtlamalar:**
*   `image_ref` sağlanmazsa veya `strength` 0.0 olarak ayarlanırsa, düğüm işlem yapmadan orijinal `image_target`'i döndürür.
*   `source_stats` `"target_frame"` olarak ayarlandığında, `target_index` `image_target` grubu içinde geçerli bir indeks olmalıdır. Kare sayısını aşarsa, son kare kullanılır.
*   `source_stats` `"per_frame"` olarak ayarlanmış `histogram` yöntemi için, `image_ref`'in grup boyutu 1'den büyükse, her hedef kare indekse göre karşılık gelen referans kareyle eşleştirilir. Referans grubunda yalnızca bir kare varsa, tüm hedef kareler için kullanılır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Renk aktarımı uygulandıktan sonra elde edilen görüntü(ler). |
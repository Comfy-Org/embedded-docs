> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/tr.md)

ReplaceVideoLatentFrames düğümü, bir kaynak gizli videodan alınan kareleri, belirtilen bir kare indeksinden başlayarak bir hedef gizli videoya ekler. Kaynak gizli video sağlanmazsa, hedef gizli video değiştirilmeden döndürülür. Düğüm negatif indekslemeyi işler ve kaynak kareler hedef video içine sığmazsa bir uyarı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `destination` | LATENT | Evet | - | Karelerin değiştirileceği hedef gizli video. |
| `source` | LATENT | Hayır | - | Hedef gizli videoya eklenecek kareleri sağlayan kaynak gizli video. Sağlanmazsa, hedef gizli video değiştirilmeden döndürülür. |
| `index` | INT | Hayır | -MAX_RESOLUTION to MAX_RESOLUTION | Kaynak gizli video karelerinin yerleştirileceği, hedef gizli videodaki başlangıç gizli kare indeksi. Negatif değerler sondan sayılır (varsayılan: 0). |

**Kısıtlamalar:**

* `index`, hedef gizli videonun kare sayısı sınırları içinde olmalıdır. Değilse, bir uyarı kaydedilir ve hedef video değiştirilmeden döndürülür.
* Kaynak gizli video kareleri, belirtilen `index`'ten başlayarak hedef gizli video kareleri içine sığmalıdır. Sığmazsa, bir uyarı kaydedilir ve hedef video değiştirilmeden döndürülür.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Kare değiştirme işlemi sonucunda elde edilen gizli video. |

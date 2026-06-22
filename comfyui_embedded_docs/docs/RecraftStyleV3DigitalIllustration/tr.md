# Recraft Stili - Dijital İllüstrasyon

Bu düğüm, Recraft API ile kullanılmak üzere bir stil yapılandırır ve özellikle "digital_illustration" (dijital illüstrasyon) stilini seçer. Oluşturulan görüntünün sanatsal yönünü daha da hassaslaştırmak için isteğe bağlı bir alt stil seçmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `alt_stil` | Belirli bir dijital illüstrasyon türünü belirtmek için isteğe bağlı bir alt stil. Seçilmezse, temel "digital_illustration" stili kullanılır. | STRING | Hayır | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `recraft_style` | Seçilen "digital_illustration" stilini ve isteğe bağlı alt stili içeren, diğer Recraft API düğümlerine aktarılmaya hazır, yapılandırılmış bir stil nesnesi. | STYLEV3 |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/tr.md)

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`

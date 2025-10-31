> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/tr.md)

`CLIP Vision Encode` düğümü, ComfyUI'da giriş görüntülerini CLIP Vision modeli aracılığıyla görsel özellik vektörlerine dönüştürmek için kullanılan bir görüntü kodlama düğümüdür. Bu düğüm, görüntü ve metin anlama arasında önemli bir köprü görevi görür ve çeşitli AI görüntü oluşturma ve işleme iş akışlarında yaygın olarak kullanılır.

**Düğüm İşlevselliği**

- **Görüntü özellik çıkarımı**: Giriş görüntülerini yüksek boyutlu özellik vektörlerine dönüştürür
- **Çoklu ortam köprüsü**: Görüntü ve metnin birlikte işlenmesi için bir temel sağlar
- **Koşullu oluşturma**: Görüntü tabanlı koşullu oluşturma için görsel koşullar sağlar

## Girişler

| Parametre Adı | Veri Türü    | Açıklama                                                      |
| -------------- | -----------  | --------------------------------------------------------------- |
| `clip_vision`  | CLIP_VISION  | CLIP görü modeli, genellikle CLIPVisionLoader düğümü aracılığıyla yüklenir |
| `image`        | IMAGE        | Kodlanacak giriş görüntüsü                                     |
| `crop`         | Dropdown     | Görüntü kırpma yöntemi, seçenekler: center (merkezden kırpma), none (kırpma yok) |

## Çıkışlar

| Çıkış Adı         | Veri Türü           | Açıklama                |
| ------------------- | ------------------ | -------------------------- |
| CLIP_VISION_OUTPUT  | CLIP_VISION_OUTPUT | Kodlanmış görsel özellikler    |

Bu çıkış nesnesi şunları içerir:

- `last_hidden_state`: Son gizli durum
- `image_embeds`: Görüntü yerleştirme vektörü
- `penultimate_hidden_states`: Sondan bir önceki gizli durum
- `mm_projected`: Çoklu ortam projeksiyon sonucu (mevcutsa)
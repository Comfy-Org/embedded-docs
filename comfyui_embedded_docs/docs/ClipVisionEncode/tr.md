> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/tr.md)

`CLIP Vision Encode` düğümü, ComfyUI'de bulunan bir görüntü kodlama düğümüdür. CLIP Vision modeli aracılığıyla giriş görüntülerini görsel öznitelik vektörlerine dönüştürmek için kullanılır. Bu düğüm, görüntü ve metin anlayışını birbirine bağlayan önemli bir köprüdür ve çeşitli yapay zeka görüntü oluşturma ve işleme iş akışlarında yaygın olarak kullanılır.

**Düğüm İşlevi**

- **Görüntü öznitelik çıkarımı**: Giriş görüntülerini yüksek boyutlu öznitelik vektörlerine dönüştürür
- **Çok modlu köprüleme**: Görüntü ve metnin birlikte işlenmesi için bir temel sağlar
- **Koşullu oluşturma**: Görüntü tabanlı koşullu oluşturma için görsel koşullar sağlar

## Girişler

| Parametre Adı | Veri Türü    | Açıklama                                                      |
| ------------- | -----------  | ------------------------------------------------------------- |
| `clip_vision` | CLIP_VISION  | CLIP vision modeli, genellikle CLIPVisionLoader düğümü aracılığıyla yüklenir |
| `image`       | IMAGE        | Kodlanacak giriş görüntüsü                                    |
| `crop`        | Açılır Menü  | Görüntü kırpma yöntemi, seçenekler: center (merkezden kırpma), none (kırpma yok) |

## Çıktılar

| Çıktı Adı            | Veri Türü            | Açıklama                |
| -------------------- | -------------------- | ----------------------- |
| CLIP_VISION_OUTPUT   | CLIP_VISION_OUTPUT   | Kodlanmış görsel öznitelikler |

Bu çıktı nesnesi şunları içerir:

- `last_hidden_state`: Son gizli durum
- `image_embeds`: Görüntü gömme vektörü
- `penultimate_hidden_states`: Sondan bir önceki gizli durum
- `mm_projected`: Çok modlu projeksiyon sonucu (varsa)
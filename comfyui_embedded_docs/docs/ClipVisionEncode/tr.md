`CLIP Vision Encode` düğümü, ComfyUI'de bulunan bir görüntü kodlama düğümüdür. CLIP Vision modeli aracılığıyla giriş görüntülerini görsel öznitelik vektörlerine dönüştürmek için kullanılır. Bu düğüm, görüntü ve metin anlayışını birbirine bağlayan önemli bir köprüdür ve çeşitli yapay zeka görüntü oluşturma ve işleme iş akışlarında yaygın olarak kullanılır.

**Düğüm İşlevi**

- **Görüntü öznitelik çıkarımı**: Giriş görüntülerini yüksek boyutlu öznitelik vektörlerine dönüştürür
- **Çok modlu köprüleme**: Görüntü ve metnin birlikte işlenmesi için bir temel sağlar
- **Koşullu oluşturma**: Görüntü tabanlı koşullu oluşturma için görsel koşullar sağlar

## Girişler

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip_görü` | CLIP vision modeli, genellikle CLIPVisionLoader düğümü aracılığıyla yüklenir | CLIP_VISION |
| `görüntü` | Kodlanacak giriş görüntüsü | IMAGE |
| `kırp` | Görüntü kırpma yöntemi, seçenekler: center (merkezden kırpma), none (kırpma yok) | Açılır Menü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| CLIP_VISION_OUTPUT | Kodlanmış görsel öznitelikler | CLIP_VISION_OUTPUT |

Bu çıktı nesnesi şunları içerir:

- `last_hidden_state`: Son gizli durum
- `image_embeds`: Görüntü gömme vektörü
- `penultimate_hidden_states`: Sondan bir önceki gizli durum
- `mm_projected`: Çok modlu projeksiyon sonucu (varsa)

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/tr.md)

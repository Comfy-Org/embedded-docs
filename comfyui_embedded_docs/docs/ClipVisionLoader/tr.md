> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/tr.md)

Bu düğüm, `ComfyUI/models/clip_vision` klasöründe bulunan modelleri ve `extra_model_paths.yaml` dosyasında yapılandırılmış ek model yollarını otomatik olarak algılar. ComfyUI'yi başlattıktan sonra model eklerseniz, en son model dosyalarının listelenmesi için lütfen **ComfyUI arayüzünü yenileyin**.

## Girişler

| Alan         | Veri Türü       | Açıklama |
|-------------|---------------|-------------|
| `clip_adı` | COMBO[STRING]  | `ComfyUI/models/clip_vision` klasöründeki desteklenen tüm model dosyalarını listeler. |

## Çıkışlar

| Alan          | Veri Türü     | Açıklama |
|--------------|--------------|-------------|
| `clip_vision` | CLIP_VISION  | Yüklenmiş CLIP Vision modeli, görüntü kodlama veya diğer görüntüyle ilgili görevler için hazırdır. |
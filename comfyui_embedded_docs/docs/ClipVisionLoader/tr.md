> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/tr.md)

Bu düğüm, `ComfyUI/models/clip_vision` klasöründe bulunan modelleri ve `extra_model_paths.yaml` dosyasında yapılandırılan ek model yollarını otomatik olarak algılar. ComfyUI'yi başlattıktan sonra model eklerseniz, lütfen en güncel model dosyalarının listelendiğinden emin olmak için **ComfyUI arayüzünü yenileyin**.

## Girdiler

| Alan        | Veri Tipi      | Açıklama |
|-------------|---------------|-------------|
| `clip_name` | COMBO[STRING]  | `ComfyUI/models/clip_vision` klasöründeki desteklenen tüm model dosyalarını listeler. |

## Çıktılar

| Alan          | Veri Tipi    | Açıklama |
|--------------|--------------|-------------|
| `clip_vision` | CLIP_VISION  | Yüklenen CLIP Vision modeli; görüntü kodlama veya diğer görüntü ile ilgili görevler için hazır. |
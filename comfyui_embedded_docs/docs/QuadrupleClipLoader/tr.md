> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/tr.md)

**Quadruple CLIP Loader**, QuadrupleCLIPLoader, ComfyUI'nin çekirdek düğümlerinden biridir ve ilk olarak HiDream I1 sürüm modelini desteklemek için eklenmiştir. Bu düğümü bulamıyorsanız, düğüm desteğini sağlamak için ComfyUI'yi en son sürüme güncellemeyi deneyin.

4 adet CLIP modeli gerektirir; bunlar `clip_name1`, `clip_name2`, `clip_name3` ve `clip_name4` parametrelerine karşılık gelir ve sonraki düğümler için bir CLIP model çıktısı sağlayacaktır.

Bu düğüm, `ComfyUI/models/text_encoders` klasöründe bulunan modelleri algılayacak ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardan modelleri okuyacaktır. Bazen modelleri ekledikten sonra, ilgili klasördeki model dosyalarını okuyabilmesi için **ComfyUI arayüzünü yeniden yüklemeniz** gerekebilir.
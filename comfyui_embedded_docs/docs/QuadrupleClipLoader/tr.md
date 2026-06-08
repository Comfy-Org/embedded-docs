**Quadruple CLIP Loader (Dörtlü CLIP Yükleyici)**

QuadrupleCLIPLoader, ComfyUI'nin temel düğümlerinden biridir ve ilk olarak HiDream I1 sürüm modelini desteklemek için eklenmiştir. Bu düğümü eksik bulursanız, düğüm desteğini sağlamak için ComfyUI'yi en son sürüme güncellemeyi deneyin.

`clip_name1`, `clip_name2`, `clip_name3` ve `clip_name4` parametrelerine karşılık gelen 4 CLIP modeli gerektirir ve sonraki düğümler için bir CLIP model çıktısı sağlar.

Bu düğüm, `ComfyUI/models/text_encoders` klasöründe bulunan modelleri algılar ve ayrıca extra_model_paths.yaml dosyasında yapılandırılan ek yollardaki modelleri de okur. Bazen, model ekledikten sonra, ilgili klasördeki model dosyalarını okuması için **ComfyUI arayüzünü yeniden yüklemeniz** gerekebilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/tr.md)

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

LatentApplyOperationCFG düğümü, bir modeldeki koşullandırma kılavuzluk sürecini değiştirmek için bir gizli işlem uygular. Sınıflandırıcısız kılavuzluk (CFG) örnekleme süreci sırasında koşullandırma çıktılarını keserek ve üretim için kullanılmadan önce gizli temsillere belirtilen işlemi uygulayarak çalışır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | CFG işleminin uygulanacağı model |
| `işlem` | LATENT_OPERATION | Evet | - | CFG örnekleme süreci sırasında uygulanacak gizli işlem |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Örnekleme sürecine CFG işlemi uygulanmış modifiye edilmiş model |
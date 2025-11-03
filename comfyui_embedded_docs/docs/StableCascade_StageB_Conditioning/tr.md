> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/tr.md)

StableCascade_StageB_Conditioning düğümü, mevcut koşullandırma bilgilerini Stage C'den gelen önceki gizli temsillerle birleştirerek Stable Cascade Stage B üretimi için koşullandırma verilerini hazırlar. Stage C'den gelen gizli örnekleri içerecek şekilde koşullandırma verilerini değiştirerek, üretim sürecinin daha tutarlı çıktılar için önceki bilgilerden yararlanmasını sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `koşullandırma` | CONDITIONING | Evet | - | Stage C önceki bilgileri ile değiştirilecek koşullandırma verisi |
| `aşama_c` | LATENT | Evet | - | Koşullandırma için önceki örnekleri içeren Stage C'den gelen gizli temsil |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Stage C önceki bilgileri entegre edilmiş değiştirilmiş koşullandırma verisi |
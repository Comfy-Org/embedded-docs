> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/tr.md)

Create Hook Keyframe düğümü, bir oluşturma sürecinde hook davranışının değiştiği belirli noktaları tanımlamanıza olanak sağlar. Oluşturma ilerlemesinin belirli yüzdeliklerinde hook gücünü değiştiren kare animasyonları oluşturur ve bu kare animasyonları karmaşık zamanlama desenleri oluşturmak için birbirine zincirlenebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `strength_mult` | FLOAT | Evet | -20.0 - 20.0 | Bu kare animasyonundaki hook gücü için çarpan (varsayılan: 1.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | Bu kare animasyonunun etkili olduğu oluşturma sürecindeki yüzdelik nokta (varsayılan: 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Hayır | - | Bu kare animasyonunu eklemek için isteğe bağlı önceki hook kare animasyonu grubu |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Yeni oluşturulan kare animasyonunu da içeren bir hook kare animasyonları grubu |
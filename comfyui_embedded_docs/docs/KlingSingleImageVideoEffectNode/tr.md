> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/tr.md)

Kling Single Image Video Effect Node, tek bir referans görseline dayalı olarak farklı özel efektler içeren videolar oluşturur. Statik görselleri dinamik video içeriğine dönüştürmek için çeşitli görsel efektler ve sahneler uygular. Node, istenen görsel sonucu elde etmek için farklı efekt sahnelerini, model seçeneklerini ve video sürelerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Referans Görseli. URL veya Base64 kodlanmış dize (data:image öneki olmadan). Dosya boyutu 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. |
| `efekt_sahnesi` | COMBO | Evet | KlingSingleImageEffectsScene'dan Seçenekler | Video oluşturmaya uygulanacak özel efekt sahnesinin türü |
| `model_adı` | COMBO | Evet | KlingSingleImageEffectModelName'dan Seçenekler | Video efekti oluşturmak için kullanılacak belirli model |
| `süre` | COMBO | Evet | KlingVideoGenDuration'dan Seçenekler | Oluşturulan videonun uzunluğu |

**Not:** `effect_scene`, `model_name` ve `duration` parametrelerine ait belirli seçenekler, ilgili enum sınıflarında (KlingSingleImageEffectsScene, KlingSingleImageEffectModelName ve KlingVideoGenDuration) mevcut değerler tarafından belirlenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Uygulanan efektlerle oluşturulan video |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `süre` | STRING | Oluşturulan videonun süresi |
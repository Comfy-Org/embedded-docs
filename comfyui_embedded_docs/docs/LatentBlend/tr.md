> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/tr.md)

LatentBlend düğümü, iki latent örneğini belirtilen bir karıştırma faktörü kullanarak birleştirir. İki latent girdisi alır ve ilk örneğin karıştırma faktörüyle, ikinci örneğin ise bunun tersiyle ağırlıklandırıldığı yeni bir çıktı oluşturur. Girdi örnekleri farklı şekillere sahipse, ikinci örnek otomatik olarak ilk örneğin boyutlarına göre yeniden boyutlandırılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Evet | - | Karıştırılacak ilk latent örnek |
| `samples2` | LATENT | Evet | - | Karıştırılacak ikinci latent örnek |
| `blend_factor` | FLOAT | Evet | 0 ile 1 | İki örnek arasındaki karıştırma oranını kontrol eder (varsayılan: 0.5) |

**Not:** Eğer `samples1` ve `samples2` farklı şekillere sahipse, `samples2`, merkez kırpma ile bikübik enterpolasyon kullanılarak otomatik olarak `samples1`'in boyutlarına uyacak şekilde yeniden boyutlandırılacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | Her iki girdi örneğinin birleştirilmiş hali olan latent örnek |
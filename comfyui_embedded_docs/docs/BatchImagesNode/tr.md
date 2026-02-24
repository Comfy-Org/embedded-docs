> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/tr.md)

Batch Images düğümü, birden fazla ayrı görüntüyü tek bir toplu işte birleştirir. Değişken sayıda görüntü girişi alır ve bunları tek bir toplu görüntü tensörü olarak çıktılar, böylece sonraki düğümlerde birlikte işlenebilmelerini sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | 2 ila 50 giriş | Dinamik bir görüntü girişleri listesi. Toplu iş haline getirilmek üzere 2 ila 50 arasında görüntü ekleyebilirsiniz. Düğüm arayüzü, gerektiğinde daha fazla görüntü giriş yuvası eklemenize olanak tanır. |

**Not:** Düğümün çalışması için en az iki görüntü bağlamalısınız. İlk giriş yuvası her zaman zorunludur ve düğüm arayüzünde görünen "+" düğmesini kullanarak daha fazla ekleyebilirsiniz.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Tüm giriş görüntülerinin üst üste istiflendiği tek bir toplu görüntü tensörü. |

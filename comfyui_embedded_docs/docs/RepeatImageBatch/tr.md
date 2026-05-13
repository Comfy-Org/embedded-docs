> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/tr.md)

RepeatImageBatch düğümü, belirtilen bir görseli belirli sayıda çoğaltarak aynı görsellerden oluşan bir grup oluşturmak üzere tasarlanmıştır. Bu işlevsellik, toplu işleme veya veri artırma gibi aynı görselin birden fazla örneğini gerektiren işlemler için kullanışlıdır.

## Girişler

| Alan    | Veri Türü | Açıklama                                                                 |
|---------|-------------|-------------------------------------------------------------------------|
| `image` | `IMAGE`     | 'image' parametresi, çoğaltılacak görseli temsil eder. Grup boyunca kopyalanacak içeriğin tanımlanması açısından kritik öneme sahiptir. |
| `amount`| `INT`       | 'amount' parametresi, giriş görselinin kaç kez çoğaltılacağını belirtir. Çıktı grubunun boyutunu doğrudan etkileyerek esnek grup oluşturulmasını sağlar. |

## Çıktılar

| Alan  | Veri Türü | Açıklama                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | Çıktı, her biri giriş görseliyle aynı olan ve belirtilen 'amount' değerine göre çoğaltılmış bir görsel grubudur. |
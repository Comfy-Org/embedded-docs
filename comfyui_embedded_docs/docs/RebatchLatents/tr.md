> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/tr.md)

RebatchLatents düğümü, bir grup gizli temsili (latent representation), belirtilen bir grup boyutuna (batch size) göre yeni bir grup konfigürasyonunda yeniden düzenlemek için tasarlanmıştır. Gizli örneklerin, boyut ve ölçü farklılıkları ele alınarak uygun şekilde gruplandırılmasını sağlar ve böylece ileri işleme veya model çıkarımını (inference) kolaylaştırır.

## Girdiler

| Parametre    | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `gizli_değişkenler`    | `LATENT`    | 'latents' parametresi, yeniden gruplandırılacak olan girdi gizli temsillerini ifade eder. Çıktı grubunun yapısını ve içeriğini belirlemede çok önemlidir. |
| `toplu_boyut` | `INT`      | 'batch_size' parametresi, çıktıdaki her grup başına istenen örnek sayısını belirtir. Girdi gizli temsillerinin yeni gruplara ayrılmasını ve gruplandırılmasını doğrudan etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen grup boyutuna göre ayarlanmış, yeniden düzenlenmiş bir gizli temsil grubudur. İleri işlemeyi veya analizi kolaylaştırır. |
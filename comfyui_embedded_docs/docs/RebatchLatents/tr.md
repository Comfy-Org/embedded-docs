> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/tr.md)

RebatchLatents düğümü, belirtilen bir grup boyutuna göre bir dizi gizli temsili (latent representation) yeniden düzenleyerek yeni bir grup yapılandırması oluşturmak üzere tasarlanmıştır. Bu düğüm, gizli örneklerin boyut ve ölçü farklılıklarını yöneterek uygun şekilde gruplandırılmasını sağlar ve böylece ileri işleme veya model çıkarımını kolaylaştırır.

## Girişler

| Parametre     | Veri Türü | Açıklama |
|---------------|-------------|-------------|
| `gizli_değişkenler`     | `LATENT`    | 'latents' parametresi, yeniden gruplandırılacak giriş gizli temsillerini temsil eder. Çıktı grubunun yapısını ve içeriğini belirlemede kritik öneme sahiptir. |
| `toplu_boyut`  | `INT`       | 'batch_size' parametresi, çıktıda grup başına istenen örnek sayısını belirtir. Giriş gizli temsillerinin yeni gruplara ayrılmasını ve gruplandırılmasını doğrudan etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen grup boyutuna göre ayarlanmış, yeniden düzenlenmiş bir gizli temsil grubudur. İleri işleme veya analizi kolaylaştırır. |
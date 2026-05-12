> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/tr.md)

## Genel Bakış

VOIDSampler düğümü, özellikle VOID iç boyama (inpainting) modelleri için tasarlanmış özel bir DDIM örnekleme yöntemi sunar. Standart KSampler düğümlerinin uyguladığı gürültü ölçekleme olmaksızın, VOID model eğitimi sırasında kullanılan aynı gürültü giderme (denoising) sürecini uygular. Bu düğüm, SamplerCustom veya SamplerCustomAdvanced düğümleriyle birlikte kullanılmak üzere tasarlanmıştır ve RandomNoise veya VOIDWarpedNoiseSource ile eşleştirilmelidir.

## Girdiler

Bu düğümün yapılandırılabilir giriş parametresi yoktur. Sabit bir DDIM örnekleme algoritması uygulayan, kendi kendine yeterli bir örnekleyicidir.

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| *Giriş yok* | - | - | - | Bu düğüm herhangi bir giriş parametresi kabul etmez. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `SAMPLER` | SAMPLER | VOID DDIM algoritmasını uygulayan, SamplerCustom veya SamplerCustomAdvanced düğümlerine bağlanmaya hazır bir örnekleyici nesnesi. |
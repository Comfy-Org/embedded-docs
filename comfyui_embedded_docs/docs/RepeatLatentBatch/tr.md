> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/tr.md)

RepeatLatentBatch düğümü, belirli sayıda gizli temsil grubunu çoğaltmak ve gerektiğinde gürültü maskeleri ve grup indeksleri gibi ek verileri dahil etmek üzere tasarlanmıştır. Bu işlevsellik, veri büyütme veya belirli üretim görevleri gibi aynı gizli verinin birden fazla örneğini gerektiren işlemler için hayati öneme sahiptir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `örnekler` | `LATENT`    | 'samples' parametresi, çoğaltılacak olan gizli temsilleri temsil eder. Tekrarlanacak veriyi tanımlamak için esastır. |
| `miktar`  | `INT`       | 'amount' parametresi, girdi örneklerinin kaç kez tekrarlanacağını belirtir. Çıktı grubunun boyutunu doğrudan etkileyerek hesaplama yükünü ve üretilen verinin çeşitliliğini etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, girdi olarak verilen gizli temsillerin, belirtilen 'amount' değerine göre çoğaltılmış halidir. Uygulanabilir olduğu durumlarda, çoğaltılmış gürültü maskelerini ve ayarlanmış grup indekslerini içerebilir. |
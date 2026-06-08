RepeatLatentBatch düğümü, belirtilen bir latent temsil grubunu, istenen sayıda çoğaltmak için tasarlanmıştır; buna gürültü maskeleri ve grup indeksleri gibi ek veriler de dahil olabilir. Bu işlevsellik, veri artırma veya belirli üretken görevler gibi aynı latent verinin birden fazla örneğini gerektiren işlemler için kritik öneme sahiptir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, çoğaltılacak latent temsilleri temsil eder. Tekrarlanacak veriyi tanımlamak için gereklidir. | `LATENT` |
| `miktar` | 'amount' parametresi, giriş örneklerinin kaç kez tekrarlanması gerektiğini belirtir. Çıktı grubunun boyutunu doğrudan etkileyerek hesaplama yükünü ve üretilen verinin çeşitliliğini etkiler. | `INT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, belirtilen 'amount' değerine göre çoğaltılmış, giriş latent temsillerinin değiştirilmiş bir sürümüdür. Varsa, çoğaltılmış gürültü maskelerini ve ayarlanmış grup indekslerini içerebilir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/tr.md)

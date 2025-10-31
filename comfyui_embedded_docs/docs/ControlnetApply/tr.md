> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/tr.md)

ControlNet kullanımı, girdi görsellerinin ön işleme tabi tutulmasını gerektirir. ComfyUI'nin başlangıç düğümleri ön işlemciler ve ControlNet modelleri ile birlikte gelmediğinden, lütfen öncelikle ControlNet ön işlemcilerini [ön işlemcileri buradan indirin](https://github.com/Fannovel16/comfy_controlnet_preprocessors) ve ilgili ControlNet modellerini yükleyin.

## Girdiler

| Parametre | Veri Türü | İşlev |
| --- | --- | --- |
| `positive` | `CONDITIONING` | CLIP Metin Kodlayıcı veya diğer koşullandırma girdilerinden gelen pozitif koşullandırma verisi |
| `negative` | `CONDITIONING` | CLIP Metin Kodlayıcı veya diğer koşullandırma girdilerinden gelen negatif koşullandırma verisi |
| `kontrol_ağı` | `CONTROL_NET` | Uygulanacak ControlNet modeli, genellikle ControlNet Yükleyici'den girdi olarak alınır |
| `görüntü` | `IMAGE` | ControlNet uygulaması için görsel, ön işlemci tarafından işlenmiş olması gerekir |
| `vae` | `VAE` | VAE model girdisi |
| `güç` | `FLOAT` | Ağ ayarlamalarının gücünü kontrol eder, değer aralığı 0~10. 0.5~1.5 arasındaki değerlerin makul olduğu önerilir. Düşük değerler modele daha fazla özgürlük tanırken, yüksek değerler daha katı kısıtlamalar uygular. Çok yüksek değerler garip görsellerle sonuçlanabilir. Control ağının etkisini ince ayar yapmak için bu değeri test edip ayarlayabilirsiniz. |
| `start_percent` | `FLOAT` | 0.000~1.000 değeri, ControlNet uygulamasının yüzde olarak ne zaman başlayacağını belirler, örneğin 0.2 değeri ControlNet rehberliğinin difüzyon sürecinin %20'sinde görsel oluşumunu etkilemeye başlayacağı anlamına gelir |
| `end_percent` | `FLOAT` | 0.000~1.000 değeri, ControlNet uygulamasının yüzde olarak ne zaman duracağını belirler, örneğin 0.8 değeri ControlNet rehberliğinin difüzyon sürecinin %80'inde görsel oluşumunu etkilemeyi bırakacağı anlamına gelir |

## Çıktılar

| Parametre | Veri Türü | İşlev |
| --- | --- | --- |
| `positive` | `CONDITIONING` | ControlNet tarafından işlenmiş pozitif koşullandırma verisi, bir sonraki ControlNet veya K Sampler düğümlerine çıktı olarak verilebilir |
| `negative` | `CONDITIONING` | ControlNet tarafından işlenmiş negatif koşullandırma verisi, bir sonraki ControlNet veya K Sampler düğümlerine çıktı olarak verilebilir |
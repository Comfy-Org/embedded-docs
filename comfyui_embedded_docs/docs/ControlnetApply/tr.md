ControlNet kullanımı, giriş görüntülerinin ön işlenmesini gerektirir. ComfyUI'nin başlangıç düğümleri ön işlemciler ve ControlNet modelleri ile gelmediğinden, lütfen öncelikle ControlNet ön işlemcilerini [ön işlemcileri buradan indirin](https://github.com/Fannovel16/comfy_controlnet_preprocessors) ve ilgili ControlNet modellerini yükleyin.

## Girişler

| Parametre | Veri Türü | İşlev |
| --- | --- | --- |
| `positive` | `CONDITIONING` | CLIP Metin Kodlayıcı veya diğer koşullandırma girişlerinden gelen pozitif koşullandırma verileri |
| `negative` | `CONDITIONING` | CLIP Metin Kodlayıcı veya diğer koşullandırma girişlerinden gelen negatif koşullandırma verileri |
| `kontrol_ağı` | `CONTROL_NET` | Uygulanacak ControlNet modeli, genellikle ControlNet Yükleyici'den gelen giriş |
| `görüntü` | `IMAGE` | ControlNet uygulaması için görüntü, ön işlemci tarafından işlenmesi gerekir |
| `vae` | `VAE` | VAE model girişi |
| `güç` | `FLOAT` | Ağ ayarlamalarının gücünü kontrol eder, değer aralığı 0~10. Önerilen değerler 0.5~1.5 arası makuldür. Düşük değerler modele daha fazla özgürlük tanır, yüksek değerler daha katı kısıtlamalar uygular. Çok yüksek değerler garip görüntülere neden olabilir. Kontrol ağının etkisini ince ayarlamak için bu değeri test edip ayarlayabilirsiniz. |
| `start_percent` | `FLOAT` | Değer 0.000~1.000, ControlNet uygulamasının başlama zamanını yüzde olarak belirler, örn. 0.2, ControlNet yönlendirmesinin difüzyon sürecinin %20'sinde görüntü oluşturmayı etkilemeye başlayacağı anlamına gelir |
| `end_percent` | `FLOAT` | Değer 0.000~1.000, ControlNet uygulamasının durma zamanını yüzde olarak belirler, örn. 0.8, ControlNet yönlendirmesinin difüzyon sürecinin %80'inde görüntü oluşturmayı etkilemeyi bırakacağı anlamına gelir |

### Çıktılar

| Parametre | Veri Türü | İşlev |
| --- | --- | --- |
| `positive` | `CONDITIONING` | ControlNet tarafından işlenmiş pozitif koşullandırma verileri, sonraki ControlNet veya K Örnekleyici düğümlerine çıktı olarak verilebilir |
| `negative` | `CONDITIONING` | ControlNet tarafından işlenmiş negatif koşullandırma verileri, sonraki ControlNet veya K Örnekleyici düğümlerine çıktı olarak verilebilir |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/tr.md)

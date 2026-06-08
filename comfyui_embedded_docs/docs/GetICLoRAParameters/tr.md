## Genel Bakış

Bu düğüm, bir LoRA yüklenmiş modelin meta verilerinden IC-LoRA parametrelerini çıkarır. Referans küçültme faktörü gibi değerleri bulmak için safetensors meta verilerini okur ve bunları yapılandırılmış bir parametre nesnesi olarak çıktılar; bu nesne, özel kılavuz işleme için LTXVAddGuide düğümüne bağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `iclora_model` | Meta verilerin çıkarılacağı belirli IC-LoRA için bir LoRA Yükleyici'den doğrudan çıktı. | MODEL | Evet | Yok |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `iclora_parameters` | LoRA meta verilerinden çıkarılan IC-LoRA parametreleri (örneğin, reference_downscale_factor). LoRA, kılavuzların özel işlenmesini gerektiriyorsa LTXVAddGuide'a bağlayın. | IC_LORA_PARAMETERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/tr.md)

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`

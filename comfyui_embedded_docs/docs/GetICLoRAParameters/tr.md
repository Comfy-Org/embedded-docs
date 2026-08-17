# IC-LoRA Parametrelerini Al

## Genel Bakış

Bu düğüm, LoRA yüklü bir modelin meta verilerinden IC-LoRA parametrelerini çıkarır. Safetensors meta verilerini okuyarak referans küçültme faktörü gibi değerleri bulur ve bunları yapılandırılmış bir parametre nesnesi olarak çıkarır; bu nesne, özel kılavuz işleme için LTXVAddGuide düğümüne bağlanabilir. Meta veriler eksikse veya referans küçültme faktörü okunamazsa değer varsayılan olarak 1 olur; bulunduğunda ise değer yuvarlanır ve minimum 1 olacak şekilde sınırlandırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `iclora_model` | Meta verileri çıkarılacak belirli IC-LoRA'ya ait bir LoRA Loader'ın doğrudan çıktısı. | MODEL | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `iclora_parameters` | LoRA meta verilerinden çıkarılan IC-LoRA parametreleri (örn. reference_downscale_factor). LoRA, kılavuzların özel işlenmesini gerektiriyorsa LTXVAddGuide düğümüne bağlayın. | IC_LORA_PARAMETERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/tr.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`

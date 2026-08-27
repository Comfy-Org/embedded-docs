# IC-LoRA Parametrelerini Al

Bu düğüm, LoRA yüklü bir modelden meta verileri okuyarak referans küçültme faktörü gibi IC-LoRA parametrelerini çıkarır. Bu parametreleri, bir LoRA'nın kılavuzlar için özel işlem gerektirmesi durumunda LTXVAddGuide düğümüne bağlanabilen yapılandırılmış bir nesne olarak çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `iclora_model` | Meta verilerinin çıkarılacağı belirli IC-LoRA için bir LoRA Yükleyici'nin doğrudan çıktısı. | MODEL | Evet | N/A |

Not: LoRA meta verileri eksikse veya `reference_downscale_factor` girişi içermiyorsa, düğüm varsayılan değer olarak 1 çıktısı verir. Faktör mevcut olduğunda yuvarlanır ve minimum 1 olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `iclora_parameters` | LoRA meta verilerinden çıkarılan IC-LoRA parametreleri (örn. reference_downscale_factor). LoRA'nın kılavuzlar için özel işlem gerektirmesi durumunda LTXVAddGuide düğümüne bağlayın. | IC_LORA_PARAMETERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/tr.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`

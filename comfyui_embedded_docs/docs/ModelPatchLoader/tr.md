# ModelPatchLoader

ModelPatchLoader düğümü, `model_patches` klasöründen bir model yama dosyası yükler ve bunu bir iş akışında kullanılmak üzere hazırlar. Dosyada bulunan yama türünü otomatik olarak algılar, eşleşen mimariyi oluşturur, kaydedilmiş ağırlıkları yükler ve her şeyi bir model yamalayıcı içine sarar; böylece diğer modellere uygulanabilir. Ek ControlNet dalları, özellik gömücü modeller, bağdaştırıcılar, animasyon/LLLite rehberlik modülleri ve benzer modüller dahil olmak üzere birçok özel yama biçimini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `name` | `model_patches` klasöründen yüklenecek model yamasının dosya adı. Listeden mevcut yama dosyalarından birini seçin. | COMBO | Evet | `model_patches` klasöründe bulunan tüm model yama dosyalarının dinamik olarak oluşturulan listesi |

Not: Bu düğüm deneysel olarak işaretlenmiştir. Yama türü dosya içeriğinden otomatik olarak algılanır, bu nedenle manuel tür seçimi gerekmez. Düğüm, checkpoint meta verilerini okur ve hangi mimarinin oluşturulacağına karar vermek için ağırlık anahtarlarını inceler (örneğin Qwen Image blok tabanlı ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP özellik projeksiyonu, Lightricks duration head, Anima LLLite, MultiTalk veya SUPIR). Ağırlıklar güvenli yükleme etkin olarak yüklenir ve model, daha sonra başka bir modele uygulanabilmesi için bir `CoreModelPatcher` içindeki offload aygıtına yerleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL_PATCH` | Bir model yamalayıcı içine sarılmış yüklenmiş model yaması; iş akışındaki bir modele uygulanmaya hazırdır | MODEL_PATCH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`

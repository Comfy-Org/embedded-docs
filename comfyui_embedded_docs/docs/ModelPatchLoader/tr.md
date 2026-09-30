# ModelPatchLoader

ModelPatchLoader düğümü, `model_patches` klasöründen bir model yama dosyası yükler ve bunu bir iş akışında kullanıma hazırlar. Dosyada bulunan yama türünü otomatik olarak algılar, eşleşen mimariyi oluşturur, kaydedilmiş ağırlıkları yükler ve her şeyi diğer modellere uygulanabilmesi için bir model yamalayıcıya sarar. Ek ControlNet dalları, özellik gömücü modelleri, adaptörler, animasyon/LLLite yönlendirme modülleri ve benzer modüller dahil olmak üzere birçok özel yama biçimini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ad` | `model_patches` klasöründen yüklenecek model yamasının dosya adı. Listeden mevcut yama dosyalarından birini seçin. | COMBO | Evet | `model_patches` klasöründe bulunan tüm model yama dosyalarının dinamik olarak oluşturulan listesi |

Not: Bu düğüm deneysel olarak işaretlenmiştir. Yama türü, dosya içeriğinden otomatik olarak algılanır, bu nedenle elle tür seçimi gerekmez. Düğüm, checkpoint meta verilerini okur ve hangi mimarinin oluşturulacağına karar vermek için ağırlık anahtarlarını inceler (örneğin Qwen Image blok bazlı ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP özellik projeksiyonu, Lightricks süre başlığı, Anima LLLite, MultiTalk veya SUPIR). Ağırlıklar güvenli yükleme etkinken yüklenir ve model, daha sonra başka bir modele uygulanabilmesi için `CoreModelPatcher` içinde offload aygıtına yerleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL_PATCH` | Bir model yamalayıcıya sarılmış, iş akışındaki bir modele uygulanmaya hazır yüklenmiş model yaması | MODEL_PATCH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`

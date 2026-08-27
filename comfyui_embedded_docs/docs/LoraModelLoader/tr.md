# LoRA Modeli Yükle

LoraModelLoader düğümü, eğitilmiş LoRA (Low-Rank Adaptation) ağırlıklarını bir difüzyon modeline uygular. Eğitilmiş bir LoRA modelinden LoRA ağırlıklarını yükleyip etki güçlerini ayarlayarak temel modeli değiştirir. Bu, difüzyon modellerinin davranışını sıfırdan yeniden eğitmeden özelleştirmenize olanak tanır; ayrıca temel model ağırlıklarını değiştirmeden bırakan bir bypass modunu da içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `lora` | Difüzyon modeline uygulanacak LoRA modeli. | LORA_MODEL | Evet | - |
| `model_gücü` | Difüzyon modelinin ne kadar güçlü değiştirileceğini belirler. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ile 100.0 |
| `bypass` | Etkinleştirildiğinde, temel model ağırlıklarını değiştirmeden LoRA'yı bypass modunda uygular. Eğitim sırasında ve model ağırlıkları boşaltıldığında kullanışlıdır (varsayılan: False). | BOOLEAN | Evet | True or False |

**Not:** `strength_model` 0 olarak ayarlandığında, düğüm herhangi bir LoRA değişikliği uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LoRA ağırlıkları uygulanmış değiştirilmiş difüzyon modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`

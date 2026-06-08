LoraModelLoader düğümü, eğitilmiş LoRA (Düşük Dereceli Uyarlama) ağırlıklarını bir difüzyon modeline uygular. Eğitilmiş bir LoRA modelinden LoRA ağırlıklarını yükleyerek ve bunların etki gücünü ayarlayarak temel modeli değiştirir. Bu, difüzyon modellerini sıfırdan yeniden eğitmeye gerek kalmadan davranışlarını özelleştirmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `lora` | Difüzyon modeline uygulanacak LoRA modeli. | LORA_MODEL | Evet | - |
| `model_gücü` | Difüzyon modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1,0). | FLOAT | Evet | -100,0 ila 100,0 |
| `bypass` | Etkinleştirildiğinde, LoRA'yı temel model ağırlıklarını değiştirmeden bypass modunda uygular. Eğitim ve model ağırlıklarının boşaltıldığı durumlar için kullanışlıdır (varsayılan: Yanlış). | BOOLEAN | Evet | Doğru veya Yanlış |

**Not:** `strength_model` 0 olarak ayarlandığında, düğüm herhangi bir LoRA değişikliği uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | LoRA ağırlıkları uygulanmış değiştirilmiş difüzyon modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`

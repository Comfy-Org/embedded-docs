> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/tr.md)

LoraModelLoader düğümü, eğitilmiş LoRA (Düşük Dereceli Uyarlama) ağırlıklarını bir difüzyon modeline uygular. Temel modeli, eğitilmiş bir LoRA modelinden LoRA ağırlıklarını yükleyerek ve bunların etki gücünü ayarlayarak değiştirir. Bu, difüzyon modellerinin davranışını sıfırdan yeniden eğitmeden özelleştirmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | LoRA'nın uygulanacağı difüzyon modeli. |
| `lora` | LORA_MODEL | Evet | - | Difüzyon modeline uygulanacak LoRA modeli. |
| `strength_model` | FLOAT | Evet | -100.0 - 100.0 | Difüzyon modelinin ne kadar güçlü bir şekilde değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). |

**Not:** `strength_model` değeri 0 olarak ayarlandığında, düğüm herhangi bir LoRA değişikliği uygulamadan orijinal modeli döndürür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | LoRA ağırlıkları uygulanmış, değiştirilmiş difüzyon modeli. |
# LoRA Yükle (Bypass) (Hata Ayıklama İçin)

LoraLoaderBypass düğümü, özel bir bypass modunda bir difüzyon modeline ve bir CLIP modeline LoRA (Düşük Dereceli Uyarlama) uygular. Standart bir LoRA yükleyicisinden farklı olarak, temel model ağırlıklarını kalıcı olarak değiştirmez. Bunun yerine, LoRA'nın etkisini modelin normal ileri geçişine ekler; bu, eğitim sırasında veya ağırlıkları boşaltılmış modellerle çalışırken kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | N/A |
| `clip` | LoRA'nın uygulanacağı CLIP modeli. | CLIP | Evet | N/A |
| `lora_name` | Uygulanacak LoRA dosyasının adı. Seçenekler `loras` klasöründen yüklenir. | COMBO | Evet | Mevcut LoRA dosyalarının listesi |
| `strength_model` | Difüzyon modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ile 100.0 |
| `strength_clip` | CLIP modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ile 100.0 |

**Not:** Hem `strength_model` hem de `strength_clip` 0 olarak ayarlanırsa, düğüm işlem yapmadan orijinal, değiştirilmemiş `model` ve `clip` girdilerini döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | LoRA bypass modunda uygulanmış difüzyon modeli. | MODEL |
| `CLIP` | LoRA bypass modunda uygulanmış CLIP modeli. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/tr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`

# LoRA Yükle (Bypass) (Hata Ayıklama İçin)

LoraLoaderBypass düğümü, bir LoRA (Düşük Dereceli Uyarlama) öğesini özel bir "bypass" modunda bir difüzyon modeline ve bir CLIP modeline uygular. Standart bir LoRA yükleyicisinden farklı olarak bu yöntem, temel modelin ağırlıklarını kalıcı olarak değiştirmez. Bunun yerine, LoRA'nın etkisini modelin normal ileri geçişine ekleyerek çıktıyı hesaplar; bu, eğitim sırasında veya ağırlıkları boşaltılmış modellerle çalışırken kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `clip` | LoRA'nın uygulanacağı CLIP modeli. | CLIP | Evet | - |
| `lora_name` | LoRA'nın adı. Mevcut LoRA dosyaları `loras` klasöründen yüklenir. | COMBO | Evet | Mevcut LoRA dosyalarının listesi |
| `strength_model` | Difüzyon modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ile 100.0 (adım: 0.01) |
| `strength_clip` | CLIP modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 ile 100.0 (adım: 0.01) |

**Not:** Hem `strength_model` hem de `strength_clip` 0 olarak ayarlanırsa, düğüm orijinal, değiştirilmemiş `model` ve `clip` girdilerini işleme yapmadan döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Değiştirilmiş difüzyon modeli. | MODEL |
| `CLIP` | Değiştirilmiş CLIP modeli. | CLIP |

**Not:** Bu düğüm deneysel olarak işaretlenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/tr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`

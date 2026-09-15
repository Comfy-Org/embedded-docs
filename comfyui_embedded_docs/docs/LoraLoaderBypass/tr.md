# LoRA Yükle (Bypass) (Hata Ayıklama İçin)

LoraLoaderBypass düğümü, bir difüzyon modeline ve bir CLIP modeline özel bir “bypass” modunda LoRA (Düşük Dereceli Uyarlama) uygular. Standart bir LoRA yükleyiciden farklı olarak bu yöntem, temel modelin ağırlıklarını kalıcı olarak değiştirmez. Bunun yerine, LoRA'nın katkısını modelin normal ileri geçişine ekleyerek sonucu hesaplar; bu, eğitim için veya ağırlıkları dışarıya aktarılmış modellerle çalışırken kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'nın uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `clip` | LoRA'nın uygulanacağı CLIP modeli. | CLIP | Evet | - |
| `lora_name` | LoRA'nın adı. Kullanılabilir LoRA dosyaları `loras` klasöründen yüklenir. | COMBO | Evet | Kullanılabilir LoRA dosyalarının listesi |
| `strength_model` | Difüzyon modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 - 100.0 (adım: 0.01) |
| `strength_clip` | CLIP modelinin ne kadar güçlü değiştirileceği. Bu değer negatif olabilir (varsayılan: 1.0). | FLOAT | Evet | -100.0 - 100.0 (adım: 0.01) |

**Not:** Hem `strength_model` hem de `strength_clip` 0 olarak ayarlanırsa, düğüm işlem yapmadan orijinal, değiştirilmemiş `model` ve `clip` girdilerini döndürür.

**Not:** Seçilen LoRA dosyası ilk yüklendikten sonra önbelleğe alınır. Yalnızca farklı bir `lora_name` seçildiğinde diskten yeniden okunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Değiştirilmiş difüzyon modeli. | MODEL |
| `CLIP` | Değiştirilmiş CLIP modeli. | CLIP |

**Not:** Bu düğüm deneysel olarak işaretlenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/tr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`

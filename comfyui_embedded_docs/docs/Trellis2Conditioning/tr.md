# Trellis2Conditioning

Trellis2Conditioning, bir girdi görüntüsünü TRELLIS.2 modeli için koşullandırma verisine dönüştürür. Görüntüyü iki özellik kümesine (512 ve 1024 ölçeklerinde) kodlamak için bir CLIP görüş modeli kullanır ve bunları bir pozitif koşullandırma çifti olarak paketlerken, boş bir referans görevi gören eşleşen sıfır doldurulmuş bir negatif koşullandırma çifti de oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | Görüntüyü koşullandırma özelliklerine kodlamak için kullanılan CLIP görüş modeli. | CLIP_VISION | Evet | Kullanılabilir herhangi bir CLIP görüş modeli |
| `image` | ImageCropToMask'ten ön işlenmiş görüntü (TRELLIS.2 için pad_factor=1.0). | IMAGE | Evet | Herhangi bir görüntü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | TRELLIS.2 modeli için pozitif koşullandırma olarak kullanılan, 512 ve 1024 ölçeklerinde kodlanmış görüntü özelliklerini içeren koşullandırma. | CONDITIONING |
| `negative` | Pozitif koşullandırmayla aynı şekle sahip, boş bir negatif referans olarak kullanılan sıfır doldurulmuş koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`

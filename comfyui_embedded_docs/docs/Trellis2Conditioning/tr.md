# Trellis2Conditioning

Trellis2Conditioning, bir girdi görüntüsünü TRELLIS.2 modeli için koşullama verilerine dönüştürür. Görüntüyü iki özellik kümesine (512 ve 1024 ölçeklerinde) kodlamak için bir CLIP görü modeli kullanır ve bunları olumlu (positive) koşullama çifti olarak paketler; ayrıca boş bir referans görevi gören, sıfırlarla doldurulmuş eşleşen bir olumsuz (negative) koşullama çifti oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | Görüntüyü koşullama özelliklerine kodlamak için kullanılan CLIP görü modeli. | CLIP_VISION | Evet | Kullanılabilir herhangi bir CLIP görü modeli |
| `görüntü` | ImageCropToMask'ten önceden işlenmiş görüntü (TRELLIS.2 için pad_factor=1.0). | IMAGE | Evet | Herhangi bir görüntü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | 512 ve 1024 ölçeklerinde kodlanmış görüntü özelliklerini içeren ve TRELLIS.2 modeli için olumlu koşullama olarak kullanılan koşullama. | CONDITIONING |
| `negatif` | Olumlu koşullamayla aynı şekle sahip, sıfırlarla doldurulmuş ve boş bir olumsuz referans olarak kullanılan koşullama. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`

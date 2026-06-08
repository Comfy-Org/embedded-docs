SDPoseFaceBBoxes düğümü, insan yüzlerinin etrafında sınırlayıcı kutular tespit etmek ve oluşturmak için poz anahtar noktası verilerini işler. Bir karedeki her kişi için 2B yüz anahtar noktalarını analiz eder, bu noktalara dayalı bir sınırlayıcı kutu hesaplar ve kutunun boyutunu ve şeklini ayarlayabilir. Ortaya çıkan sınırlayıcı kutular, SDPoseKeypointExtractor gibi SDPose iş akışındaki diğer düğümlerle uyumlu olacak şekilde biçimlendirilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar_noktalar` | Kare başına tespit edilen kişiler ve bunların vücut/yüz işaret noktaları hakkında bilgi içeren poz anahtar noktası verileri. | POSE_KEYPOINT | Evet | - |
| `ölçek` | Tespit edilen her yüzün etrafındaki sınırlayıcı kutu alanı için çarpan. Daha büyük bir değer daha büyük bir kutu oluşturur. (varsayılan: 1.5) | FLOAT | Hayır | 1.0 - 10.0 |
| `kare_zorla` | Kırpma bölgesinin her zaman kare olması için daha kısa bbox eksenini genişletir. (varsayılan: True) | BOOLEAN | Hayır | - |

**Not:** `keypoints` girişi, SDPoseKeypointExtractor gibi düğümler tarafından üretilen, her kişi için `canvas_height`, `canvas_width` ve `face_keypoints_2d` içeren `people` verilerini içeren belirli formatta olmalıdır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bboxes` | Her kare için bir yüz sınırlayıcı kutu listesi. Her sınırlayıcı kutu, sol üst koordinatları (`x`, `y`), `width` ve `height` ile tanımlanır. Bu çıkış, SDPoseKeypointExtractor düğümünün `bboxes` girişiyle uyumludur. | BOUNDINGBOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`

# SAM3D Body Tahminini Çalıştır

SAM3D Vücut Tahmini, girdi görüntülerinde 3D vücut ve el duruşu tahmini çalıştırır; kare başına bir veya daha fazla kişiyi algılar. Algılamayı iyileştirmek için izleme verileri veya sınırlayıcı kutular sağlanabilir; ikisi de sağlanmadığında düğüm, tam kare tek kişilik algılamaya geri döner.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | Tahmin için kullanılacak SAM3D vücut modeli. | SAM3D_BODY_MODEL | Evet | — |
| `image` | Vücut tahmininin çalıştırılacağı görüntü veya görüntü topluluğu. | IMAGE | Evet | — |
| `track_data` | Çok kişili algılama için gerekli olan SAM3 Video Track izleme verileri. | SAM3_TRACK_DATA | Hayır | — |
| `bboxes` | Daha iyi algılama için kullanılan kare başına sınırlayıcı kutular. İzleme verilerine alternatif olarak kullanılabilir. | BBOX | Hayır | — |
| `run_hand_refinement` | El duruşunu iyileştirir; ek çıkarım süresi ve bellek kullanımı pahasına. Varsayılan: true. | BOOLEAN | Hayır | true<br>false |
| `fov` | Derece cinsinden dikey FoV. Tahmin edilen derinliği ve mutlak ölçeği etkiler. 0 = ~53° (16:9) değerine geri döner. Varsayılan: 0.0. | FLOAT | Hayır | 0.0 veya daha büyük |
| `batch_size` | Toplu iş olarak işlenecek maksimum kişi kırpma sayısı. Daha büyük değerler daha hızlı çıkarım için daha fazla VRAM kullanır. Varsayılan: 64. | INT | Hayır | 1 ile 512 arası |

Not: `track_data` sağlandığında, `bboxes` üzerinde önceliğe sahiptir. Ne `track_data` ne de `bboxes` sağlanmazsa, düğüm tek kişilik tam kare algılamaya geri döner. Sınırlayıcı kutular tek bir kare için (her kareye uygulanır) veya kare başına sağlanabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mhr_pose_data` | Kare başına duruş algılama sonuçlarını, yüz geometrisini, girdi görüntüsü boyutunu, kanonik köşe renklerini ve bir el köşe maskesini içeren vücut duruşu veri paketi. | MHR_POSE_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/tr.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`

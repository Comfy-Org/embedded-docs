> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/tr.md)

SaveGLB düğümü, 3B ağ verilerini veya 3B dosyaları çıktı dizinine kaydeder. Ağ verilerini veya çeşitli 3B dosya biçimlerini (GLB, GLTF, OBJ, FBX, STL, USDZ) kabul eder ve belirtilen bir dosya adı ön ekiyle dışa aktarır. Ağ verileri kaydedilirken birden çok ağı işleyebilir ve meta veriler etkinleştirildiğinde dosyalara otomatik olarak iş akışı meta verileri ekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|----------|
| `mesh` | MESH veya FILE3D | Evet | - | Kaydedilecek ağ veya 3B dosya. Ağ verilerini veya GLB, GLTF, OBJ, FBX, STL ve USDZ dahil 3B dosya biçimlerini kabul eder |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "3d/ComfyUI") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ui` | UI | Kaydedilen 3B dosyaları, dosya adı, alt klasör ve tür bilgileriyle birlikte kullanıcı arayüzünde görüntüler |

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`

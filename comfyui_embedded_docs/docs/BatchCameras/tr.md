# Batch Cameras

Kameraları ve kamera yörüngelerini giriş sırasına göre tek bir kamera listesinde birleştirir. Render Mesh ve Render Splat, listedeki her kamera için bir görüntü oluşturur; çok görünümlü bir işleme bu şekilde oluşturulur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `cameras` | Genişletilebilir kamera yuvası; Create Camera Info, Create Camera Orbit veya bir görüntüleyiciden gelir. Bir kamera listesi, içindeki her kamera olarak sayılır. | AUTOGROW | Evet | 1 ile 50 kamera arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `camera_info` | Giriş sırasına göre tüm giriş kameralarını içeren tek bir kamera listesi. | LOAD3D_CAMERA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/tr.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`

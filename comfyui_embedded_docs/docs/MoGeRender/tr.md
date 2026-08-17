# MoGe Render

## Genel Bakış

Bu düğüm, bir MOGE_GEOMETRY paketini (bir MoGe derinlik/normal tahmin düğümü tarafından üretilir) alır ve bunu standart bir görüntü formatında işler. Çıktı olarak bir derinlik haritası, renkli bir derinlik haritası, bir normal haritası veya bir maske seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Bir MoGe tahmin düğümünden gelen geometri veri paketi. | MOGE_GEOMETRY | Evet | N/A |
| `output` | Geometri verisinden işlenecek görüntü türü. DirectX ve OpenGL, normal haritasının yeşil kanal kuralını kontrol eder. DirectX: yeşil = -Y aşağı (Unreal). OpenGL: yeşil = +Y yukarı (Blender, Substance, Unity, glTF). (varsayılan: "depth") | COMBO | Evet | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Not:** Seçilen `output` modu, `moge_geometry` içinde hangi verilerin bulunması gerektiğini belirler:
- `depth` ve `depth_colored`, derinlik verisi gerektirir. Derinlik, 0.1/99.9 yüzdelik dilim kırpma kullanılarak normalleştirilmiş bir disparity (1/derinlik) haritasına dönüştürülür.
- `normal_opengl` ve `normal_directx`, normal verisi veya normallerin türetilebileceği nokta verisi gerektirir. Hiçbiri mevcut değilse düğüm bir hata verir.
- `mask`, maske verisi gerektirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | RGB tensörlerinden oluşan bir grup olarak işlenmiş görüntü. İçerik, `output` moduna bağlıdır: gri tonlamalı bir derinlik haritası, renkli bir derinlik haritası, bir normal haritası veya bir maske. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/tr.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`

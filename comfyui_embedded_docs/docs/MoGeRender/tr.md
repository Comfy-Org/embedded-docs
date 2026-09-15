# MoGe Render

Bu düğüm, bir MoGe derinlik/normal tahmin düğümü tarafından üretilen bir MOGE_GEOMETRY paketini alır ve onu standart bir görüntü formatına dönüştürür. Çıktı olarak bir derinlik haritası, renkli bir derinlik haritası, bir normal haritası veya bir maske seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Bir MoGe tahmin düğümünden gelen geometri veri paketi. | MOGE_GEOMETRY | Evet | N/A |
| `output` | Geometri verilerinden işlenecek görüntü türü. `depth` gri tonlamalı bir derinlik haritası verir, `depth_colored` renkli bir derinlik haritası verir, `normal_opengl` ve `normal_directx` normal haritaları verir ve `mask` bir maske verir. DirectX ve OpenGL, normal haritası yeşil kanal kuralını kontrol eder. DirectX: yeşil = -Y aşağı (Unreal). OpenGL: yeşil = +Y yukarı (Blender, Substance, Unity, glTF). (varsayılan: "depth") | COMBO | Evet | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Not:** Geometri paketi, seçilen `output` moduyla eşleşen verileri içermelidir. `depth` ve `depth_colored` modları pakette derinlik verisi gerektirir. `normal_opengl` ve `normal_directx` modları normal verisi veya normal verilerinin türetildiği nokta verileri gerektirir. `mask` modu maske verisi gerektirir. Gerekli veri eksikse düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | RGB tensörlerinden oluşan bir grup olarak işlenmiş görüntü. İçerik `output` moduna bağlıdır: gri tonlamalı bir derinlik haritası, renkli bir derinlik haritası, bir normal haritası veya RGB'ye dönüştürülmüş bir maske. Çıktı grubu boyutu, girdi geometrisi grup boyutuyla eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/tr.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`

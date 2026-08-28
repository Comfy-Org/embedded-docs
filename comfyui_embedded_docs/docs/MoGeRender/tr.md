# MoGe Render

## Genel Bakış

Bu düğüm, bir MOGE_GEOMETRY paketini (bir MoGe derinlik/normal tahmin düğümü tarafından üretilir) alır ve bunu standart bir görüntü formatına dönüştürür. Derinlik haritası, renkli derinlik haritası, normal haritası veya maske çıktısı vermeyi seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Bir MoGe tahmin düğümünden gelen geometri veri paketi. | MOGE_GEOMETRY | Evet | N/A |
| `output` | Geometri verilerinden oluşturulacak görüntü türü. `depth` gri tonlamalı bir derinlik haritası çıktısı verir, `depth_colored` renkli bir derinlik haritası çıktısı verir, `normal_opengl` ve `normal_directx` normal haritaları çıktısı verir ve `mask` bir maske çıktısı verir. DirectX ile OpenGL, normal haritasının yeşil kanal kuralını belirler. DirectX: yeşil = -Y aşağı (Unreal). OpenGL: yeşil = +Y yukarı (Blender, Substance, Unity, glTF). (varsayılan: "depth") | COMBO | Evet | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Not:** Geometri paketi, seçilen `output` moduyla eşleşen verileri içermelidir. `depth` ve `depth_colored` modları, pakette derinlik verisi gerektirir. `normal_opengl` ve `normal_directx` modları, normal verisi veya normallerin türetildiği nokta verisi gerektirir. `mask` modu, maske verisi gerektirir. Gerekli veri eksikse düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | RGB tensörlerinden oluşan bir parti olarak işlenmiş görüntü. İçerik, `output` moduna bağlıdır: gri tonlamalı derinlik haritası, renkli derinlik haritası, normal haritası veya RGB'ye dönüştürülmüş maske. Çıktı parti boyutu, girdi geometri parti boyutuyla eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/tr.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`

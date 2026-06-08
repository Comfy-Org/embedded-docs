## Genel Bakış

Bu düğüm, bir MOGE_GEOMETRY paketini (MoGe derinlik/normal tahmin düğümü tarafından üretilir) alır ve standart bir görüntü formatına dönüştürür. Derinlik haritası, renklendirilmiş derinlik haritası, normal haritası veya maske çıktısı almayı seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_geometry` | MoGe tahmin düğümünden gelen geometri veri paketi. | MOGE_GEOMETRY | Evet | Yok |
| `output` | Geometri verilerinden oluşturulacak görüntü türü. DirectX ve OpenGL, normal haritası yeşil kanal kuralını belirler. DirectX: yeşil = -Y aşağı (Unreal). OpenGL: yeşil = +Y yukarı (Blender, Substance, Unity, glTF). (varsayılan: "depth") | COMBO | Evet | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | RGB tensörleri yığını olarak oluşturulmuş görüntü. İçerik, `output` moduna bağlıdır: gri tonlamalı derinlik haritası, renklendirilmiş derinlik haritası, normal haritası veya maske. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/tr.md)

---
**Source fingerprint (SHA-256):** `45ba499e746ce46f9b6f7773e3218bcf80ad2e8d65940b38e248cc2f20c8b2fe`

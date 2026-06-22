# Webcam Yakalama

WebcamCapture düğümü, bir web kamerası cihazından görüntüler yakalar ve bunları ComfyUI iş akışlarında kullanılabilecek bir formata dönüştürür. LoadImage düğümünden türetilmiştir ve yakalama boyutlarını ve zamanlamasını kontrol etmek için seçenekler sunar. Etkinleştirildiğinde, düğüm iş akışı kuyruğu her işlendiğinde yeni görüntüler yakalayabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Görüntülerin yakalanacağı web kamerası giriş kaynağı | WEBCAM | Evet | - |
| `genişlik` | Yakalanan görüntü için istenen genişlik (varsayılan: 0, web kamerasının yerel çözünürlüğünü kullanır) | INT | Evet | 0 ile MAX_RESOLUTION |
| `yükseklik` | Yakalanan görüntü için istenen yükseklik (varsayılan: 0, web kamerasının yerel çözünürlüğünü kullanır) | INT | Evet | 0 ile MAX_RESOLUTION |
| `kuyrukta_yakala` | Etkinleştirildiğinde, iş akışı kuyruğu her işlendiğinde yeni bir görüntü yakalar (varsayılan: True) | BOOLEAN | Evet | - |

**Not:** Hem `width` hem de `height` 0 olarak ayarlandığında, düğüm web kamerasının yerel çözünürlüğünü kullanır. Herhangi bir boyutu sıfır olmayan bir değere ayarlamak, yakalanan görüntüyü buna göre yeniden boyutlandıracaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | ComfyUI'nin görüntü formatına dönüştürülmüş yakalanan web kamerası görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/tr.md)

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`

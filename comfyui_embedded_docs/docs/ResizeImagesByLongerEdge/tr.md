# Görüntüleri Uzun Kenara Göre Yeniden Boyutlandır

Uzun Kenara Göre Görselleri Yeniden Boyutlandır düğümü, bir veya daha fazla görseli, en uzun kenarları belirtilen hedef uzunluğa denk gelecek şekilde yeniden boyutlandırır. Genişlik veya yükseklikten hangisinin daha uzun olduğunu otomatik olarak belirler ve orijinal en-boy oranını korumak için diğer boyutu orantılı olarak ölçeklendirir. Bu özellik, görselleri en büyük boyutlarına göre standartlaştırmak için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Yeniden boyutlandırılacak giriş görseli veya görsel grubu. | IMAGE | Evet | - |
| `uzun_kenar` | Uzun kenar için hedef uzunluk. Kısa kenar orantılı olarak ölçeklendirilecektir. (varsayılan: 1024) | INT | Evet | 1 - 8192 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Yeniden boyutlandırılmış görsel veya görsel grubu. Çıkış, girişle aynı sayıda görsel içerir ve her birinin uzun kenarı belirtilen `uzun_kenar` uzunluğuna denk gelir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/tr.md)

---
**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`

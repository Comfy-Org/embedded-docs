Bir başlangıç ve bitiş noktası arasında enterpolasyonlu güç değerlerine sahip bir dizi kanca anahtar karesi oluşturur. Bu düğüm, üretim sürecinin belirtilen bir yüzde aralığı boyunca güç parametresini düzgün bir şekilde geçiş yapan birden çok anahtar kare üretir ve geçiş eğrisini kontrol etmek için çeşitli enterpolasyon yöntemleri kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `başlangıç_gücü` | Enterpolasyon dizisi için başlangıç güç değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `bitiş_gücü` | Enterpolasyon dizisi için bitiş güç değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `enterpolasyon` | Güç değerleri arasında geçiş yapmak için kullanılan enterpolasyon yöntemi (varsayılan: LINEAR) | COMBO | Evet | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `başlangıç_yüzdesi` | Üretim sürecindeki başlangıç yüzde konumu (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | Üretim sürecindeki bitiş yüzde konumu (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `anahtar_kare_sayısı` | Enterpolasyon dizisinde oluşturulacak anahtar kare sayısı (varsayılan: 5) | INT | Evet | 2 - 100 |
| `anahtar_kareleri_yazdır` | Oluşturulan anahtar kare bilgilerinin günlüğe yazdırılıp yazdırılmayacağı (varsayılan: False) | BOOLEAN | Evet | True/False |
| `önceki_kanca_kf` | Eklenecek isteğe bağlı önceki kanca anahtar kareleri grubu | HOOK_KEYFRAMES | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Kanca_KF` | Enterpolasyonlu diziyi içeren oluşturulan kanca anahtar kareleri grubu | HOOK_KEYFRAMES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/tr.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`

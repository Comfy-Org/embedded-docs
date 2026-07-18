Bu düğüm, belirtilen başlangıç ve bitiş yüzdeleri arasında eşit olarak dağıtarak, kayan noktalı güç değerlerinin bir listesinden kanca anahtar kareleri oluşturur. Her güç değerinin animasyon zaman çizelgesinde belirli bir yüzde konumuna atandığı bir dizi anahtar kare üretir. Düğüm, yeni bir anahtar kare grubu oluşturabilir veya mevcut bir gruba ekleyebilir; ayrıca hata ayıklama amacıyla oluşturulan anahtar kareleri yazdırma seçeneğine sahiptir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ondalık_güç` | Anahtar kareler için güç değerlerini temsil eden tek bir kayan nokta değeri veya kayan nokta değerleri listesi (varsayılan: -1) | FLOATS | Evet | -1 ila ∞ |
| `başlangıç_yüzdesi` | Zaman çizelgesindeki ilk anahtar kare için başlangıç yüzde konumu (varsayılan: 0,0) | FLOAT | Evet | 0,0 ila 1,0 |
| `bitiş_yüzdesi` | Zaman çizelgesindeki son anahtar kare için bitiş yüzde konumu (varsayılan: 1,0) | FLOAT | Evet | 0,0 ila 1,0 |
| `anahtar_kareleri_yazdır` | Etkinleştirildiğinde, oluşturulan anahtar kare bilgilerini konsola yazdırır (varsayılan: Yanlış) | BOOLEAN | Evet | Doğru/Yanlış |
| `önceki_kanca_kf` | Yeni anahtar karelerin ekleneceği mevcut bir kanca anahtar kare grubu; sağlanmazsa yeni bir grup oluşturur | HOOK_KEYFRAMES | Hayır | - |

**Not:** `floats_strength` parametresi tek bir kayan nokta değerini veya yinelenebilir bir kayan nokta listesini kabul eder. Anahtar kareler, sağlanan güç değerlerinin sayısına bağlı olarak `start_percent` ve `end_percent` arasında doğrusal olarak dağıtılır. İlk anahtar karenin uygulanmasını sağlamak için en az bir adıma sahip olması garanti edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Kanca_KF` | Yeni oluşturulan anahtar kareleri içeren bir kanca anahtar kare grubu; yeni bir grup olarak veya giriş anahtar kare grubuna eklenmiş olarak | HOOK_KEYFRAMES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/tr.md)

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/tr.md)

Bu düğüm, belirtilen başlangıç ve bitiş yüzdeleri arasında eşit olarak dağıtarak, kayan noktalı güç değerlerinin bir listesinden kanca anahtar kareleri oluşturur. Her güç değerinin animasyon zaman çizelgesinde belirli bir yüzde konumuna atandığı bir dizi anahtar kare üretir. Düğüm, yeni bir anahtar kare grubu oluşturabilir veya mevcut bir gruba ekleyebilir; ayrıca hata ayıklama amacıyla oluşturulan anahtar kareleri yazdırma seçeneğine sahiptir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `floats_strength` | FLOATS | Evet | -1 ila ∞ | Anahtar kareler için güç değerlerini temsil eden tek bir kayan nokta değeri veya kayan nokta değerleri listesi (varsayılan: -1) |
| `start_percent` | FLOAT | Evet | 0,0 ila 1,0 | Zaman çizelgesindeki ilk anahtar kare için başlangıç yüzde konumu (varsayılan: 0,0) |
| `end_percent` | FLOAT | Evet | 0,0 ila 1,0 | Zaman çizelgesindeki son anahtar kare için bitiş yüzde konumu (varsayılan: 1,0) |
| `print_keyframes` | BOOLEAN | Evet | Doğru/Yanlış | Etkinleştirildiğinde, oluşturulan anahtar kare bilgilerini konsola yazdırır (varsayılan: Yanlış) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Hayır | - | Yeni anahtar karelerin ekleneceği mevcut bir kanca anahtar kare grubu; sağlanmazsa yeni bir grup oluşturur |

**Not:** `floats_strength` parametresi tek bir kayan nokta değerini veya yinelenebilir bir kayan nokta listesini kabul eder. Anahtar kareler, sağlanan güç değerlerinin sayısına bağlı olarak `start_percent` ve `end_percent` arasında doğrusal olarak dağıtılır. İlk anahtar karenin uygulanmasını sağlamak için en az bir adıma sahip olması garanti edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Yeni oluşturulan anahtar kareleri içeren bir kanca anahtar kare grubu; yeni bir grup olarak veya giriş anahtar kare grubuna eklenmiş olarak |

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`

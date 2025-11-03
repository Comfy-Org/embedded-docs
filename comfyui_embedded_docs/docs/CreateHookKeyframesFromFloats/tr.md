> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/tr.md)

Bu düğüm, belirtilen başlangıç ve bitiş yüzdeleri arasında eşit şekilde dağıtılmış bir kayan nokta kuvvet değerleri listesinden kanca kareleri oluşturur. Animasyon zaman çizelgesinde her kuvvet değerinin belirli bir yüzdelik konuma atandığı bir kare dizisi üretir. Düğüm, yeni bir kare grubu oluşturabilir veya mevcut bir gruba ekleyebilir ve hata ayıklama amacıyla oluşturulan kareleri yazdırma seçeneği sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ondalık_güç` | FLOATS | Evet | -1 ile ∞ | Kareler için kuvvet değerlerini temsil eden tek bir kayan nokta değeri veya kayan nokta değerleri listesi (varsayılan: -1) |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 ile 1.0 | Zaman çizelgesindeki ilk karenin başlangıç yüzdelik konumu (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 ile 1.0 | Zaman çizelgesindeki son karenin bitiş yüzdelik konumu (varsayılan: 1.0) |
| `anahtar_kareleri_yazdır` | BOOLEAN | Evet | Doğru/Yanlış | Etkinleştirildiğinde, oluşturulan kare bilgilerini konsola yazdırır (varsayılan: Yanlış) |
| `önceki_kanca_kf` | HOOK_KEYFRAMES | Hayır | - | Yeni karelerin ekleneceği mevcut bir kanca kare grubu veya sağlanmazsa yeni bir grup oluşturur |

**Not:** `floats_strength` parametresi, tek bir kayan nokta değeri veya yinelenebilir bir kayan nokta listesi kabul eder. Kareler, sağlanan kuvvet değerlerinin sayısına bağlı olarak `start_percent` ve `end_percent` arasında doğrusal olarak dağıtılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Yeni oluşturulan kareleri içeren bir kanca kare grubu; yeni bir grup olarak veya girdi kare grubuna eklenmiş şekilde |
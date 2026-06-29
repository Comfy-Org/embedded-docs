# Tohum

Seed düğümü, sabit veya rastgele bir tam sayı değeri üretir. Diğer düğümlerdeki rastgele işlemlerin tekrarlanabilirliğini kontrol etmek için, rastgele sayı üretimlerine tutarlı bir başlangıç noktası sağlayarak yaygın olarak kullanılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `tohum` | Kullanılacak tohum değeri. Üretim sonrası kontrol seçeneği, değerin sabit kalıp kalmayacağını veya her üretimden sonra değişip değişmeyeceğini belirler. | INT | Evet | 0 ile 9223372036854775807 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `tohum` | Üretilen tohum değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

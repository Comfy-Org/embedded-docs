# Float

PrimitiveFloat düğümü, iş akışınızda kullanılabilen bir ondalık sayı değeri oluşturur. Tek bir sayısal girdi alır ve aynı değeri çıktı olarak verir; böylece ComfyUI hattınızdaki farklı düğümler arasında ondalık sayı değerleri tanımlamanıza ve iletmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `value` | Çıktı olarak verilecek ondalık sayı değeri (varsayılan: 0.0) | FLOAT | Yes | -sys.maxsize to sys.maxsize (step: 0.1) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Girdi olarak verilen ondalık sayı değeri | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/tr.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`

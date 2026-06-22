# Zaman Adımları Aralığı

ConditioningTimestepsRange düğümü, üretim sürecinde koşullandırma efektlerinin ne zaman uygulanacağını kontrol etmek için üç ayrı zaman adımı aralığı oluşturur. Başlangıç ve bitiş yüzde değerlerini alır ve tüm zaman adımı aralığını (0.0 ile 1.0 arası) üç bölüme ayırır: belirtilen yüzdeler arasındaki ana aralık, başlangıç yüzdesinden önceki aralık ve bitiş yüzdesinden sonraki aralık.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `başlangıç_yüzdesi` | Zaman adımı aralığının başlangıç yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | Zaman adımı aralığının bitiş yüzdesi (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `TIMESTEPS_RANGE` | start_percent ve end_percent tarafından tanımlanan ana zaman adımı aralığı | TIMESTEPS_RANGE |
| `BEFORE_RANGE` | 0.0 ile start_percent arasındaki zaman adımı aralığı | TIMESTEPS_RANGE |
| `AFTER_RANGE` | end_percent ile 1.0 arasındaki zaman adımı aralığı | TIMESTEPS_RANGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/tr.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`

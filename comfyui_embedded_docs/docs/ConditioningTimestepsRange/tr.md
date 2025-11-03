> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/tr.md)

ConditioningTimestepsRange düğümü, üretim süreci boyunca koşullandırma etkilerinin ne zaman uygulanacağını kontrol etmek için üç farklı zaman adımı aralığı oluşturur. Başlangıç ve bitiş yüzde değerlerini alır ve tüm zaman adımı aralığını (0.0 ile 1.0 arası) üç bölüme ayırır: belirtilen yüzdeler arasındaki ana aralık, başlangıç yüzdesinden önceki aralık ve bitiş yüzdesinden sonraki aralık.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | Zaman adımı aralığının başlangıç yüzdesi (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | Zaman adımı aralığının bitiş yüzdesi (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `TIMESTEPS_RANGE` | TIMESTEPS_RANGE | start_percent ve end_percent tarafından tanımlanan ana zaman adımı aralığı |
| `BEFORE_RANGE` | TIMESTEPS_RANGE | 0.0'dan start_percent'e kadar olan zaman adımı aralığı |
| `AFTER_RANGE` | TIMESTEPS_RANGE | end_percent'ten 1.0'a kadar olan zaman adımı aralığı |
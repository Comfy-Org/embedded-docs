> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/tr.md)

UNetCrossAttentionMultiply düğümü, bir UNet modelindeki çapraz dikkat mekanizmasına çarpım faktörleri uygular. Çapraz dikkat katmanlarının sorgu, anahtar, değer ve çıktı bileşenlerini ölçeklendirerek farklı dikkat davranışları ve etkileri denemenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dikkat ölçeklendirme faktörleriyle değiştirilecek UNet modeli |
| `q` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatteki sorgu bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `k` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatteki anahtar bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `v` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatteki değer bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `out` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatteki çıktı bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Ölçeklendirilmiş çapraz dikkat bileşenlerine sahip değiştirilmiş UNet modeli |
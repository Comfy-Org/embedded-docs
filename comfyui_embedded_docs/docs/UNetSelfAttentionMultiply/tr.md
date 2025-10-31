> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/tr.md)

UNetSelfAttentionMultiply düğümü, bir UNet modelindeki öz-dikkat mekanizmasının sorgu, anahtar, değer ve çıktı bileşenlerine çarpım faktörleri uygular. Dikkat ağırlıklarının modelin davranışını nasıl etkilediğini denemek için, dikkat hesaplamasının farklı bölümlerini ölçeklendirmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dikkat ölçeklendirme faktörleri ile değiştirilecek UNet modeli |
| `q` | FLOAT | Hayır | 0.0 - 10.0 | Sorgu bileşeni için çarpım faktörü (varsayılan: 1.0) |
| `k` | FLOAT | Hayır | 0.0 - 10.0 | Anahtar bileşeni için çarpım faktörü (varsayılan: 1.0) |
| `v` | FLOAT | Hayır | 0.0 - 10.0 | Değer bileşeni için çarpım faktörü (varsayılan: 1.0) |
| `out` | FLOAT | Hayır | 0.0 - 10.0 | Çıktı bileşeni için çarpım faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Ölçeklendirilmiş dikkat bileşenlerine sahip değiştirilmiş UNet modeli |
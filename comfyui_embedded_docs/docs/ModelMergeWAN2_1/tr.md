> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/tr.md)

ModelMergeWAN2_1 düğümü, iki modelin bileşenlerini ağırlıklı ortalamalar kullanarak birleştirir. 30 blok içeren 1.3B modelleri ve 40 blok içeren 14B modelleri dahil olmak üzere farklı model boyutlarını destekler; ek bir görüntü gömme bileşeni içeren görüntüden videoya modeller için özel bir işleme sahiptir. Modellerin her bir bileşeni, iki giriş modeli arasındaki karıştırma oranını kontrol etmek için bağımsız olarak ağırlıklandırılabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `patch_embedding.` | FLOAT | Evet | 0.0 - 1.0 | Yama gömme bileşeni için ağırlık (varsayılan: 1.0) |
| `time_embedding.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme bileşeni için ağırlık (varsayılan: 1.0) |
| `time_projection.` | FLOAT | Evet | 0.0 - 1.0 | Zaman projeksiyonu bileşeni için ağırlık (varsayılan: 1.0) |
| `text_embedding.` | FLOAT | Evet | 0.0 - 1.0 | Metin gömme bileşeni için ağırlık (varsayılan: 1.0) |
| `img_emb.` | FLOAT | Evet | 0.0 - 1.0 | Görüntüden videoya modellerde kullanılan görüntü gömme bileşeni için ağırlık (varsayılan: 1.0) |
| `blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Blok 0 için ağırlık (varsayılan: 1.0) |
| `blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Blok 1 için ağırlık (varsayılan: 1.0) |
| `blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Blok 2 için ağırlık (varsayılan: 1.0) |
| `blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Blok 3 için ağırlık (varsayılan: 1.0) |
| `blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Blok 4 için ağırlık (varsayılan: 1.0) |
| `blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Blok 5 için ağırlık (varsayılan: 1.0) |
| `blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Blok 6 için ağırlık (varsayılan: 1.0) |
| `blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Blok 7 için ağırlık (varsayılan: 1.0) |
| `blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Blok 8 için ağırlık (varsayılan: 1.0) |
| `blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Blok 9 için ağırlık (varsayılan: 1.0) |
| `blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Blok 10 için ağırlık (varsayılan: 1.0) |
| `blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Blok 11 için ağırlık (varsayılan: 1.0) |
| `blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Blok 12 için ağırlık (varsayılan: 1.0) |
| `blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Blok 13 için ağırlık (varsayılan: 1.0) |
| `blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Blok 14 için ağırlık (varsayılan: 1.0) |
| `blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Blok 15 için ağırlık (varsayılan: 1.0) |
| `blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Blok 16 için ağırlık (varsayılan: 1.0) |
| `blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Blok 17 için ağırlık (varsayılan: 1.0) |
| `blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Blok 18 için ağırlık (varsayılan: 1.0) |
| `blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Blok 19 için ağırlık (varsayılan: 1.0) |
| `blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Blok 20 için ağırlık (varsayılan: 1.0) |
| `blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Blok 21 için ağırlık (varsayılan: 1.0) |
| `blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Blok 22 için ağırlık (varsayılan: 1.0) |
| `blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Blok 23 için ağırlık (varsayılan: 1.0) |
| `blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Blok 24 için ağırlık (varsayılan: 1.0) |
| `blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Blok 25 için ağırlık (varsayılan: 1.0) |
| `blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Blok 26 için ağırlık (varsayılan: 1.0) |
| `blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Blok 27 için ağırlık (varsayılan: 1.0) |
| `blocks.28.` | FLOAT | Evet | 0.0 - 1.0 | Blok 28 için ağırlık (varsayılan: 1.0) |
| `blocks.29.` | FLOAT | Evet | 0.0 - 1.0 | Blok 29 için ağırlık (varsayılan: 1.0) |
| `blocks.30.` | FLOAT | Evet | 0.0 - 1.0 | Blok 30 için ağırlık (varsayılan: 1.0) |
| `blocks.31.` | FLOAT | Evet | 0.0 - 1.0 | Blok 31 için ağırlık (varsayılan: 1.0) |
| `blocks.32.` | FLOAT | Evet | 0.0 - 1.0 | Blok 32 için ağırlık (varsayılan: 1.0) |
| `blocks.33.` | FLOAT | Evet | 0.0 - 1.0 | Blok 33 için ağırlık (varsayılan: 1.0) |
| `blocks.34.` | FLOAT | Evet | 0.0 - 1.0 | Blok 34 için ağırlık (varsayılan: 1.0) |
| `blocks.35.` | FLOAT | Evet | 0.0 - 1.0 | Blok 35 için ağırlık (varsayılan: 1.0) |
| `blocks.36.` | FLOAT | Evet | 0.0 - 1.0 | Blok 36 için ağırlık (varsayılan: 1.0) |
| `blocks.37.` | FLOAT | Evet | 0.0 - 1.0 | Blok 37 için ağırlık (varsayılan: 1.0) |
| `blocks.38.` | FLOAT | Evet | 0.0 - 1.0 | Blok 38 için ağırlık (varsayılan: 1.0) |
| `blocks.39.` | FLOAT | Evet | 0.0 - 1.0 | Blok 39 için ağırlık (varsayılan: 1.0) |
| `head.` | FLOAT | Evet | 0.0 - 1.0 | Baş (head) bileşeni için ağırlık (varsayılan: 1.0) |

**Not:** Tüm ağırlık parametreleri, 0.01 adım artışlarıyla 0.0 ile 1.0 arasında bir aralık kullanır. Düğüm, farklı model boyutlarını barındırmak için 40 bloğa kadar destekler; 1.3B modeller 30 blok, 14B modeller ise 40 blok kullanır. `img_emb.` parametresi özellikle görüntüden videoya modeller içindir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen ağırlıklara göre her iki giriş modelinden bileşenlerin birleştirilmesiyle oluşan birleştirilmiş model |
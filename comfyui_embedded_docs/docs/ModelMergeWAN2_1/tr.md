ModelMergeWAN2_1 düğümü, iki WAN2.1 modelini bileşenlerini ağırlıklı ortalamalar kullanarak harmanlayarak birleştirir. 30 bloklu 1.3B modeller ve 40 bloklu 14B modeller dahil olmak üzere farklı model boyutlarını destekler. Ek bir görüntü gömme bileşeni içeren görüntüden videoya modeller için özel işleme sahiptir. Modellerin her bir bileşeni, iki giriş modeli arasındaki harmanlama oranını kontrol etmek için ayrı ayrı ağırlıklandırılabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `patch_embedding.` | Yama gömme bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `time_embedding.` | Zaman gömme bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `time_projection.` | Zaman izdüşümü bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `text_embedding.` | Metin gömme bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `img_emb.` | Görüntü gömme bileşeni için ağırlık, görüntüden videoya modellerde kullanılır (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.0.` | Blok 0 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.1.` | Blok 1 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.2.` | Blok 2 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.3.` | Blok 3 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.4.` | Blok 4 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.5.` | Blok 5 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.6.` | Blok 6 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.7.` | Blok 7 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.8.` | Blok 8 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.9.` | Blok 9 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.10.` | Blok 10 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.11.` | Blok 11 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.12.` | Blok 12 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.13.` | Blok 13 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.14.` | Blok 14 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.15.` | Blok 15 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.16.` | Blok 16 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.17.` | Blok 17 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.18.` | Blok 18 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.19.` | Blok 19 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.20.` | Blok 20 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.21.` | Blok 21 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.22.` | Blok 22 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.23.` | Blok 23 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.24.` | Blok 24 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.25.` | Blok 25 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.26.` | Blok 26 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.27.` | Blok 27 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.28.` | Blok 28 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.29.` | Blok 29 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.30.` | Blok 30 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.31.` | Blok 31 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.32.` | Blok 32 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.33.` | Blok 33 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.34.` | Blok 34 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.35.` | Blok 35 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.36.` | Blok 36 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.37.` | Blok 37 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.38.` | Blok 38 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.39.` | Blok 39 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `head.` | Baş bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Tüm ağırlık parametreleri 0.0 ile 1.0 arasında, 0.01 adım artışlarıyla bir aralık kullanır. Düğüm, farklı model boyutlarını desteklemek için 40 bloğa kadar destekler; 1.3B modeller 30 blok, 14B modeller ise 40 blok kullanır. `img_emb.` parametresi özellikle görüntüden videoya modeller içindir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklara göre her iki giriş modelinin bileşenlerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/tr.md)

---
**Source fingerprint (SHA-256):** `d550a2f62bbcb4b46ccdd8a04fab80e93f96ea63426d48acb3515d51175efc99`

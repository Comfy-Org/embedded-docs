> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/tr.md)

ModelMergeFlux1 düğümü, iki difüzyon modelini bileşenlerini ağırlıklı enterpolasyon kullanarak harmanlayarak birleştirir. Modellerin farklı bölümlerinin - görüntü işleme blokları, zaman gömme katmanları, rehberlik mekanizmaları, vektör girişleri, metin kodlayıcılar ve çeşitli transformatör blokları dahil - nasıl birleştirileceği üzerinde hassas kontrol sağlar. Bu, iki kaynak modelden özelleştirilmiş karakteristiklere sahip melez modeller oluşturmayı mümkün kılar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek birinci kaynak model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci kaynak model |
| `img_in.` | FLOAT | Evet | 0.0 - 1.0 | Görüntü girişi enterpolasyon ağırlığı (varsayılan: 1.0) |
| `time_in.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `rehberlik_girişi` | FLOAT | Evet | 0.0 - 1.0 | Rehberlik mekanizması enterpolasyon ağırlığı (varsayılan: 1.0) |
| `vector_in.` | FLOAT | Evet | 0.0 - 1.0 | Vektör girişi enterpolasyon ağırlığı (varsayılan: 1.0) |
| `txt_in.` | FLOAT | Evet | 0.0 - 1.0 | Metin kodlayıcı enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `double_blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Çift blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.24.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 24 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.25.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 25 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.26.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 26 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.27.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 27 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.28.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 28 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.29.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 29 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.30.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 30 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.31.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 31 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.32.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 32 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.33.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 33 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.34.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 34 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.35.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 35 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.36.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 36 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `single_blocks.37.` | FLOAT | Evet | 0.0 - 1.0 | Tek blok 37 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki giriş modelinden karakteristikleri birleştiren harmanlanmış model |
# ModelBirleştirmeFlux1

ModelMergeFlux1 düğümü, iki difüzyon modelini bileşenlerini ağırlıklı enterpolasyon kullanarak harmanlayarak birleştirir. Görüntü işleme blokları, zaman gömme katmanları, yönlendirme mekanizmaları, vektör girdileri, metin kodlayıcılar ve çeşitli dönüştürücü blokları dahil olmak üzere modellerin farklı bölümlerinin nasıl birleştirileceği üzerinde ince ayar yapma kontrolü sağlar. Bu, iki kaynak modelden özelleştirilmiş özelliklere sahip hibrit modeller oluşturmayı mümkün kılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk kaynak model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci kaynak model | MODEL | Evet | - |
| `img_in.` | Görüntü girdisi enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `time_in.` | Zaman gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `rehberlik_girişi` | Yönlendirme mekanizması enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `vector_in.` | Vektör girdisi enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `txt_in.` | Metin kodlayıcı enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.0.` | Çift blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.1.` | Çift blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.2.` | Çift blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.3.` | Çift blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.4.` | Çift blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.5.` | Çift blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.6.` | Çift blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.7.` | Çift blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.8.` | Çift blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.9.` | Çift blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.10.` | Çift blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.11.` | Çift blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.12.` | Çift blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.13.` | Çift blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.14.` | Çift blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.15.` | Çift blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.16.` | Çift blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.17.` | Çift blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `double_blocks.18.` | Çift blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.0.` | Tek blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.1.` | Tek blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.2.` | Tek blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.3.` | Tek blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.4.` | Tek blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.5.` | Tek blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.6.` | Tek blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.7.` | Tek blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.8.` | Tek blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.9.` | Tek blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.10.` | Tek blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.11.` | Tek blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.12.` | Tek blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.13.` | Tek blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.14.` | Tek blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.15.` | Tek blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.16.` | Tek blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.17.` | Tek blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.18.` | Tek blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.19.` | Tek blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.20.` | Tek blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.21.` | Tek blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.22.` | Tek blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.23.` | Tek blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.24.` | Tek blok 24 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.25.` | Tek blok 25 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.26.` | Tek blok 26 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.27.` | Tek blok 27 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.28.` | Tek blok 28 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.29.` | Tek blok 29 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.30.` | Tek blok 30 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.31.` | Tek blok 31 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.32.` | Tek blok 32 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.33.` | Tek blok 33 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.34.` | Tek blok 34 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.35.` | Tek blok 35 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.36.` | Tek blok 36 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `single_blocks.37.` | Tek blok 37 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `final_layer.` | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/tr.md)

---
**Source fingerprint (SHA-256):** `a632133b5d4bc7c5a4e1be5f6f779e424a491fffb8ef7702346adc4acf6f23bc`

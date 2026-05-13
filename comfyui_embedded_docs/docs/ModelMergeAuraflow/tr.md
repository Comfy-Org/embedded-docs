> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/tr.md)

ModelMergeAuraflow düğümü, iki farklı modeli, çeşitli model bileşenleri için belirli harmanlama ağırlıklarını ayarlayarak birleştirmenize olanak tanır. Modellerin farklı kısımlarının (ilk katmanlardan son çıktılara kadar) nasıl birleştirileceği üzerinde ince ayarlı kontrol sağlar. Bu düğüm, birleştirme süreci üzerinde hassas kontrol ile özel model kombinasyonları oluşturmak için özellikle kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `init_x_linear.` | FLOAT | Evet | 0.0 - 1.0 | İlk doğrusal dönüşüm için harmanlama ağırlığı (varsayılan: 1.0) |
| `positional_encoding` | FLOAT | Evet | 0.0 - 1.0 | Konumsal kodlama bileşenleri için harmanlama ağırlığı (varsayılan: 1.0) |
| `cond_seq_linear.` | FLOAT | Evet | 0.0 - 1.0 | Koşullu dizi doğrusal katmanları için harmanlama ağırlığı (varsayılan: 1.0) |
| `register_tokens` | FLOAT | Evet | 0.0 - 1.0 | Token kaydı bileşenleri için harmanlama ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme bileşenleri için harmanlama ağırlığı (varsayılan: 1.0) |
| `double_layers.0.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 0 için harmanlama ağırlığı (varsayılan: 1.0) |
| `double_layers.1.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 1 için harmanlama ağırlığı (varsayılan: 1.0) |
| `double_layers.2.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 2 için harmanlama ağırlığı (varsayılan: 1.0) |
| `double_layers.3.` | FLOAT | Evet | 0.0 - 1.0 | Çift katman grubu 3 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.0.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 0 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.1.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 1 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.2.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 2 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.3.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 3 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.4.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 4 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.5.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 5 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.6.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 6 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.7.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 7 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.8.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 8 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.9.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 9 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.10.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 10 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.11.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 11 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.12.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 12 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.13.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 13 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.14.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 14 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.15.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 15 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.16.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 16 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.17.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 17 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.18.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 18 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.19.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 19 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.20.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 20 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.21.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 21 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.22.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 22 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.23.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 23 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.24.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 24 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.25.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 25 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.26.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 26 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.27.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 27 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.28.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 28 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.29.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 29 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.30.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 30 için harmanlama ağırlığı (varsayılan: 1.0) |
| `single_layers.31.` | FLOAT | Evet | 0.0 - 1.0 | Tek katman 31 için harmanlama ağırlığı (varsayılan: 1.0) |
| `modF.` | FLOAT | Evet | 0.0 - 1.0 | modF bileşenleri için harmanlama ağırlığı (varsayılan: 1.0) |
| `final_linear.` | FLOAT | Evet | 0.0 - 1.0 | Son doğrusal dönüşüm için harmanlama ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen harmanlama ağırlıklarına göre her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model |

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`

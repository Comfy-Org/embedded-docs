# ModelBirleştirmeWAN2_1

ModelMergeWAN2_1 düğümü, iki WAN2.1 modelini, bileşenlerini ağırlıklı ortalamalar kullanarak harmanlayarak birleştirir. 1.3B modeller (30 blok) ve 14B modeller (40 blok) dahil olmak üzere farklı model boyutlarını destekler; ek bir görüntü yerleştirme bileşeni içeren görüntüden videoya (image-to-video) modeller için özel işleme sahiptir. Her bileşen, iki girdi modeli arasındaki harmanlama oranını kontrol etmek için ayrı ayrı ağırlıklandırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `patch_embedding.` | Patch yerleştirme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `time_embedding.` | Zaman yerleştirme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `time_projection.` | Zaman projeksiyonu bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `text_embedding.` | Metin yerleştirme bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `img_emb.` | Görüntü yerleştirme bileşeni ağırlığı; görüntüden videoya modellerde kullanılır (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.0.` | 0. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.1.` | 1. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.2.` | 2. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.3.` | 3. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.4.` | 4. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.5.` | 5. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.6.` | 6. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.7.` | 7. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.8.` | 8. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.9.` | 9. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.10.` | 10. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.11.` | 11. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.12.` | 12. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.13.` | 13. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.14.` | 14. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.15.` | 15. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.16.` | 16. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.17.` | 17. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.18.` | 18. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.19.` | 19. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.20.` | 20. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.21.` | 21. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.22.` | 22. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.23.` | 23. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.24.` | 24. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.25.` | 25. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.26.` | 26. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.27.` | 27. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.28.` | 28. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.29.` | 29. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.30.` | 30. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.31.` | 31. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.32.` | 32. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.33.` | 33. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.34.` | 34. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.35.` | 35. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.36.` | 36. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.37.` | 37. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.38.` | 38. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.39.` | 39. blok ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `baş.` | Baş (head) bileşeni ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Tüm ağırlık parametreleri 0,01 adım artışlarıyla 0,0 ile 1,0 aralığını kullanır. Düğüm, farklı model boyutlarını desteklemek için en fazla 40 blok ağırlık girdisi sağlar: 1.3B modeller 30 blok kullanır (`blocks.0.` ile `blocks.29.` arası), 14B modeller ise 40 blok kullanır (`blocks.0.` ile `blocks.39.` arası). `img_emb.` parametresi görüntüden videoya modeller tarafından kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklara göre her iki girdi modelinin bileşenlerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/tr.md)

---
**Source fingerprint (SHA-256):** `6a17defa25b1ef045b85af4a73e00d3a64c1948c0c47f355d1d488a75b09f224`

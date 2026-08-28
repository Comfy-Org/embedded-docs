# ClipMergeSimple

`CLIPMergeSimple`, belirtilen bir orana göre iki CLIP metin kodlayıcı modelini birleştiren bir model birleştirme düğümüdür. İlk CLIP modelini kopyalar ve ikinci CLIP modelinden position IDs ve logit scale bileşenlerini atlayarak ağırlıklı yamaları uygular; böylece her iki kaynağın özelliklerini harmanlayan hibrit bir model üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip1` | Birleştirilecek ilk CLIP modeli. Birleştirme sürecinde temel model olarak görev yapar. | CLIP | Evet | - |
| `clip2` | Birleştirilecek ikinci CLIP modeli. position IDs ve logit scale hariç, anahtar yamaları belirtilen orana göre birinci modele uygulanır. | CLIP | Evet | - |
| `oran` | İkinci modele ait özelliklerin birinci modele ne oranda karıştırılacağını belirler. 1.0 oranı, ikinci modelin özelliklerinin tamamen benimsenmesi anlamına gelirken, 0.0 oranı yalnızca birinci modelin özelliklerini korur. Varsayılan: 1.0. | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Belirtilen orana göre her iki girdi modelinin özelliklerini içeren, birleştirme sonucu elde edilen CLIP modeli. | CLIP |

## Birleştirme Mekanizması Açıklaması

### Birleştirme Algoritması

Düğüm, iki modeli birleştirmek için ağırlıklı ortalama kullanır:

1. **Temel Modeli Kopyala**: Önce `clip1` temel model olarak kopyalanır
2. **Yamaları Al**: `clip2`'den tüm anahtar yamalar elde edilir
3. **Özel Anahtarları Filtrele**: `.position_ids` ve `.logit_scale` ile biten anahtarlar atlanır
4. **Ağırlıklı Birleştirme Uygula**: `(1.0 - ratio) * clip1 + ratio * clip2` formülünü kullanır

### Oran Parametresi Açıklaması

- **ratio = 0.0**: `clip1`'i tamamen kullanır, `clip2`'yi yok sayar
- **ratio = 0.5**: Her iki modelden %50 katkı
- **ratio = 1.0**: `clip2`'yi tamamen kullanır, `clip1`'i yok sayar

## Kullanım Alanları

1. **Model Stili Füzyonu**: Farklı verilerle eğitilmiş CLIP modellerinin özelliklerini birleştirir
2. **Performans Optimizasyonu**: Farklı modellerin güçlü ve zayıf yönlerini dengeler
3. **Deneysel Araştırma**: Farklı CLIP kodlayıcı kombinasyonlarını keşfeder

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipMergeSimple/tr.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`

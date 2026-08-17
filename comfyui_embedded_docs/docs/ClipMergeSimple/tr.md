# Basit CLIP Birleştirme

`CLIPMergeSimple`, iki CLIP metin kodlayıcı modelini tek bir modelde birleştirir. İlk CLIP modelini temel olarak klonlar ve ikinci CLIP modelinden alınan ağırlıklı parametre yamalarını uygular; böylece sonuç her iki modelin özelliklerini birleştirir. `ratio` ayarı, her modelin ne kadar güçlü katkıda bulunacağını kontrol eder; varsayılan 1.0 değerinde ilk model değiştirilmeden kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip1` | İlk CLIP modeli. Birleştirme için temel model olarak klonlanır ve kullanılır. | CLIP | Evet | — |
| `clip2` | İkinci CLIP modeli. Anahtar yamaları, anahtarları `.position_ids` veya `.logit_scale` ile biten yamalar hariç temel modele uygulanır. | CLIP | Evet | — |
| `ratio` | İki modelin göreceli gücünü kontrol eder. Temel model (`clip1`), `ratio` değerine eşit bir güç korur ve `clip2`'nin yamaları `1.0 - ratio` gücüyle uygulanır. Varsayılan 1.0 değerinde çıktı `clip1`'e eşittir; daha düşük değerler `clip2`'yi daha fazla karıştırır; 0.0 değerinde `clip2`'nin yamaları tam güçle uygulanır. | FLOAT | Evet | 0.0 to 1.0 (default: 1.0, step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `clip` | Birleştirilmiş CLIP modeli: `ratio` değerine göre `clip2`'den alınan yamalar uygulanmış `clip1` klonudur. | CLIP |

## Birleştirme Mekanizması Açıklaması

### Birleştirme Algoritması

Düğüm, iki modeli birleştirmek için ağırlıklı yama uygulaması kullanır:

1. **Temel Modeli Klonla**: Temel model olarak kullanılmak üzere `clip1`'i klonlar.
2. **Yamaları Al**: `clip2`'den tüm anahtar yamaları (parametre değerlerini) toplar.
3. **Özel Anahtarları Filtrele**: `.position_ids` ve `.logit_scale` ile biten anahtarları atlar, böylece bu parametreler değişmeden kalır.
4. **Ağırlıklı Birleştirmeyi Uygula**: `clip2`'nin yamalarını, `1.0 - ratio` yama gücüyle klonlanmış temel modele uygular; temel model ise `ratio` gücünü korur.

### Ratio Parametresi Açıklaması

- **ratio = 1.0**: Temel güç 1.0 ve yama gücü 0.0'dır, bu nedenle çıktı `clip1` ile aynıdır (varsayılan).
- **ratio = 0.5**: Temel güç ve yama gücü her ikisi de 0.5'tir, bu nedenle her iki model eşit güçte katkıda bulunur.
- **ratio = 0.0**: Temel güç 0.0 ve yama gücü 1.0'dır, bu nedenle `clip2`'nin yamaları tam güçle uygulanır.

## Kullanım Alanları

1. **Model Stili Füzyonu**: Farklı verilerle eğitilmiş CLIP modellerinin özelliklerini birleştirir.
2. **Performans Optimizasyonu**: Farklı modellerin güçlü ve zayıf yönlerini dengeler.
3. **Deneysel Araştırma**: Farklı CLIP kodlayıcılarının kombinasyonlarını keşfeder.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/tr.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`

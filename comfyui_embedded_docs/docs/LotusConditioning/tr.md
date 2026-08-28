# LotusKoşullandırma

LotusConditioning düğümü, Lotus modeli için önceden hesaplanmış koşullandırma (conditioning) embedding'leri sağlar. Referans uygulamayla eşitliği sağlamak için dondurulmuş bir kodlayıcıyı null koşullandırma ile kullanır ve çıkarım yapmaya veya büyük tensör dosyaları yüklemeye gerek kalmadan sabit kodlanmış prompt embedding'leri döndürür. Bu düğüm, üretim hattında doğrudan kullanılabilen sabit bir koşullandırma tensörü çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm herhangi bir girdi parametresi kabul etmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `koşullandırma` | Lotus modeli için önceden hesaplanmış koşullandırma embedding'leri; sabit prompt embedding'leri ve boş bir sözlük içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`

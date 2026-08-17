# LotusKoşullandırma

LotusConditioning düğümü, Lotus modeli için önceden hesaplanmış conditioning gömme vektörlerini sağlar. Referans uygulamayla eşitlik sağlamak için dondurulmuş bir kodlayıcıyı null conditioning ile kullanır ve sabit kodlanmış prompt gömme vektörlerini döndürür; böylece çıkarım yapılması veya büyük tensor dosyalarının yüklenmesi gerekmez. Bu düğüm, üretim hattında doğrudan kullanılabilen sabit bir conditioning tensoru çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm herhangi bir girdi parametresi kabul etmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Lotus modeli için önceden hesaplanmış conditioning gömme vektörleri; sabit prompt gömme vektörlerini ve boş bir sözlüğü içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`

# Euler Atasal Örnekleyici

The SamplerEulerAncestral düğümü, görüntü üretmek için bir Euler Ancestral örnekleyici oluşturur. Bu örnekleyici, Euler entegrasyonunu ancestral örnekleme teknikleriyle birleştiren belirli bir matematiksel yaklaşım kullanarak görüntü varyasyonları üretir. Düğüm, üretim sürecindeki rastgeleliği ve adım boyutunu kontrol eden parametreleri ayarlayarak örnekleme davranışını yapılandırmanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin adım boyutunu ve rastgeleliğini kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilen, yapılandırılmış bir Euler Ancestral örnekleyici döndürür. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/tr.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`

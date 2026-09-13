# Euler Atasal Örnekleyici

SamplerEulerAncestral düğümü, görüntü oluşturma sırasında kullanılabilecek bir Euler Ancestral örnekleyici oluşturur. Bu örnekleyici, Euler entegrasyonunu atasal örneklemeyle birleştirir; bu da her adımda bir miktar rastgelelik ekleyerek çeşitli sonuçlar üretir. Düğüm, ayarları aracılığıyla ne kadar rastgelelik uygulanacağını ayarlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin adım boyutunu ve stokastikliğini kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Evet | 0.0 - 100.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme işlem hattında kullanılabilecek yapılandırılmış bir Euler Ancestral örnekleyici döndürür. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/tr.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`

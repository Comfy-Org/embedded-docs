# Euler Atasal Örnekleyici

SamplerEulerAncestral düğümü, görüntü oluşturmak için bir Euler Atasal örnekleyici oluşturur. Bu örnekleyici, Euler entegrasyonunu atasal örnekleme teknikleriyle birleştiren belirli bir matematiksel yaklaşım kullanarak görüntü varyasyonları üretir. Düğüm, oluşturma süreci sırasında rastgeleliği ve adım boyutunu kontrol eden parametreleri ayarlayarak örnekleme davranışını yapılandırmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin adım boyutunu ve stokastikliğini kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Hayır | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. | FLOAT | Hayır | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilecek yapılandırılmış bir Euler Atasal örnekleyici döndürür. | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/tr.md)

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`

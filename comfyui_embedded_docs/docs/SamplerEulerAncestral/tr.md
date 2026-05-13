> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/tr.md)

SamplerEulerAncestral düğümü, görüntü oluşturmak için bir Euler Atasal örnekleyici oluşturur. Bu örnekleyici, Euler entegrasyonunu atasal örnekleme teknikleriyle birleştiren belirli bir matematiksel yaklaşım kullanarak görüntü varyasyonları üretir. Düğüm, oluşturma süreci sırasında rastgeleliği ve adım boyutunu kontrol eden parametreleri ayarlayarak örnekleme davranışını yapılandırmanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `eta` | FLOAT | Hayır | 0.0 - 100.0 | Örnekleme sürecinin adım boyutunu ve stokastikliğini kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. |
| `s_noise` | FLOAT | Hayır | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0). Bu gelişmiş bir parametredir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sampler` | SAMPLER | Örnekleme hattında kullanılabilecek yapılandırılmış bir Euler Atasal örnekleyici döndürür. |

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`

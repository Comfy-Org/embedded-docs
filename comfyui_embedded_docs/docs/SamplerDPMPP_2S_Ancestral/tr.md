# ÖrnekleyiciDPMPP_2S_Atasal

SamplerDPMPP_2S_Ancestral düğümü, görüntü üretmek için DPM++ 2S Ancestral örnekleme yöntemini kullanan bir örnekleyici oluşturur. Bu örnekleyici, belirli bir tutarlılığı korurken çeşitli sonuçlar üretmek için deterministik ve stokastik öğeleri birleştirir. Örnekleme süreci sırasında rastgeleliği ve gürültü seviyelerini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sırasında eklenen stokastik gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme süreci sırasında uygulanan gürültünün ölçeğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilen yapılandırılmış bir örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/tr.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`

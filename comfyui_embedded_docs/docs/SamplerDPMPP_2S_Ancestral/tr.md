> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/tr.md)

SamplerDPMPP_2S_Ancestral düğümü, görüntü üretmek için DPM++ 2S Ancestral örnekleme yöntemini kullanan bir örnekleyici oluşturur. Bu örnekleyici, belirli bir tutarlılığı korurken çeşitli sonuçlar üretmek için deterministik ve stokastik öğeleri birleştirir. Örnekleme işlemi sırasında rastgelelik ve gürültü seviyelerini kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen stokastik gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `s_gürültü` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme işlemi sırasında uygulanan gürültü ölçeğini kontrol eder (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sampler` | SAMPLER | Örnekleme hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür |

---
**Source fingerprint (SHA-256):** `9634c96934850f5b746cd7c8b29727396af534133b8d54b6bdac12e9e0975189`

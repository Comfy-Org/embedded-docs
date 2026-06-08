# TripoSplat Örnekleme Önizlemesi

Bu düğüm, bir TripoSplat modelini, standart KSampler düğümüyle kullanıldığında her örnekleme adımında çözümlenmiş gauss dağılımı sıçramasının (gaussian splat) canlı önizlemesini gösterecek şekilde yamalar. Çalışma prensibi, örnekleyicinin geri çağrımını (callback) sararak modelin çıktısını her adımdan sonra bir önizleme görüntüsüne çözümlemektir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Canlı önizleme için yamalanacak TripoSplat modeli | MODEL | Evet | |
| `vae` | TripoSplat VAE kod çözücüsü | VAE | Evet | |
| `octree_seviyesi` | Önizleme çözümlemesi için sekizlik ağaç derinliği (düşük = daha ucuz/kaba). Varsayılan: 5 | INT | Hayır | 2 ila 8 |
| `gauss_sayisi` | Önizleme için üretilecek gauss sayısı (32'nin katına yuvarlanır). Varsayılan: 16384 | INT | Hayır | 1024 ila 262144 (adım: 32) |
| `yana_dönüş` | Önizleme kamerası yatış açısı (derece). Varsayılan: 90.0 | FLOAT | Hayır | -360.0 ila 360.0 (adım: 1.0) |
| `eğim` | Önizleme kamerası eğim açısı (derece). Varsayılan: 15.0 | FLOAT | Hayır | -89.0 ila 89.0 (adım: 1.0) |
| `nokta_boyutu` | Piksel cinsinden maksimum sıçrama yarıçapı. Her gauss, ölçeğine göre boyutlandırılır ve bu değerle sınırlanır; düşük = daha ince/noktasal, yüksek = daha kaba. Varsayılan: 3 | INT | Hayır | 1 ila 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MODEL` | Canlı önizleme işlevselliği eklenmiş yamalı TripoSplat modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/tr.md)

---
**Source fingerprint (SHA-256):** `56d5eeb5255b42d90f8cffd50319791fe6ec755c6dad47478fe8cc2e9bb65dfb`

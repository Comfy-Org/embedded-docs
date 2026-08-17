# TripoSplat Örnekleme Önizlemesi

Bu düğüm, standart KSampler düğümüyle kullanıldığında her örnekleme adımında kod çözülmüş gaussyan splatının canlı önizlemesinin gösterilmesi için bir TripoSplat modelini yamalar. Örnekleyicinin geri çağırma işlevini sararak modelin çıktısını her adımdan sonra bir önizleme görüntüsüne kod çözer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|-------|
| `model` | Canlı önizleme için yamalanacak TripoSplat modeli | MODEL | Evet | |
| `vae` | TripoSplat VAE kod çözücü | VAE | Evet | |
| `octree_level` | Önizleme kod çözme için sekizli ağaç derinliği (düşük = daha ucuz/kaba). Varsayılan: 5 | INT | Hayır | 2 to 8 |
| `num_gaussians` | Önizleme için üretilecek gaussyan sayısı (32'nin katına yuvarlanır). Varsayılan: 16384 | INT | Hayır | 1024 to 262144 (step: 32) |
| `yaw` | Önizleme kamerasının yaw açısı (derece). Varsayılan: 90.0 | FLOAT | Hayır | -360.0 to 360.0 (step: 1.0) |
| `pitch` | Önizleme kamerasının pitch açısı (derece). Varsayılan: 15.0 | FLOAT | Hayır | -89.0 to 89.0 (step: 1.0) |
| `point_size` | Piksel cinsinden maksimum splat yarıçapı. Her gaussyan ölçeğine göre boyutlandırılır ve burada sınırlanır; düşük = daha ince/noktalı, yüksek = daha iri. Varsayılan: 3 | INT | Hayır | 1 to 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `MODEL` | Canlı önizleme işlevi eklenmiş yamalı TripoSplat modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/tr.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`

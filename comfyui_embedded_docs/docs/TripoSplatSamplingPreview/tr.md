# TripoSplat Örnekleme Önizlemesi

Bu düğüm, standart KSampler düğümüyle kullanıldığında her örnekleme adımında kodu çözülmüş Gaussian splat'ın canlı önizlemesinin gösterilmesi için bir TripoSplat modelini yamalar. Çalışma şekli, örnekleyicinin geri çağrımını sararak modelin çıktısını her adımdan sonra bir önizleme görüntüsüne dönüştürmektir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Canlı önizleme için yamalanacak TripoSplat modeli | MODEL | Evet | |
| `vae` | TripoSplat VAE kod çözücü | VAE | Evet | |
| `oktav_seviyesi` | Önizleme kod çözme için octree derinliği (düşük = daha ucuz/daha kaba). Varsayılan: 5 | INT | Hayır | 2 ila 8 |
| `gauss_sayısı` | Önizleme için üretilecek Gaussian sayısı (32'nin katına yuvarlanır). Varsayılan: 16384 | INT | Hayır | 1024 ila 262144 (adım: 32) |
| `yana_dönüş` | Önizleme kamerasının yaw açısı (derece). Varsayılan: 90.0 | FLOAT | Hayır | -360.0 ila 360.0 (adım: 1.0) |
| `eğim` | Önizleme kamerasının pitch açısı (derece). Varsayılan: 15.0 | FLOAT | Hayır | -89.0 ila 89.0 (adım: 1.0) |
| `nokta_boyutu` | Piksel cinsinden maksimum splat yarıçapı. Her Gaussian ölçeğine göre boyutlandırılır ve burada sınırlanır; düşük = daha ince/daha noktasal, yüksek = daha kaba. Varsayılan: 3 | INT | Hayır | 1 ila 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MODEL` | Canlı önizleme işlevi eklenmiş yamalı TripoSplat modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/tr.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`

# GizliİşlemTonEşlemeReinhard

LatentOperationTonemapReinhard düğümü, Reinhard ton eşlemesini gizli vektörlere uygular. Bu teknik, ortalama ve standart sapmaya dayalı istatistiksel bir yaklaşım kullanarak gizli vektörleri normalleştirir ve büyüklüklerini ayarlar; yoğunluk bir çarpan parametresiyle kontrol edilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `çarpan` | Ton eşleme efektinin yoğunluğunu kontrol eder (varsayılan: 1,0) | FLOAT | Hayır | 0,0 ile 100,0 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Gizli vektörlere uygulanabilen bir ton eşleme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/tr.md)

---
**Source fingerprint (SHA-256):** `70c04eaef06b749392a0c65f3d1267e52484f7cf956f87173d10ad935afcf98c`

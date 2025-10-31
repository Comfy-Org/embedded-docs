> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/tr.md)

LatentOperationTonemapReinhard düğümü, gizli vektörlere Reinhard ton eşleme uygular. Bu teknik, gizli vektörleri normalleştirir ve büyüklüklerini, yoğunluğu bir çarpan parametresi tarafından kontrol edilen ortalama ve standart sapmaya dayalı istatistiksel bir yaklaşımla ayarlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `multiplier` | FLOAT | Hayır | 0.0 - 100.0 | Ton eşleme efektinin yoğunluğunu kontrol eder (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Gizli vektörlere uygulanabilen bir ton eşleme işlemi döndürür |
# Video Bileşenlerini Al

Get Video Components düğümü, bir video dosyasındaki tüm ana öğeleri çıkarır. Videoyu ayrı karelere böler, ses parçasını çıkarır ve videonun kare hızı, bit derinliği ve renk uzayı bilgilerini sağlar. Bu sayede her bileşenle bağımsız olarak çalışıp daha ileri düzeyde işleme veya analiz yapabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `video` | Bileşenlerin çıkarılacağı video. | VIDEO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `görüntüler` | Videodan ayrı görüntüler olarak çıkarılan tek tek kareler. | IMAGE |
| `ses` | Videodan çıkarılan ses parçası. | AUDIO |
| `fps` | Videonun saniyedeki kare sayısı cinsinden kare hızı. | FLOAT |
| `bit_depth` | Videonun bit derinliği. | INT |
| `color_space` | Videonun renk uzayı. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/tr.md)

---
**Source fingerprint (SHA-256):** `ffe8b6c698cb9a855b8796768f068d403448cf56188ce4c5ead21bff30baff6e`

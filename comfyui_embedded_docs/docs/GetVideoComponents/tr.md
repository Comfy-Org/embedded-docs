# Video Bileşenlerini Al

Get Video Components düğümü, bir video dosyasındaki tüm ana öğeleri çıkarır. Videoyu ayrı karelere böler, ses parçasını çıkarır ve videonun kare hızı, bit derinliği ve renk uzayı bilgilerini sağlar. Bu sayede her öğeyle bağımsız olarak daha ileri işleme veya analiz için çalışabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Bileşenlerin çıkarılacağı video. | VIDEO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntüler` | Videodan ayrı görüntüler olarak çıkarılan tek tek kareler. | IMAGE |
| `ses` | Videodan çıkarılan ses parçası. | AUDIO |
| `fps` | Videonun saniyedeki kare sayısı (fps) cinsinden kare hızı. | FLOAT |
| `bit_depth` | Videonun bit derinliği. | COMBO |
| `color_space` | Videonun renk uzayı. | COMBO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/tr.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`

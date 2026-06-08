Video Bileşenlerini Al düğümü, bir video dosyasındaki tüm ana öğeleri çıkarır. Videoyu ayrı karelere ayırır, ses parçasını çıkarır ve videonun kare hızı bilgisini sağlar. Bu sayede her bir bileşenle bağımsız olarak çalışarak ileri işleme veya analiz yapabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Bileşenlerinin çıkarılacağı video. | VIDEO | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Videodan ayrı görüntüler olarak çıkarılan bireysel kareler. | IMAGE |
| `audio` | Videodan çıkarılan ses parçası. | AUDIO |
| `fps` | Videonun saniyedeki kare sayısı cinsinden kare hızı. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/tr.md)

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`

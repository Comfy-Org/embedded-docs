# Sesi Önizle

Preview Audio düğümü, sesi çıktı dizinine kaydetmeden doğrudan ComfyUI içinde dinlemenizi sağlar. Bir ses girdisi alır, ses verisinin gerçekten mevcut olduğunu kontrol eder ve ardından aynı sesi çıktısı olarak iletirken arayüzdeki bir önizleme oynatıcısı aracılığıyla oynatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Önizlenecek ses verisi. Bu girdi None ise düğüm bir ValueError yükseltir; bu, kaynak videoda ses parçası olmadığında meydana gelebilir. | AUDIO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Girdiden değiştirilmeden geçirilen ses verisi; böylece düğüm bir iş akışının ortasına yerleştirilebilir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/tr.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`

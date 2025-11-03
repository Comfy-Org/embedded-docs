> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/tr.md)

EmptyAudio düğümü, belirtilen süre, örnekleme hızı ve kanal konfigürasyonuna sahip sessiz bir ses klibi oluşturur. Tümü sıfırlardan oluşan bir dalga formu yaratır ve belirtilen süre boyunca tam sessizlik üretir. Bu düğüm, yer tutucu ses oluşturmak veya ses iş akışlarında sessiz bölümler üretmek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `duration` | FLOAT | Evet | 0.0 - 1.8446744073709552e+19 | Boş ses klibinin saniye cinsinden süresi (varsayılan: 60.0) |
| `sample_rate` | INT | Evet | - | Boş ses klibinin örnekleme hızı (varsayılan: 44100) |
| `channels` | INT | Evet | 1 - 2 | Ses kanalı sayısı (1 mono, 2 stereo için) (varsayılan: 2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Dalga formu verileri ve örnekleme hızı bilgisini içeren oluşturulmuş sessiz ses klibi |
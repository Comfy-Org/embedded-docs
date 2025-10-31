> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/tr.md)

RecordAudio düğümü, ses kayıt arayüzü aracılığıyla kaydedilmiş veya seçilmiş ses dosyalarını yükler. Ses dosyasını işler ve iş akışındaki diğer ses işleme düğümleri tarafından kullanılabilecek bir dalga formu formatına dönüştürür. Düğüm, örnekleme hızını otomatik olarak tespit eder ve ses verilerini daha fazla manipülasyon için hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO_RECORD | Evet | Yok | Ses kayıt arayüzünden gelen ses kaydı girdisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Dalga formu ve örnekleme hızı bilgilerini içeren işlenmiş ses verisi |
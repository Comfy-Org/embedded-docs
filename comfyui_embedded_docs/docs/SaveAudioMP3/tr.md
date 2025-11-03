> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

SaveAudioMP3 düğümü, ses verilerini bir MP3 dosyası olarak kaydeder. Ses girişini alır ve özelleştirilebilir dosya adı ve kalite ayarlarıyla belirtilen çıktı dizinine aktarır. Düğüm, oynatılabilir bir MP3 dosyası oluşturmak için dosya adlandırmayı ve format dönüşümünü otomatik olarak halleder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | MP3 dosyası olarak kaydedilecek ses verisi |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") |
| `quality` | STRING | Hayır | "V0"<br>"128k"<br>"320k" | MP3 dosyası için ses kalitesi ayarı (varsayılan: "V0") |
| `prompt` | PROMPT | Hayır | - | Dahili prompt verileri (sistem tarafından otomatik olarak sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek PNG bilgileri (sistem tarafından otomatik olarak sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | - | Bu düğüm herhangi bir çıktı verisi döndürmez, ancak ses dosyasını çıktı dizinine kaydeder |
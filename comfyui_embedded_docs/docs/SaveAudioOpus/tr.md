> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

SaveAudioOpus düğümü, ses verilerini Opus formatında bir dosyaya kaydeder. Ses girişini alır ve yapılandırılabilir kalite ayarlarıyla sıkıştırılmış bir Opus dosyası olarak dışa aktarır. Düğüm, dosya adlandırmayı otomatik olarak halleder ve çıktıyı belirlenen çıktı dizinine kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Opus dosyası olarak kaydedilecek ses verisi |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") |
| `quality` | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | Opus dosyası için ses kalitesi ayarı (varsayılan: "128k") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğüm herhangi bir çıktı değeri döndürmez. Birincil işlevi olarak ses dosyasını diske kaydeder. |
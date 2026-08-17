# Sesi Kaydet (Opus)

SaveAudioOpus düğümü, ses verilerini Opus formatında bir dosyaya kaydeder. Bir ses girdisi alır ve yapılandırılabilir kalite ayarlarıyla sıkıştırılmış bir Opus dosyası olarak dışa aktarır. Bu düğüm kullanımdan kaldırılmıştır ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Opus dosyası olarak kaydedilecek ses verisi. Hiçbir ses sağlanmazsa (örneğin, kaynak videoda ses parçası yoksa) düğüm bir hata verir. | AUDIO | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `quality` | Opus dosyası için ses kalitesi (bit hızı) ayarı (varsayılan: "128k") | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Opus dosyası diske kaydedildikten sonra döndürülen girdi ses verisi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

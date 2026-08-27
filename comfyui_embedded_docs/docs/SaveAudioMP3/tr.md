# Ses Kaydet (MP3)

SaveAudioMP3 düğümü, ses verilerini MP3 dosyası olarak kaydeder. Bir ses girdisi alır ve özelleştirilebilir dosya adı ve kalite ayarlarıyla çıktı dizinine aktarır; dosya adlandırma ve MP3 formatına dönüştürme işlemlerini otomatik olarak yönetir. **Bu düğüm kullanımdan kaldırılmıştır ve gelecek sürümlerde kaldırılabilir.**

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `ses` | MP3 dosyası olarak kaydedilecek ses verisi | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `kalite` | MP3 dosyası için ses kalitesi ayarı (varsayılan: "V0") | COMBO | Hayır | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Sistem tarafından otomatik sağlanan dahili prompt verisi | PROMPT | Hayır | - |
| `extra_pnginfo` | Sistem tarafından otomatik sağlanan ek PNG bilgisi | EXTRA_PNGINFO | Hayır | - |

**Not:** `audio` girdisi None ise (örneğin, kaynak videoda ses parçası olmadığında), düğüm bir ValueError fırlatır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `audio` | MP3 dosyası olarak kaydedilen ses verisi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

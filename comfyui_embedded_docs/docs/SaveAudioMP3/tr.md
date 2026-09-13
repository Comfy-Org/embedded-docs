# Ses Kaydet (MP3)

SaveAudioMP3 düğümü, ses verisini MP3 dosyası olarak kaydeder. Bir ses girdisi alır ve özelleştirilebilir bir dosya adı ve kalite ayarıyla çıktı dizinine aktarır; dosya adlandırma ve MP3 formatı dönüşümünü otomatik olarak yönetir. **Bu düğüm kullanımdan kaldırılmıştır ve gelecek sürümlerde kaldırılabilir.**

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | MP3 dosyası olarak kaydedilecek ses verisi | AUDIO | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `quality` | MP3 dosyası için ses kalitesi ayarı (varsayılan: "V0") | COMBO | Hayır | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Dahili prompt verisi, sistem tarafından otomatik olarak sağlanır | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG bilgisi, sistem tarafından otomatik olarak sağlanır | EXTRA_PNGINFO | Hayır | - |

**Not:** `audio` girdisi None ise (örneğin, kaynak videonun ses parçası yoksa), düğüm bir ValueError yükseltir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `audio` | MP3 dosyasına kaydedilen ses verisi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

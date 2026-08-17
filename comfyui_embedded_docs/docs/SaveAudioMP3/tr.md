# Ses Kaydet (MP3)

SaveAudioMP3 düğümü, ses verilerini MP3 dosyası olarak kaydeder. Bir ses girdisi alır ve özelleştirilebilir bir dosya adı öneki ve kalite ayarıyla çıktı dizinine yazar. Bu düğüm kullanımdan kaldırılmıştır ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | MP3 dosyası olarak kaydedilecek ses verisi | AUDIO | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `quality` | MP3 kodlama kalite ayarı (varsayılan: "V0"). V0, yüksek kalite için değişken bit hızı kullanır; 128k ve 320k, 128 ve 320 kbps sabit bit hızlarını kullanır | COMBO | Hayır | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Sistem tarafından otomatik olarak sağlanan dahili prompt verisi | PROMPT | Hayır | - |
| `extra_pnginfo` | Sistem tarafından otomatik olarak sağlanan ek PNG bilgisi | EXTRA_PNGINFO | Hayır | - |

**Not:** `audio` girdisi None ise (örneğin, kaynak videoda ses parçası olmadığında), düğüm bir ValueError hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | MP3 dosyası olarak kaydedilen ses verisi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

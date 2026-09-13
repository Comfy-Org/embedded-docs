# Sesi Kaydet

Bu düğüm, ses verilerini FLAC formatında bir dosyaya kaydeder. Bir ses girişi alır ve belirtilen dosya adı ön ekini kullanarak çıktı dizinine yazar; ayrıca sesi çıkışına da aktarır. Bu düğüm kullanımdan kaldırılmıştır ve güncel Save Audio düğümüyle değiştirilmelidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Kaydedilecek ses verileri | AUDIO | Evet | - |
| `filename_prefix` | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |

*Not: `prompt` ve `extra_pnginfo` parametreleri gizlidir ve sistem tarafından otomatik olarak işlenir.*

Eğer `audio` girişi herhangi bir veri almazsa (örneğin, kaynak videonun ses parçası yoksa), düğüm bir hata verir ve hiçbir dosya kaydedilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Dosya kaydedildikten sonra çıkışa aktarılan, girişe sağlanan ses verileri | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/tr.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

# Sesi Kaydet

SaveAudio düğümü, ses verilerini FLAC biçiminde bir dosyaya kaydeder. Bir ses girdisi alır, belirtilen dosya adı önekini kullanarak çıktı dizinine yazar ve aynı ses verisini çıktısı olarak iletir. Bu düğüm kullanımdan kaldırılmıştır ve güncel Save Audio düğümü ile değiştirilmelidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Kaydedilecek ses verisi | AUDIO | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |

Düğüm, `audio` değeri None olduğunda bir hata verir; bu, kaynak videoda ses parçası olmadığında meydana gelebilir.

`prompt` ve `extra_pnginfo` parametreleri gizlidir ve sistem tarafından otomatik olarak yönetilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Dosyaya kaydedilen ses verisinin aynısı | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/tr.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

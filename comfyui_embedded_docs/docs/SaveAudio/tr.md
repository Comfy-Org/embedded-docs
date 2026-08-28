# Sesi Kaydet

Bu düğüm, ses verilerini FLAC formatında bir dosyaya kaydeder. Bir ses girdisi alır ve belirtilen dosya adı önekiyle çıktı dizinine yazar. Bu düğüm kullanımdan kaldırılmıştır ve mevcut Ses Kaydet düğümüyle değiştirilmelidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Kaydedilecek ses verisi | AUDIO | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adı öneki (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |

*Not: `prompt` ve `extra_pnginfo` parametreleri gizlidir ve sistem tarafından otomatik olarak işlenir.*

Eğer `audio` girdisi hiç veri almazsa (örneğin, kaynak videoda ses parçası yoksa), düğüm bir hata verir ve hiçbir dosya kaydedilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Girdiye sağlanan ses verisi, dosya kaydedildikten sonra olduğu gibi iletilir | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/tr.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/tr.md)

SaveAudio düğümü, ses verilerini FLAC formatında bir dosyaya kaydeder. Ses girişini alır ve belirtilen çıktı dizinine verilen dosya adı önekiyle yazar. Düğüm, dosya adlandırmayı otomatik olarak halleder ve sesin daha sonra kullanılmak üzere düzgün şekilde kaydedilmesini sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Kaydedilecek ses verisi |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") |

*Not: `prompt` ve `extra_pnginfo` parametreleri gizlidir ve sistem tarafından otomatik olarak işlenir.*

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Yok* | - | Bu düğüm herhangi bir çıktı verisi döndürmez, ancak ses dosyasını çıktı dizinine kaydeder |
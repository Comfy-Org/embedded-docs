> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/tr.md)

Metin açıklamalarından yüksek kaliteli müzik ve ses efektleri oluşturur. Bu düğüm, metin istemlerinize dayanarak ses içeriği oluşturmak için Stability AI'nin ses üretim teknolojisini kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"stable-audio-2.5"` | Kullanılacak ses üretim modeli (varsayılan: "stable-audio-2.5") |
| `prompt` | STRING | Evet | - | Ses içeriği oluşturmak için kullanılan metin açıklaması (varsayılan: boş dize) |
| `duration` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) |
| `seed` | INT | Hayır | 0-4294967294 | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0) |
| `steps` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Metin istemine dayalı olarak oluşturulan ses dosyası |
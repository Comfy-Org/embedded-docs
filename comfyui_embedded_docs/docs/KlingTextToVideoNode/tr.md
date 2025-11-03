> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

Kling Metinden Videoya Düğümü, metin açıklamalarını video içeriğine dönüştürür. Metin istemlerini alır ve belirtilen yapılandırma ayarlarına dayalı olarak karşılık gelen video dizileri oluşturur. Düğüm, farklı en-boy oranlarını ve üretim modlarını destekleyerek değişen sürelerde ve kalitelerde videolar üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Olumlu metin istemi (varsayılan: yok) |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin istemi (varsayılan: yok) |
| `cfg_ölçeği` | FLOAT | Hayır | 0.0-1.0 | Yapılandırma ölçeği değeri (varsayılan: 1.0) |
| `en_boy_oranı` | COMBO | Hayır | KlingVideoGenAspectRatio'dan seçenekler | Video en-boy oranı ayarı (varsayılan: "16:9") |
| `mod` | COMBO | Hayır | Birden fazla seçenek mevcut | Video oluşturma için kullanılacak, şu biçimi izleyen yapılandırma: mod / süre / model_adı. (varsayılan: modlar[4]) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Oluşturulan video çıktısı |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan video için süre bilgisi |
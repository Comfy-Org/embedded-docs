> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/tr.md)

Mevcut ses örneklerini metin talimatlarını kullanarak yeni yüksek kaliteli bestelere dönüştürür. Bu düğüm, bir giriş ses dosyası alır ve yeni ses içeriği oluşturmak için metin isteminize dayalı olarak değiştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "stable-audio-2.5"<br> | Ses dönüşümü için kullanılacak AI modeli |
| `prompt` | STRING | Evet |  | Sesi nasıl dönüştüreceğini açıklayan metin talimatları (varsayılan: boş) |
| `audio` | AUDIO | Evet |  | Ses 6 ila 190 saniye arasında olmalıdır |
| `duration` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) |
| `seed` | INT | Hayır | 0-4294967294 | Üretim için kullanılan rastgele tohum (varsayılan: 0) |
| `steps` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) |
| `strength` | FLOAT | Hayır | 0.01-1.0 | Parametre, ses parametresinin oluşturulan ses üzerinde ne kadar etkisi olduğunu kontrol eder (varsayılan: 1.0) |

**Not:** Giriş sesinin süresi 6 ila 190 saniye arasında olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Giriş sesi ve metin istemine dayalı olarak oluşturulan dönüştürülmüş ses |
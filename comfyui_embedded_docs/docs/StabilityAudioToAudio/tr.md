# Stability AI Ses'ten Ses'e

Mevcut ses örneklerini metin talimatları kullanarak yeni, yüksek kaliteli bestelere dönüştürür. Bu düğüm, bir giriş ses dosyasını alır ve metin isteminize dayanarak onu değiştirerek yeni ses içeriği oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Ses dönüşümü için kullanılacak AI modeli | COMBO | Evet | "stable-audio-2.5"<br> |
| `komut` | Sesin nasıl dönüştürüleceğini açıklayan metin talimatları (varsayılan: boş) | STRING | Evet |  |
| `ses` | Ses, 6 ila 190 saniye arasında uzunlukta olmalıdır | AUDIO | Evet |  |
| `süre` | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) | INT | Hayır | 1-190 |
| `tohum` | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0-4294967294 |
| `adımlar` | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) | INT | Hayır | 4-8 |
| `güç` | Bu parametre, ses parametresinin oluşturulan ses üzerindeki etki düzeyini kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.01-1.0 |

**Not:** Giriş sesi 6 ila 190 saniye arasında uzunlukta olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ses` | Giriş sesi ve metin istemine dayalı olarak oluşturulan dönüştürülmüş ses | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/tr.md)

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`

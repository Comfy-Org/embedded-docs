> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/tr.md)

Mevcut ses örneklerini metin talimatları kullanarak yeni, yüksek kaliteli bestelere dönüştürür. Bu düğüm, bir giriş ses dosyasını alır ve metin isteminize dayanarak onu değiştirerek yeni ses içeriği oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "stable-audio-2.5"<br> | Ses dönüşümü için kullanılacak AI modeli |
| `komut` | STRING | Evet |  | Sesin nasıl dönüştürüleceğini açıklayan metin talimatları (varsayılan: boş) |
| `ses` | AUDIO | Evet |  | Ses, 6 ila 190 saniye arasında uzunlukta olmalıdır |
| `süre` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) |
| `tohum` | INT | Hayır | 0-4294967294 | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0) |
| `adımlar` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) |
| `güç` | FLOAT | Hayır | 0.01-1.0 | Bu parametre, ses parametresinin oluşturulan ses üzerindeki etki düzeyini kontrol eder (varsayılan: 1.0) |

**Not:** Giriş sesi 6 ila 190 saniye arasında uzunlukta olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ses` | AUDIO | Giriş sesi ve metin istemine dayalı olarak oluşturulan dönüştürülmüş ses |

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`

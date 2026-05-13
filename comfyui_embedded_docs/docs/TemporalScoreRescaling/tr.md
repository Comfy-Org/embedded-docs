> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

Bu düğüm, bir difüzyon modeline Zamansal Puan Yeniden Ölçekleme (TSR) uygular. Gürültü giderme işlemi sırasında tahmin edilen gürültüyü veya puanı yeniden ölçeklendirerek modelin örnekleme davranışını değiştirir; bu, oluşturulan çıktının çeşitliliğini yönlendirebilir. Bu, bir CFG (Sınıflandırıcısız Kılavuzluk) sonrası işlevi olarak uygulanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | TSR işleviyle yamalanacak difüzyon modeli. |
| `tsr_k` | FLOAT | Hayır | 0.01 - 100.0 | Yeniden ölçekleme gücünü kontrol eder. Daha düşük k değeri, görüntü oluşturmada daha ayrıntılı sonuçlar üretir; daha yüksek k değeri ise daha yumuşak sonuçlar üretir. k = 1 olarak ayarlandığında yeniden ölçekleme devre dışı bırakılır. (varsayılan: 0.95) |
| `tsr_sigma` | FLOAT | Hayır | 0.01 - 100.0 | Yeniden ölçeklemenin ne kadar erken etkili olacağını kontrol eder. Daha büyük değerler daha erken etkili olur. (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Örnekleme sürecine Zamansal Puan Yeniden Ölçekleme işlevi uygulanmış olan giriş modeli. |

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`

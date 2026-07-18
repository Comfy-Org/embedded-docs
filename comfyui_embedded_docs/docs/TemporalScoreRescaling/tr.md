Bu düğüm, bir difüzyon modeline Zamansal Puan Yeniden Ölçekleme (TSR) uygular. Gürültü giderme işlemi sırasında tahmin edilen gürültüyü veya puanı yeniden ölçeklendirerek modelin örnekleme davranışını değiştirir; bu, oluşturulan çıktının çeşitliliğini yönlendirebilir. Bu, bir CFG (Sınıflandırıcısız Kılavuzluk) sonrası işlevi olarak uygulanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | TSR işleviyle yamalanacak difüzyon modeli. | MODEL | Evet | - |
| `tsr_k` | Yeniden ölçekleme gücünü kontrol eder. Daha düşük k değeri, görüntü oluşturmada daha ayrıntılı sonuçlar üretir; daha yüksek k değeri ise daha yumuşak sonuçlar üretir. k = 1 olarak ayarlandığında yeniden ölçekleme devre dışı bırakılır. (varsayılan: 0.95) | FLOAT | Hayır | 0.01 - 100.0 |
| `tsr_sigma` | Yeniden ölçeklemenin ne kadar erken etkili olacağını kontrol eder. Daha büyük değerler daha erken etkili olur. (varsayılan: 1.0) | FLOAT | Hayır | 0.01 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yama_uygulanmış_model` | Örnekleme sürecine Zamansal Puan Yeniden Ölçekleme işlevi uygulanmış olan giriş modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/tr.md)

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`

# Sonilo Metinden Müzik Üret

Sonilo Metinden Müziğe düğümü, Sonilo'nun yapay zeka modelini kullanarak bir metin açıklamasından müzik üretir. İstediğiniz müziği tanımlayan bir istem sağlarsınız ve düğüm, bir ses dosyası oluşturmak için Sonilo hizmetine bir istek gönderir. Hedeflenen bir süre belirtebilir veya modelin bunu isteminizden çıkarmasına izin verebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Oluşturulacak müziği tanımlayan metin istemi. Bu alan zorunludur. | STRING | Evet | Yok |
| `duration` | Saniye cinsinden hedef süre. Modelin süreyi istemden çıkarması için 0 olarak ayarlayın. Maksimum: 6 dakika (360 saniye). Varsayılan: 0. | INT | Hayır | 0 ila 360 |
| `seed` | Tekrarlanabilirlik için tohum değeri. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. Varsayılan: 0. | INT | Hayır | 0 ila 18446744073709551615 |

**Not:** `seed` girişi, iş akışı tutarlılığı için sağlanmıştır ancak şu anda Sonilo hizmetinin çıktısını etkilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Bir ses dosyası olarak oluşturulan müzik. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/tr.md)

---
**Source fingerprint (SHA-256):** `aac2762d9310179279ed7dcc9766f38342400902de2f8791b78d8092a96b86b4`

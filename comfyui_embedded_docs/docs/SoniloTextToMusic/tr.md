# Sonilo Metinden Müzik Üret

Sonilo Text to Music düğümü, Sonilo'nun yapay zeka modelini kullanarak bir metin açıklamasından müzik üretir. İstediğiniz müziği tanımlayan bir metin istemi girersiniz ve düğüm, bir ses dosyası oluşturmak için Sonilo hizmetine istek gönderir. Oluşturulan klip için hedef süre belirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek müziği tanımlayan metin istemi. Boşluklar kırpıldıktan sonra 1 ila 1000 karakter içermelidir. | STRING | Evet | N/A |
| `duration` | Hedef süre (saniye cinsinden). Maksimum: 6 dakika. Varsayılan: 30. | INT | Hayır | 1 ile 360 |
| `seed` | Tekrarlanabilirlik için seed değeri. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. Varsayılan: 0. | INT | Hayır | 0 ile 18446744073709551615 |

**Notlar:**
- `seed` girdisi iş akışı tutarlılığı için sağlanmıştır ancak şu anda Sonilo hizmetinin çıktısını etkilemez.
- Kullanım, talep edilen `duration` süresinin saniyesi başına $0.0025 olarak faturalandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Ses dosyası olarak oluşturulan müzik. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/tr.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`

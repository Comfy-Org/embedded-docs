# Sonilo Metinden Müzik Üret

Sonilo Text to Music düğümü, Sonilo'nun AI modelini kullanarak bir metin açıklamasından müzik üretir. İstediğiniz müziği tanımlayan bir prompt sağlarsınız ve düğüm, bir ses dosyası oluşturmak için Sonilo hizmetine bir istek gönderir. Ayrıca üretilen müziğin hedef süresini de belirtebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek müziği tanımlayan metin promptu. 1 ile 1000 karakter arasında olmalıdır. | STRING | Evet | 1 to 1000 characters |
| `duration` | Hedef süre (saniye cinsinden). Maksimum: 6 dakika. Varsayılan: 30. | INT | Hayır | 1 to 360 |
| `seed` | Yeniden üretilebilirlik için seed. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. Varsayılan: 0. | INT | Hayır | 0 to 18446744073709551615 |

**Not:** `seed` girdisi iş akışı tutarlılığı için sağlanır ancak şu anda Sonilo hizmetinin çıktısını etkilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Bir ses dosyası olarak üretilen müzik. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/tr.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`

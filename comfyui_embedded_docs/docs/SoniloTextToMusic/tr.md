# Sonilo Metinden Müzik Üret

Sonilo Text to Music düğümü, Sonilo'nun yapay zeka modelini kullanarak bir metin açıklamasından müzik oluşturur. İstediğiniz müziği tanımlayan bir istem sağlarsınız ve düğüm, bir ses dosyası oluşturmak için Sonilo hizmetine istek gönderir. Oluşturulan klip için hedef bir süre ayarlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak müziği tanımlayan metin istemi. Boşluklar kırpıldıktan sonra 1 ila 1000 karakter içermelidir. | STRING | Evet | 1 ila 1000 karakter |
| `duration` | Hedef süre saniye cinsinden. Maksimum: 6 dakika. Varsayılan: 30. | INT | Hayır | 1 ila 360 |
| `seed` | Tekrarlanabilirlik için tohum. Şu anda Sonilo hizmeti tarafından yok sayılır ancak graf tutarlılığı için korunur. Varsayılan: 0. | INT | Hayır | 0 ila 18446744073709551615 |

**Notlar:**
- `seed` girdisi iş akışı tutarlılığı için sağlanmıştır ancak şu anda Sonilo hizmetinin çıktısını etkilemez.
- `prompt` girdisi zorunludur ve boş olmamalıdır; düğüm, boşluklar kırpıldıktan sonra en az 1 karakter ve en fazla 1000 karakter içerdiğini doğrular.
- Kullanım, istenen `duration` süresinin saniyesi başına $0.0025 olarak faturalandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Oluşturulan müzik, bir ses dosyası olarak. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/tr.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`

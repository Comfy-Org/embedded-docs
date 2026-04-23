> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/tr.md)

Sonilo Metin-Müzik düğümü, Sonilo'nun yapay zeka modelini kullanarak bir metin açıklamasından müzik üretir. İstediğiniz müziği tanımlayan bir yönlendirme sağlarsınız ve düğüm, bir ses dosyası oluşturmak için Sonilo hizmetine bir istek gönderir. Hedeflenen bir süre belirtebilir veya modelin bunu yönlendirmenizden çıkarmasına izin verebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `prompt` | STRING | Evet | Yok | Oluşturulacak müziği tanımlayan metin yönlendirmesi. Bu zorunlu bir alandır. |
| `duration` | INT | Hayır | 0 ila 360 | Saniye cinsinden hedeflenen süre. Modelin süreyi yönlendirmeden çıkarması için 0 olarak ayarlayın. Maksimum: 6 dakika (360 saniye). Varsayılan: 0. |
| `seed` | INT | Hayır | 0 ila 18446744073709551615 | Tekrarlanabilirlik için tohum değeri. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. Varsayılan: 0. |

**Not:** `seed` girişi, iş akışı tutarlılığı için sağlanmıştır ancak şu anda Sonilo hizmetinin çıktısını etkilemez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `audio` | AUDIO | Oluşturulan müzik bir ses dosyası olarak. |
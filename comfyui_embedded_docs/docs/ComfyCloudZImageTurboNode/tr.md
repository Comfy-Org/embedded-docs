# Comfy Cloud Z-Image Turbo Metinden Görüntüye [BETA]

Bu düğüm, yalnızca 8 adımda tamamlanan Z-Image Turbo modelini kullanarak bir metin isteminden görsel üretir. Üretim, Comfy Cloud GPU'larında uzaktan çalışır ve çalışma süresine göre faturalandırılır; bu da onu burada görsel fikirleri üzerinde yineleme yapmak için en hızlı ve en ucuz seçeneklerden biri haline getirir. Üretim tamamlandığında düğüm, iş akışınızda kullanılmak üzere tamamlanan görseli indirir. Bu düğüm, BETA olarak işaretlenmiş Comfy Cloud düğüm setinin bir parçasıdır: seçenekler eklenebilir veya kaldırılabilir ve bir iş akışı kullanımdan kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görseli tanımlayan metin istemi. Çok satırlı girişi kabul eder ve gönderilmeden önce baştaki/sondaki boşluklar kırpılır. Kırpma sonrasında boş olmamalıdır. Varsayılan: "" (boş). | STRING | Evet | 1 - 4096 characters |
| `seed` | Üretimin tekrarlanabilirliğini kontrol etmek için kullanılan rastgele tohum. Değiştirilmesi farklı bir varyasyon üretir. Üretim sonrası kontrol seçeneği içerir. Varsayılan: 42. | INT | Hayır | 0 - 18446744073709551615 |
| `aspect_ratio` | Oluşturulan görselin en-boy oranı. Varsayılan: "1:1". | COMBO | Hayır | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Toplam piksel bütçesi. Kare oranda 1.0 yaklaşık 1024x1024'tür. Varsayılan: 1.0. | FLOAT | Hayır | 0.1 - 16.0<br>(0.1 adım) |

Not: Giriş değerleri, üretim gönderilmeden önce doğrulanır. `prompt`, boşluklar kırpıldıktan sonra 1 ile 4.096 karakter arasında olmalıdır; `aspect_ratio` listelenen seçeneklerden biri olmalıdır ve `megapixels` 0,1'lik artışlarla girilmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Daha ileri görsel işleme veya kaydetme düğümleri için hazır, görüntü tensörü olarak döndürülen oluşturulmuş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/tr.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`

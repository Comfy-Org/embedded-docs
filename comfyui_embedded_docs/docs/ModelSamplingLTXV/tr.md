# ModelÖrneklemeLTXV

ModelSamplingLTXV düğümü, token sayısına göre modele gelişmiş örnekleme parametreleri uygular. Taban ve maksimum kaydırma değerleri arasında doğrusal enterpolasyon kullanarak bir kaydırma değeri hesaplar; hesaplama, giriş latenti içindeki token sayısına bağlıdır. Düğüm daha sonra özelleştirilmiş bir model örnekleme yapılandırması oluşturur ve bunu giriş modeline uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerinin uygulanacağı giriş modeli | MODEL | Evet | - |
| `maks_kaydırma` | Doğrusal enterpolasyon hesaplamasında kullanılan maksimum kaydırma değeri (varsayılan: 2.05) | FLOAT | Evet | 0.0 ile 100.0 (step: 0.01) |
| `temel_kaydırma` | Doğrusal enterpolasyon hesaplamasında kullanılan taban kaydırma değeri (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 100.0 (step: 0.01) |
| `gizli` | Kaydırma hesaplaması için token sayısını belirlemek amacıyla kullanılan isteğe bağlı latent giriş. Sağlanmazsa, varsayılan token sayısı olarak 4096 kullanılır | LATENT | Hayır | - |

Kaydırma değeri, `base_shift` ve `max_shift` arasında 1024 ila 4096 token aralığında enterpolasyon yapılarak hesaplanır. Bir `latent` sağlandığında, token sayısı uzamsal boyutlarının (yükseklik ve genişlik gibi) çarpımından hesaplanır. Hiçbir `latent` sağlanmazsa, token sayısı varsayılan olarak 4096 olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme parametreleri uygulanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`

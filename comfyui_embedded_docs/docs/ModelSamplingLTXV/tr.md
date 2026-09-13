# ModelÖrneklemeLTXV

ModelSamplingLTXV düğümü, token sayısına bağlı olarak bir modele gelişmiş örnekleme parametreleri uygular. Bir token aralığı boyunca `base_shift` ile `max_shift` arasında doğrusal enterpolasyon yaparak bir shift değeri hesaplar, ardından girdi modelini özelleştirilmiş bir örnekleme yapılandırmasıyla yamalar. Bir latent sağlanırsa, boyutları token sayısını belirler; aksi takdirde 4096 token kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerinin uygulanacağı girdi modeli. | MODEL | Evet | - |
| `max_shift` | Doğrusal enterpolasyon hesaplamasında kullanılan maksimum shift değeri (varsayılan: 2.05). | FLOAT | Evet | 0.0 ile 100.0 (step: 0.01) |
| `base_shift` | Doğrusal enterpolasyon hesaplamasında kullanılan temel shift değeri (varsayılan: 0.95). | FLOAT | Evet | 0.0 ile 100.0 (step: 0.01) |
| `latent` | Shift hesaplaması için token sayısını belirlemek üzere kullanılan isteğe bağlı latent girdisi. Sağlanmazsa, varsayılan 4096 token sayısı kullanılır. | LATENT | Hayır | - |

Shift değeri, 1024 token'da `base_shift` ile 4096 token'da `max_shift` arasında enterpolasyon yapılarak hesaplanır. `latent` sağlandığında, token sayısı latent örneklerindeki ilk iki boyuttan sonraki tüm boyutların çarpımıdır (uzamsal/zamansal boyutlar). `latent` sağlanmazsa, token sayısı varsayılan olarak 4096 olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Uygulanan örnekleme parametreleriyle değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`

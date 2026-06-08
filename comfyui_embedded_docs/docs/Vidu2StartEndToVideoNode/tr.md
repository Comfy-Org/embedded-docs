## Genel Bakış

Bu düğüm, bir metin yönlendirmesi rehberliğinde sağlanan başlangıç karesi ile bitiş karesi arasında enterpolasyon yaparak bir video oluşturur. Belirtilen Vidu modelini kullanarak iki görüntü arasında belirlenen süre boyunca yumuşak bir geçiş sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak Vidu modeli. | COMBO | Evet | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `ilk_kare` | Video dizisi için başlangıç görüntüsü. Yalnızca tek bir görüntüye izin verilir. | IMAGE | Evet | - |
| `bitiş_kare` | Video dizisi için bitiş görüntüsü. Yalnızca tek bir görüntüye izin verilir. | IMAGE | Evet | - |
| `komut_istemi` | Video oluşturmayı yönlendiren metin açıklaması (maksimum 2000 karakter). | STRING | Evet | - |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Hayır | 2 ila 8 |
| `tohum` | Tekrarlanabilir sonuçlar için rastgele oluşturmayı başlatan sayı (varsayılan: 1). | INT | Hayır | 0 ila 2147483647 |
| `çözünürlük` | Oluşturulan videonun çıktı çözünürlüğü. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `hareket_genliği` | Karedeki nesnelerin hareket genliği. | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Not:** `first_frame` ve `end_frame` görüntüleri benzer en-boy oranlarına sahip olmalıdır. Düğüm, en-boy oranlarının 0,8 ila 1,25 aralığında olduğunu doğrulayacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`

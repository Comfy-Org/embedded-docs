> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/tr.md)

Vidu2 Görüntüden Videoya Oluşturma düğümü, tek bir giriş görüntüsünden başlayarak bir video dizisi oluşturur. İsteğe bağlı bir metin istemi temel alınarak sahneyi canlandırmak için belirtilen bir Vidu2 modelini kullanır ve videonun uzunluğunu, çözünürlüğünü ve hareket yoğunluğunu kontrol eder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | COMBO | Evet | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | Video oluşturma için kullanılacak Vidu2 modeli. Farklı modeller, hız ve kalite arasında değişen ödünleşimler sunar. |
| `görüntü` | IMAGE | Evet | - | Oluşturulan videonun başlangıç karesi olarak kullanılacak bir görüntü. Yalnızca bir görüntüye izin verilir. |
| `istem` | STRING | Hayır | - | Video oluşturma için isteğe bağlı bir metin istemi (en fazla 2000 karakter). Varsayılan değer boş bir dizedir. |
| `süre` | INT | Evet | 1 ile 10 | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan değer 5'tir. |
| `tohum` | INT | Hayır | 0 ile 2147483647 | Tekrarlanabilir sonuçlar elde etmek için rastgele sayı üretiminde kullanılan bir tohum değeri. Varsayılan değer 1'dir. |
| `çözünürlük` | COMBO | Evet | `"720p"`<br>`"1080p"` | Oluşturulan videonun çıktı çözünürlüğü. Bu parametre gelişmiştir. |
| `hareket_genliği` | COMBO | Evet | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Karedeki nesnelerin hareket genliği. Bu parametre gelişmiştir. |

**Kısıtlamalar:**

* `image` girişi tam olarak bir görüntü içermelidir.
* Giriş görüntüsünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır.
* `prompt` metni en fazla 2000 karakterle sınırlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`

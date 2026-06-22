# LumaRay32ExtendVideoNode

Bu düğüm, önceki bir Luma Ray 3.2 video oluşturmasını, ona yeni içerik ekleyerek genişletir: ya videodan sonra (ileriye doğru uzatma) ya da videodan önce (geriye doğru uzatma). Kesintisiz 5 saniyelik bir video uzantısı oluşturmak için önceki bir Luma Ray 3.2 düğümünün oluşturma kimliği çıktısını bağlayın.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | Uzatılacak önceki Ray 3.2 videosunun oluşturma kimliği. Başka bir Luma Ray 3.2 düğümünün generation_id çıktısını bağlayın. | STRING | Evet | - |
| `direction` | İleri, önceki klipten sonra devam eder; geri, ondan önce eklenir. "İleri (sonrasından devam et)" seçildiğinde, isteğe bağlı olarak döngü modunu etkinleştirebilirsiniz. | COMBO | Evet | "İleri (sonrasından devam et)"<br>"Geri (öncesine ekle)" |
| `loop` | Uzatılmış videoyu kesintisiz olarak döngüye alır (yalnızca ileri uzatma). | BOOLEAN | Hayır | Doğru<br>Yanlış |
| `prompt` | Oluşturulacak yeni içeriği tanımlayan metin istemi. | STRING | Evet | - |
| `resolution` | Uzatılmış video bölümü için çıktı çözünürlüğü. | COMBO | Evet | "540p"<br>"720p"<br>"1080p" |
| `seed` | Tekrarlanabilir oluşturma sonuçları için rastgele tohum değeri. | INT | Evet | - |

**Not:** `loop` parametresi yalnızca `direction` "İleri (sonrasından devam et)" olarak ayarlandığında kullanılabilir. "Geri (öncesine ekle)" kullanıldığında döngü seçeneği mevcut değildir. `prompt` 1 ile 6000 karakter arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan 5 saniyelik uzatılmış video bölümü. | VIDEO |
| `generation_id` | Bu oluşturma için benzersiz tanımlayıcıdır. Daha fazla uzatma için başka bir Luma Ray 3.2 Videoyu Uzat düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`

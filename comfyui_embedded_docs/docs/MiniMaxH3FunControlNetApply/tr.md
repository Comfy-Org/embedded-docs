# MiniMaxH3FunControlNetApply

Bu düğüm, bir metinden videoya modele MiniMax H3 Fun ControlNet'i bir model yaması olarak uygular. Üretimi yönlendirmek için isteğe bağlı bir kontrol videosu ve isteğe bağlı bir maske kullanabilir ve daha sonraki örnekleme için yamanmış bir model kopyası döndürür. Güç 0 olarak ayarlandığında veya ne bir kontrol videosu ne de bir maske sağlandığında, girdi modeli değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | MiniMax H3 Fun ControlNet yamasının uygulandığı difüzyon modeli. | MODEL | Evet | N/A |
| `model_patch` | Kontrol sinyalleri modele enjekte edilen MiniMax H3 Fun ControlNet yaması; belirtilen `model` ile uyumlu olmalıdır. | MODEL_PATCH | Evet | N/A |
| `vae` | Kontrol ve kaynak video karelerini modelin beklediği gizli uzaya kodlamak için kullanılan VAE. | VAE | Evet | N/A |
| `strength` | ControlNet etkisinin genel gücü. 0 olarak ayarlandığında düğüm hiçbir şey yapmaz ve girdi modelini değiştirmeden döndürür. (varsayılan: 1.0) | FLOAT | Evet | min 0.0, max 10.0, step 0.01 |
| `start_percent` | ControlNet'in etkin olduğu örnekleme aralığının başlangıcı; örnekleme çizelgesinin yüzdesi olarak ifade edilir. Dahili olarak eşdeğer sigma değerine dönüştürülür. (varsayılan: 0.0) | FLOAT | Evet | min 0.0, max 1.0, step 0.001 |
| `end_percent` | ControlNet'in etkin olduğu örnekleme aralığının sonu; örnekleme çizelgesinin yüzdesi olarak ifade edilir. Dahili olarak eşdeğer sigma değerine dönüştürülür. (varsayılan: 1.0) | FLOAT | Evet | min 0.0, max 1.0, step 0.001 |
| `control_video` | ControlNet görsel ipucu olarak kullanılan isteğe bağlı video kareleri. Kareler, üretilen videoyla eşleşecek şekilde yeniden boyutlandırılır ve `vae` ile kodlanır. | IMAGE | Hayır | N/A |
| `mask` | 1, yeniden üretilecek bölgeleri işaretler. 0.5'in üzerindeki maske değerleri işaretlenmiş bölgeler olarak ele alınır. | MASK | Hayır | N/A |
| `source_video` | Maske arkasındaki video; yalnızca bir maske verildiğinde okunur. | IMAGE | Hayır | N/A |

Not: Yamanın bir etkisinin olması için `strength` değerinin 0'dan büyük olması ve `control_video` veya `mask` girdilerinden en az birinin sağlanması gerekir. `source_video`, yalnızca `mask` sağlandığında dikkate alınır; `source_video` olmadan `mask` verilirse, maskeli bölgelerin arkasındaki içerik siyah olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Girdi modelin MiniMax H3 Fun ControlNet uygulanmış yamanmış bir kopyası. `strength` 0 ise veya hiçbir kontrol videosu ya da maskesi sağlanmazsa, orijinal model değiştirilmeden döndürülür. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/tr.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`

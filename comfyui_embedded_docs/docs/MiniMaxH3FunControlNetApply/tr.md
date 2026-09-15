# MiniMax H3 Fun ControlNet Uygula

Bu düğüm, bir metinden videoya modele MiniMax H3 Fun ControlNet'i model yaması olarak uygular. Oluşturmayı yönlendirmek için isteğe bağlı bir kontrol videosu ve isteğe bağlı bir maske kullanabilir ve daha sonraki örnekleme için modelin yamalanmış bir kopyasını döndürür. `strength` 0 olarak ayarlandığında ya da ne bir kontrol videosu ne de bir maske sağlandığında, girdi modeli değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | MiniMax H3 Fun ControlNet yamasının uygulandığı difüzyon modeli. | MODEL | Evet | N/A |
| `model_patch` | Kontrol sinyalleri modele enjekte edilen MiniMax H3 Fun ControlNet yaması; verilen `model` ile uyumlu olmalıdır. | MODEL_PATCH | Evet | N/A |
| `vae` | Kontrol ve kaynak video karelerini modelin beklediği latent uzayına kodlamak için kullanılan VAE. | VAE | Evet | N/A |
| `strength` | ControlNet etkisinin genel gücü. 0 olarak ayarlandığında düğüm hiçbir şey yapmaz ve girdi modelini değiştirilmeden döndürür. (varsayılan: 1.0) | FLOAT | Evet | min 0.0, max 10.0, step 0.01 |
| `start_percent` | ControlNet'in etkin olduğu örnekleme aralığının başlangıcı; örnekleme planının yüzdesi olarak ifade edilir. Dahili olarak eşdeğer sigma değerine dönüştürülür. Bu gelişmiş bir ayardır. (varsayılan: 0.0) | FLOAT | Evet | min 0.0, max 1.0, step 0.001 |
| `end_percent` | ControlNet'in etkin olduğu örnekleme aralığının sonu; örnekleme planının yüzdesi olarak ifade edilir. Dahili olarak eşdeğer sigma değerine dönüştürülür. Bu gelişmiş bir ayardır. (varsayılan: 1.0) | FLOAT | Evet | min 0.0, max 1.0, step 0.001 |
| `control_video` | ControlNet görsel ipucu olarak kullanılan isteğe bağlı video kareleri. Kareler, oluşturulan videoyla eşleşecek şekilde yeniden boyutlandırılır ve `vae` ile kodlanır. | IMAGE | Hayır | N/A |
| `mask` | 1, yeniden üretilecek bölgeleri işaretler. 0.5 üzerindeki maske değerleri işaretli bölgeler olarak değerlendirilir. | MASK | Hayır | N/A |
| `source_video` | Maskenin arkasındaki video; yalnızca bir maske verildiğinde okunur. | IMAGE | Hayır | N/A |

Not: Yamanın etkili olması için `strength` 0'dan büyük olmalı ve `control_video` veya `mask` seçeneklerinden en az biri sağlanmalıdır. `mask` sağlanmadıkça `source_video` yok sayılır; `source_video` olmadan `mask` verilirse, maskelenen bölgelerin arkasındaki içerik siyah olarak değerlendirilir. Hem `control_video` hem de `mask` sağlandığında, kontrol ipucu kontrol videosu özniteliklerini maskelenmiş kaynak içeriğiyle birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | MiniMax H3 Fun ControlNet uygulanmış, girdi modelinin yamalanmış bir kopyası. `strength` 0 ise veya herhangi bir kontrol videosu ya da maske sağlanmamışsa, özgün model değiştirilmeden döndürülür. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/tr.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`

# Ideogram P-Image

Ideogram & Pruna P-Image, Ideogram'ın güçlü tipografi ve fotogerçekçilik yönleriyle bilinen hızlı metinden görüntü modelini kullanarak bir metin isteminden görüntüler üretir. Ayrıca metin dizeleri, renkler ve düzen üzerinde kesin kontrol için Ideogram 4.0 yapılandırılmış JSON açıklamalarını destekler. Düğüm, üretilen görüntü(ler)i, görüntünün gerçekte üretildiği son istemle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Metin istemi. Ayrıca Ideogram 4.0 yapılandırılmış JSON açıklamasını kabul eder (kesin renkler #RRGGBB hex olarak, kesin metin dizeleri, sınır kutusu düzeni) — olduğu gibi kullanmak için prompt_upsampling değerini OFF olarak ayarlayın. Boş olmamalıdır. (varsayılan: "") | STRING | Evet | Boş olmayan herhangi bir metin |
| `quality` | Hız/fiyat/kalite seviyesi. MEDIUM günlük varsayılandır; HIGH karmaşık istemler, ince ayrıntılar ve zor metinler için; VERY_LOW/LOW ölçekli taslaklar için. Zor metinler MEDIUM altında düşük kalitede işlenir. (varsayılan: "MEDIUM") | COMBO | Evet | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Çıktı boyut sınıfı (kesin pikseller en-boy oranına bağlıdır, örn. 16:9, 1K'da 1280x720 ve 2K'da 2560x1440 verir). Net tipografi için HIGH + 2K tercih edin. (varsayılan: "1K") | COMBO | Evet | "1K"<br>"2K" |
| `aspect_ratio` | Görüntü üretimi için en-boy oranı. (varsayılan: "1:1") | COMBO | Evet | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Kısa istemleri üretimden önce ayrıntılı yapılandırılmış bir açıklamaya genişletir (yeniden yazılan istem final_prompt olarak döndürülür). Kendi JSON açıklamanızı veya kesin ifadenizi sağlarken OFF olarak ayarlayın. (varsayılan: "AUTO") | COMBO | Evet | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Tekrarlanabilir üretim için tohum (seed). prompt_upsampling OFF iken aynı tohum ve ayarlar aynı görüntüyü döndürür; ON/AUTO iken istem yeniden yazımı her çalıştırmada değişir — bir sonucu çoğaltmak için final_prompt çıktısını prompt_upsampling OFF ve aynı tohumla yeniden kullanın. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |

**Kısıtlamalar hakkında not:** İstem, en az bir boşluk olmayan karakter içermelidir, aksi takdirde düğüm başarısız olur. Kendi yapılandırılmış JSON açıklamanızı veya kesin ifadenizi sağlarken `prompt_upsampling` değerini OFF olarak ayarlayın. `prompt_upsampling` ON veya AUTO olduğunda, istem üretimden önce yeniden yazılır, bu nedenle aynı tohum aynı görüntüyü üretmeyebilir; bir görüntüyü çoğaltmak için `final_prompt` çıktısını `prompt_upsampling` OFF ve aynı tohumla yeniden kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Üretilen görüntü(ler), bir görüntü grubu (batch) olarak döndürülür. Ideogram'ın içerik güvenlik filtresi üretimi engellerse, bunun yerine bir hata oluşturulur. | IMAGE |
| `final_prompt` | Görüntünün gerçekte üretildiği istem (prompt_upsampling çalıştığında yeniden yazılan yapılandırılmış açıklama, aksi takdirde sizin isteminiz). Bu görüntüyü çoğaltmak için prompt_upsampling OFF ve aynı tohumla geri besleyin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/tr.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`

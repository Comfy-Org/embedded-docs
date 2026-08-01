# IdeogramPImage

Ideogram P-Image, Ideogram'ın hızlı metin-görüntü modelini kullanarak bir metin isteminden görüntü üretir; bu model güçlü tipografi ve fotogerçekçilik özellikleriyle bilinir. Ayrıca metin dizeleri, renkler ve düzen üzerinde hassas kontrol için Ideogram 4.0 yapılandırılmış JSON başlıklarını (structured JSON captions) da destekler. Düğüm, üretilen görüntü(ler)i ve görüntünün gerçekte üretildiği nihai istemi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Metin istemi. Ayrıca bir Ideogram 4.0 yapılandırılmış JSON başlığını da kabul eder (#RRGGBB hex olarak tam renkler, tam metin dizeleri, sınırlayıcı kutu düzeni) — aynen kullanmak için prompt_upsampling değerini OFF olarak ayarlayın. Boş olmamalıdır. (varsayılan: "") | STRING | Evet | Herhangi bir metin |
| `quality` | Hız/fiyat/kalite kademesi. MEDIUM günlük kullanım için varsayılandır; HIGH karmaşık istemler, ince ayrıntılar ve zor metinler için; VERY_LOW/LOW ölçekte taslaklar için. Zor metinler MEDIUM seviyesinin altında kötü işlenir. (varsayılan: "MEDIUM") | STRING | Evet | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Çıktı boyut sınıfı (tam piksel sayısı en-boy oranını takip eder, örn. 16:9, 1K'da 1280x720 ve 2K'da 2560x1440 verir). Keskin tipografi için HIGH + 2K tercih edin. (varsayılan: "1K") | STRING | Evet | "1K"<br>"2K" |
| `aspect_ratio` | Görüntü üretimi için en-boy oranı. (varsayılan: "1:1") | STRING | Evet | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Kısa istemleri üretimden önce ayrıntılı bir yapılandırılmış başlığa genişletir (yeniden yazılan istem final_prompt olarak döndürülür). Kendi JSON başlığınızı veya tam ifadenizi sağlarken OFF olarak ayarlayın. (varsayılan: "AUTO") | STRING | Evet | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Tekrarlanabilir üretim için tohum değeri. prompt_upsampling OFF iken aynı tohum ve ayarlar aynı görüntüyü döndürür; ON/AUTO iken istem yeniden yazımı her çalıştırmada değişir — bir sonucu yeniden üretmek için final_prompt çıktısını prompt_upsampling OFF ve aynı tohumla yeniden kullanın. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |

**Kısıtlamalar hakkında not:** İstem en az bir boşluk olmayan karakter içermelidir, aksi takdirde düğüm başarısız olur. Kendi yapılandırılmış JSON başlığınızı veya tam ifadenizi sağlarken `prompt_upsampling` değerini OFF olarak ayarlayın. `prompt_upsampling` ON veya AUTO olduğunda, istem üretimden önce yeniden yazılır, bu nedenle aynı tohum aynı görüntüyü üretmeyebilir; bir görüntüyü yeniden üretmek için `final_prompt` çıktısını `prompt_upsampling` OFF ve aynı tohumla yeniden kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Üretilen görüntü(ler), bir görüntü grubu (batch) olarak döndürülür. Ideogram'ın içerik güvenliği filtresi üretimi engellerse, bunun yerine bir hata oluşturulur. | IMAGE |
| `final_prompt` | Görüntünün gerçekte üretildiği istem (prompt_upsampling çalıştıysa yeniden yazılan yapılandırılmış başlık, aksi takdirde sizin isteminiz). Bu görüntüyü yeniden üretmek için prompt_upsampling OFF ve aynı tohumla geri besleyin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/tr.md)

---
**Source fingerprint (SHA-256):** `7bd20aae508fee111ded32e87119ed6fc01c5ad5ba7d595e24391830a0f20bb7`

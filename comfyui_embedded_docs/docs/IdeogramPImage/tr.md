# Ideogram & Pruna P-Image

Ideogram & Pruna P-Image, Ideogram'ın güçlü tipografisi ve fotogerçekçiliğiyle bilinen hızlı metinden görüntüye modelini kullanarak bir metin isteminden görüntüler oluşturur. Ayrıca metin dizeleri, renkler ve düzen üzerinde tam kontrol için Ideogram 4.0 yapılandırılmış JSON açıklamalarını destekler. Düğüm, oluşturulan görüntü(ler)i ve görüntünün gerçekte üretildiği son istemi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Metin istemi. Ayrıca bir Ideogram 4.0 yapılandırılmış JSON açıklamasını kabul eder (#RRGGBB hex biçiminde tam renkler, tam metin dizeleri, sınırlayıcı kutu düzeni) — olduğu gibi kullanmak için prompt_upsampling'i OFF olarak ayarlayın. Boş olmamalıdır. (varsayılan: "") | STRING | Evet | Boş olmayan herhangi bir metin |
| `quality` | Hız/fiyat/kalite kademesi. MEDIUM günlük varsayılandır; karmaşık istemler, ince ayrıntı ve zor metinler için HIGH; ölçekli taslaklar için VERY_LOW/LOW. Zor metinler MEDIUM'un altında kötü oluşturulur. (varsayılan: "MEDIUM") | COMBO | Evet | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Çıktı boyutu sınıfı (tam pikseller en-boy oranını izler; örn. 16:9, 1K'da 1280x720 ve 2K'da 2560x1440 verir). Keskin tipografi için HIGH + 2K tercih edin. (varsayılan: "1K") | COMBO | Evet | "1K"<br>"2K" |
| `aspect_ratio` | Görüntü oluşturma için en-boy oranı. (varsayılan: "1:1") | COMBO | Evet | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Kısa istemleri oluşturmadan önce ayrıntılı bir yapılandırılmış açıklamaya genişletir (yeniden yazılan istem final_prompt olarak döndürülür). Kendi JSON açıklamanızı veya tam ifadenizi sağlarken OFF olarak ayarlayın. (varsayılan: "AUTO") | COMBO | Evet | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Tekrarlanabilir oluşturma için seed. prompt_upsampling OFF iken, aynı seed ve ayarlar aynı görüntüyü döndürür; ON/AUTO iken istem yeniden yazımı her çalıştırmada değişir — bir sonucu yeniden üretmek için final_prompt çıktısını prompt_upsampling OFF ve aynı seed ile yeniden kullanın. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |

**Kısıtlamalarla ilgili not:** İstem en az bir boşluk olmayan karakter içermelidir, aksi takdirde düğüm başarısız olur. Kendi yapılandırılmış JSON açıklamanızı veya tam ifadenizi sağlarken `prompt_upsampling` öğesini OFF olarak ayarlayın. `prompt_upsampling` ON veya AUTO olduğunda, istem oluşturmadan önce yeniden yazılır, bu nedenle aynı seed aynı görüntüyü yeniden üretmeyebilir; bir görüntüyü yeniden üretmek için, `prompt_upsampling` OFF ve aynı seed ile `final_prompt` çıktısını yeniden kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Oluşturulan görüntü(ler), bir görüntü grubu olarak döndürülür. Ideogram'ın içerik güvenliği filtresi oluşturmayı engellerse, bunun yerine bir hata meydana gelir. | IMAGE |
| `final_prompt` | Görüntünün gerçekte üretildiği istem (prompt_upsampling çalıştıysa yeniden yazılan yapılandırılmış açıklama, aksi halde sizin isteminiz). Bu görüntüyü yeniden üretmek için bunu prompt_upsampling OFF ve aynı seed ile geri besleyin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/tr.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`

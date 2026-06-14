# Runway Aleph2 Video’dan Video’ya Düğümü

Bu düğüm, Runway’in Aleph2 modelini kullanarak bir metin istemiyle videoyu düzenler. Orijinal hareketi ve zamanlamayı korurken, görüntülerinizi yeniden stilize ederek, yeniden aydınlatarak, öğeler ekleyerek veya çıkararak ya da bakış açısını değiştirerek dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Çıktıda ne görünmesi gerektiğini açıklar (1-1000 karakter). | STRING | Evet | 1-1000 karakter |
| `video` | Düzenlenecek giriş videosu. 30 fps veya daha düşük olmak üzere 2-30 saniye olmalıdır. | VIDEO | Evet | 2-30 saniye süre, maks. 30 fps |
| `seed` | Üretim için rastgele tohum (varsayılan: 0). | INT | Evet | 0 ile 4294967295 arası |
| `public_figure_threshold` | Tanınabilir kamu figürleri için içerik denetimi (varsayılan: "düşük"). | COMBO | Evet | "auto"<br>"low" |
| `keyframes` | Aleph2 Ana Kare düğümlerinden gelen, giriş videosuna bağlı kılavuz görüntüler (en fazla 5). Ana kare veya istem görselleri kullanın, ikisini birden kullanmayın. | KEYFRAME | Hayır | En fazla 5 öğe |
| `prompt_images` | Aleph2 İstem Görseli düğümlerinden gelen, çıkış videosuna bağlı kılavuz görüntüler (en fazla 5). Ana kare veya istem görselleri kullanın, ikisini birden kullanmayın. | PROMPT_IMAGE | Hayır | En fazla 5 öğe |

**Önemli kısıtlamalar:**
- Giriş videosu 2 ila 30 saniye arasında olmalı ve kare hızı 30 fps veya daha düşük olmalıdır.
- Kılavuz için `keyframes` veya `prompt_images` kullanabilirsiniz, ancak ikisini aynı anda kullanamazsınız.
- Her kılavuz girişi (ana kareler veya istem görselleri) en fazla 5 öğeyi destekler.
- Ana kare zaman damgaları ve istem görseli zaman damgaları, giriş videosu süresini aşmamalıdır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | Aleph2 modeli tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`

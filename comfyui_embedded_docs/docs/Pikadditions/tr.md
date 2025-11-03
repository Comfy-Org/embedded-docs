> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/tr.md)

Pikadditions düğümü, videonuza herhangi bir nesne veya görüntü eklemenize olanak tanır. Bir video yüklersiniz ve kusursuz bir şekilde entegre edilmiş bir sonuç oluşturmak için ne eklemek istediğinizi belirtirsiniz. Bu düğüm, görüntüleri videolara doğal görünümlü bir entegrasyonla eklemek için Pika API'sini kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Üzerine görüntü eklenecek video. |
| `görüntü` | IMAGE | Evet | - | Videoya eklenecek görüntü. |
| `istem_metni` | STRING | Evet | - | Videoya ne ekleneceğine dair metin açıklaması. |
| `negatif_istem` | STRING | Evet | - | Videoda nelerden kaçınılacağına dair metin açıklaması. |
| `tohum` | INT | Evet | 0 - 4294967295 | Tekrarlanabilir sonuçlar için rastgele tohum değeri. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Görüntü eklenmiş işlenmiş video. |
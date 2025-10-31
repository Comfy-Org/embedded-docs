> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/tr.md)

Pika Swaps düğümü, videonuzdaki nesneleri veya bölgeleri yeni görüntülerle değiştirmenize olanak tanır. Değiştirilecek alanları bir maske veya koordinatlar kullanarak tanımlayabilirsiniz ve düğüm, belirtilen içeriği video dizisi boyunca sorunsuz bir şekilde değiştirecektir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | İçindeki bir nesnenin değiştirileceği video. |
| `görüntü` | IMAGE | Evet | - | Videodaki maskelenmiş nesneyi değiştirmek için kullanılan görüntü. |
| `maske` | MASK | Evet | - | Videoda değiştirilecek alanları tanımlamak için maskeyi kullanın. |
| `istem_metni` | STRING | Evet | - | İstenen değişikliği tanımlayan metin istemi. |
| `negatif_istem` | STRING | Evet | - | Değişiklikte nelerden kaçınılması gerektiğini tanımlayan metin istemi. |
| `tohum` | INT | Evet | 0 - 4294967295 | Tutarlı sonuçlar için rastgele tohum değeri. |

**Not:** Bu düğüm, tüm giriş parametrelerinin sağlanmasını gerektirir. `video`, `image` ve `mask` birlikte çalışarak değiştirme işlemini tanımlar; burada maske, videonun hangi alanlarının sağlanan görüntü ile değiştirileceğini belirtir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Belirtilen nesnenin veya bölgenin değiştirildiği işlenmiş video. |
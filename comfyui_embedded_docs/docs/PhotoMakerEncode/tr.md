> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/tr.md)

PhotoMakerEncode düğümü, AI görüntü oluşturma için koşullandırma verileri üretmek amacıyla görüntüleri ve metni işler. Bir referans görüntü ve metin istemi alır, ardından referans görüntünün görsel özelliklerine dayalı olarak görüntü oluşturmayı yönlendirmek için kullanılabilecek gömme vektörlerini (embedding) oluşturur. Düğüm, görüntü tabanlı koşullandırmanın nereye uygulanacağını belirlemek için özellikle metin içindeki "photomaker" belirteçini (token) arar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `photomaker` | PHOTOMAKER | Evet | - | Görüntüyü işlemek ve gömme vektörleri oluşturmak için kullanılan PhotoMaker modeli |
| `image` | IMAGE | Evet | - | Koşullandırma için görsel özellikler sağlayan referans görüntü |
| `clip` | CLIP | Evet | - | Metin belirteçleme (tokenization) ve kodlama için kullanılan CLIP modeli |
| `text` | STRING | Evet | - | Koşullandırma üretimi için metin istemi (varsayılan: "photomaker fotoğrafı") |

**Not:** Metin içinde "photomaker" kelimesi geçtiğinde, düğüm istemdeki o konuma görüntü tabanlı koşullandırma uygular. Eğer "photomaker" metin içinde bulunamazsa, düğüm görüntü etkisi olmadan standart metin koşullandırması üretir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Görüntü oluşturmayı yönlendirmek için görüntü ve metin gömme vektörlerini içeren koşullandırma verisi |
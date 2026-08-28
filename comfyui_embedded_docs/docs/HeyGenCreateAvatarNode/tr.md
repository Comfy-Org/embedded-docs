# HeyGen Avatar Oluştur

Yeniden kullanılabilir bir HeyGen avatarı, bir kişinin fotoğrafından veya bir karakteri tanımlayan metin isteminden oluşturun. Üretilen `avatar_id`, HeyGen Avatar Video düğümüyle kullanılabilir ve gelecekteki iş akışlarında avatarı yeniden kullanmak üzere kaydedilmelidir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kaynak` | Bir metin isteminden yeni bir karakter oluşturun veya avatarı bağlı bir kişi fotoğrafından oluşturun. | DYNAMIC_COMBO | Evet | `"prompt"`<br>`"photo"` |

### Prompt Girdileri

`source` değeri `"prompt"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak avatarın açıklaması (en fazla 1000 karakter). En az 1 boşluk olmayan karakter içermelidir. Varsayılan: boş dize. | STRING | Evet | 1 ile 1000 characters |

### Fotoğraf Girdileri

`source` değeri `"photo"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Avatar'a dönüştürülecek kişinin fotoğrafı. 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Evet | Single image |

### Referans Girdileri

`source` değeri `"prompt"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Büyütülebilir yuva: oluşturulan görünümü yönlendirmek için en fazla 3 görsel bağlayın (`ref_image_1`...`ref_image_3`). Görseller 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Hayır | 0 ile 3 images |

**Not:** `source` parametresi birbirini dışlayan iki mod arasında geçiş yapar. `"prompt"` modunda `prompt` zorunludur ve isteğe bağlı olarak en fazla 3 referans görseli bağlanabilir. `"photo"` modunda `identity_photo` zorunludur. Fotoğraflar ve referans görseller 2K'dan büyük olduğunda otomatik olarak küçültülür; 3'ten fazla referans görsel kabul edilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `avatar_id` | Avatar görünüm kimliği. HeyGen Avatar Video'nun `custom_avatar_id` parametresine iletin; avatarı daha sonra yeniden kullanmak için kaydedin. | STRING |
| `önizleme` | Oluşturulan avatarın önizleme görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`

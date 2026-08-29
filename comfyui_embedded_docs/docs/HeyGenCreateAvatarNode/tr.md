# HeyGen Avatar Oluştur

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kaynak` | Bir metin isteminden yeni bir karakter oluşturun veya bağlı bir kişi fotoğrafından avatar oluşturun. | DYNAMIC_COMBO | Evet | `"prompt"`<br>`"photo"` |

### Prompt Girdileri

`source` `"prompt"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak avatarın açıklaması (en fazla 1000 karakter). En az 1 boşluk olmayan karakter içermelidir. Varsayılan: boş dize. | STRING | Evet | 1 ile 1000 arası characters |

### Fotoğraf Girdileri

`source` `"photo"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Avatara dönüştürülecek kişinin fotoğrafı. 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Evet | Single image |

### Referans Girdileri

`source` `"prompt"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: oluşturulan görünümü yönlendirmek için en fazla 3 görsel bağlayın (`ref_image_1`...`ref_image_3`). Görseller 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Hayır | 0 ile 3 arası images |

**Not:** `source` parametresi birbirini dışlayan iki mod arasında geçiş yapar. `"prompt"` modunda `prompt` gereklidir ve isteğe bağlı olarak en fazla 3 referans görseli bağlanabilir. `"photo"` modunda `identity_photo` gereklidir. Fotoğraflar ve referans görselleri 2K'dan büyükse otomatik olarak küçültülür; 3'ten fazla referans görseli kabul edilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `avatar_id` | Avatar görünüm kimliği. Bunu HeyGen Avatar Video'nun `custom_avatar_id` parametresine iletin; daha sonra avatarı yeniden kullanmak için kaydedin. | STRING |
| `önizleme` | Oluşturulan avatarın önizleme görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`

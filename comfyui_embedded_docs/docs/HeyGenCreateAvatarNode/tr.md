# HeyGenCreateAvatarNode

Bir kişinin fotoğrafından veya bir karakteri tanımlayan metin isteminden yeniden kullanılabilir bir HeyGen avatarı oluşturun. Ortaya çıkan avatar kimliği, bu avatarı kullanarak videolar oluşturmak için HeyGen Avatar Video düğümüyle kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source` | Bir metin isteminden yeni bir karakter oluşturun veya bağlı bir kişi fotoğrafından avatar oluşturun. | COMBO | Evet | `"prompt"`<br>`"photo"` |

`source` parametresi `"prompt"` olarak ayarlandığında aşağıdaki ek parametreler kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak avatarın açıklaması (en fazla 1000 karakter). | STRING | Evet | 1 ila 1000 karakter |
| `reference_images` | Oluşturulacak görünüme yön veren en fazla 3 referans görseli. | IMAGE | Hayır | 0 ila 3 görsel |

`source` parametresi `"photo"` olarak ayarlandığında aşağıdaki ek parametre kullanılabilir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Avatara dönüştürülecek kişinin fotoğrafı. 2K'dan büyükse otomatik olarak küçültülür. | IMAGE | Evet | Tek görsel |

**Not:** `source` parametresi iki mod arasında geçiş yapar. `"prompt"` modunda, bir metin açıklaması ve isteğe bağlı olarak en fazla 3 referans görseli sağlarsınız. `"photo"` modunda, bir kişinin tek bir fotoğrafını sağlarsınız. Bu modlar birbirini dışlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `avatar_id` | Avatar görünüm kimliği. Bunu HeyGen Avatar Video'nun `custom_avatar_id` parametresine iletin; avatarı daha sonra yeniden kullanmak için kaydedin. | STRING |
| `preview` | Oluşturulan avatarın önizleme görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`

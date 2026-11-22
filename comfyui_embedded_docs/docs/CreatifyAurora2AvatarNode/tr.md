# Creatify Aurora 2.0 Avatar

Creatify Aurora 2.0 Avatar, tek bir fotoğraf ile bir konuşma veya şarkı klibini konuşan veya şarkı söyleyen videoya dönüştürür. Video, bağlanan ses kadar uzundur ve bu sesi değiştirmeden korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|----------|-------|
| `image` | Canlandırılacak kişinin fotoğrafı. Her iki kenar en az 256 piksel ve en-boy oranı 1:4 ile 4:1 arasında olmalıdır; video, fotoğrafın en-boy oranını korur. | IMAGE | Evet | - |
| `audio` | Ağzı ve videonun uzunluğunu yönlendiren konuşma veya şarkı. En fazla 60 saniye veya `"2k"` çözünürlüğünde 14 saniye; başlatılan her saniye için ücretlendirilir. | AUDIO | Evet | En fazla 60 saniye |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"2k"` |
| `text_prompt` | Çekim için sahne, kamera, ışık, ifade veya hareket. Boş bırakıldığında fotoğraf olduğu gibi kalır (varsayılan: boş dize). | STRING | Evet | Herhangi bir metin |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder. Sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:** Bir kenarı 256 pikselden küçük olan veya en-boy oranı 1:4 ile 4:1 aralığının dışında olan bir fotoğraf hata verir. Seçilen çözünürlük için sınırı aşan ses reddedilir: normalde 60 saniye ve `"2k"` çözünürlüğünde 14 saniye.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Bağlanan sesle birlikte konuşan veya şarkı söyleyen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyAurora2AvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `29c83246ebed4bc7a9f3daf3612cd6f34bf2d5a2f1fde7612614a2da6a5010be`

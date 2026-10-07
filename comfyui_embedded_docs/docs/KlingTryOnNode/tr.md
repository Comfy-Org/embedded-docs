# Kling Virtual Try-On

Kling'in sanal prova özelliğiyle bir kişiyi bir giysiyle giydirin. Bir kişinin fotoğrafını ve giysinin fotoğrafını bağlayın; düğüm, o kişinin giysiyi giydiği yeni bir görüntü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Tek bir kişinin fotoğrafı; ideal olarak önden veya üç çeyrek görünümlü olmalıdır. Bir kenarı 2048 pikseli aşan görüntüler önce küçültülür. | IMAGE | Evet | N/A |
| `garment_image` | Giydirilecek giysi: ürün fotoğrafı, düz serim, manken veya model üzerinde fotoğraf. Model üzerinde bir fotoğraf, o kıyafet kombinasyonunun geri kalanını da aktarabilir. Yalnızca giysi; ayakkabı, çanta ve aksesuarlar desteklenmez. | IMAGE | Evet | N/A |
| `keep_pose` | Pozun daha iyi bir kıyafet sunumu için değişmesine izin vermek istiyorsanız kapatın. Gelişmiş parametre (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` ne olursa olsun deterministik değildir. Bu parametre "control after generate" işlevine sahiptir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Not:** Sonuç, `person_image` ile aynı boyuttadır ve en uzun kenarı 2048 piksel ile sınırlandırılır. Her iki girdi de Kling'in API'sine yüklenir; bu biraz zaman alabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Giysiyi giyen kişi. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/tr.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`

# Flux Video Düzenleme

Mevcut bir video klibini yazılı bir yönergeyle düzenler. Nesneleri kaldırabilir, ekleyebilir veya değiştirebilir; ortamı değiştirebilir, görüntüyü yeniden biçimlendirebilir, ekran metnini değiştirebilir veya konuşulan diyaloğu değiştirebilirsiniz. Uzunluk, kadraj, kamera hareketi ve ses kaynak klipten gelir; bu nedenle istemde belirtmediğiniz her şey olduğu gibi kalacak şekilde tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | 0,7 ile 15 saniye arasında, en az 160x160 piksel kaynak klip. Çıktı 24 fps'te oluşturulur ve kare başına yaklaşık 0,9 megapiksel ile sınırlandırılır; bu nedenle daha büyük bir kaynak daha küçük olarak geri döner. | VIDEO | Evet | 0,7 - 15 saniye; minimum 160x160 piksel |
| `prompt` | Değiştirilecek şeyler, sade bir dille, en fazla 4096 karakter. Belirtmediğiniz her şey olduğu gibi kalacak şekilde tasarlanmıştır. Yerine konulan diyalog, orijinal konuşmanın sürdüğü süreye sığmalıdır ve sessiz bir klip sessiz kalır. Varsayılan: boş dize. | STRING | Evet | 1 - 4096 karakter |
| `auto_downscale` | Yükleme öncesinde alan olarak 1280x704 pikselden büyük kaynakları otomatik olarak küçültür. En-boy oranı korunur; daha küçük videolara dokunulmaz. Varsayılan: true. | BOOLEAN | Hayır | true<br>false |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. Varsayılan: 4. | INT | Hayır | 0 - 4 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirlemek için tohum; FLUX kendi tohumunu seçer, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 - 4294967295 |

**Not:** `prompt` en az 1, en fazla 4096 karakter içermelidir. Kaynak `video` 0,7 ile 15 saniye arasında uzunlukta ve en az 160x160 piksel olmalıdır; bu sınırların dışında kalan yüklemeler istek gönderilmeden önce reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | FLUX hizmeti tarafından döndürülen düzenlenmiş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`

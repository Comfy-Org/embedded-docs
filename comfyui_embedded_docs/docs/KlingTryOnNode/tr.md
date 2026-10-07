# Kling Virtual Try-On

Kling'in sanal kıyafet denemesiyle bir kişiye bir kıyafet parçası giydirin. Bir kişi fotoğrafı ile bir giysi fotoğrafını bağlayın; düğüm, o kişinin söz konusu parçayı giydiği yeni bir görsel döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Bir kişinin fotoğrafı, ideal olarak önden veya üç çeyrek görünüm. En az 300x300 piksel olmalıdır; bir kenarı 2048 pikselden büyük olan görseller önce küçültülür. | IMAGE | Evet | N/A |
| `garment_image` | Giydirilecek kıyafet: ürün fotoğrafı, düz serim, manken veya model üzerinde fotoğraf. Model üzerinde bir fotoğraf, o kombinin geri kalanını da taşıyabilir. En az 300x300 piksel olmalıdır. Yalnızca kıyafet; ayakkabı, çanta ve aksesuarlar desteklenmez. | IMAGE | Evet | N/A |
| `keep_pose` | Daha iyi bir kıyafet sunumu için pozun değişmesine izin vermek üzere kapatın. Gelişmiş parametre (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Bu parametre "üretim sonrası kontrol" işlevine sahiptir (varsayılan: 42). | INT | Evet | 0 - 2147483647 |

**Not:** Sonuç, `person_image` ile aynı boyuttadır ve en uzun kenarda 2048 piksel ile sınırlandırılır. Her iki girdi de Kling'in API'sine yüklenir; bu biraz zaman alabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Kıyafet parçasını giyen kişi. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/tr.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`

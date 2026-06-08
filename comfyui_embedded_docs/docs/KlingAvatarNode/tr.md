Kling Avatar 2.0 düğümü, tek bir referans fotoğrafı ve bir ses dosyası kullanarak yayın kalitesinde dijital insan videoları oluşturur. Avatarın hareketlerini, duygularını ve kamera hareketlerini tanımlamak için isteğe bağlı bir metin istemi ile konuşan bir avatar videosu üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Avatar referans görseli. Genişlik ve yükseklik en az 300 piksel olmalıdır. En-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | - |
| `sound_file` | Ses girişi. Süresi 2 ila 300 saniye arasında olmalıdır. | AUDIO | Evet | - |
| `mode` | Kullanılacak üretim modu. | COMBO | Evet | `"std"`<br>`"pro"` |
| `prompt` | Avatar hareketlerini, duygularını ve kamera hareketlerini tanımlamak için isteğe bağlı istem. (varsayılan: boş dize) | STRING | Hayır | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

**Not:** `image` ve `sound_file` girişlerinin belirli doğrulama gereksinimleri vardır. Görsel, en az 300x300 piksel boyutunda ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. Ses dosyası 2 ila 300 saniye uzunluğunda olmalıdır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan dijital insan videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`

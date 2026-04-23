> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/tr.md)

Kling Avatar 2.0 düğümü, yayın kalitesinde dijital insan videoları oluşturur. Tek bir referans fotoğrafı ve bir ses dosyası kullanarak konuşan bir avatar videosu oluşturur. Avatarın eylemlerini, duygularını ve kamera hareketlerini tanımlamak için isteğe bağlı bir metin istemi kullanılabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Avatar referans görseli. Genişlik ve yükseklik en az 300 piksel olmalıdır. En-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `sound_file` | AUDIO | Evet | - | Ses girişi. Süresi 2 ila 300 saniye arasında olmalıdır. |
| `mode` | COMBO | Evet | `"std"`<br>`"pro"` | Kullanılacak oluşturma modu. |
| `prompt` | STRING | Hayır | - | Avatar eylemlerini, duygularını ve kamera hareketlerini tanımlamak için isteğe bağlı istem. (varsayılan: boş dize) |
| `seed` | INT | Evet | 0 - 2147483647 | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) |

**Not:** `image` ve `sound_file` girişlerinin belirli doğrulama gereksinimleri vardır. Görsel, en az 300x300 piksel boyutunda ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. Ses dosyası 2 ila 300 saniye uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan dijital insan videosu. |
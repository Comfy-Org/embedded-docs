# Comfy Cloud MiniMax H3 İlk-Son Kareden Videoya [BETA]

MiniMax H3 ilk-son kare iş akışını bir Comfy Cloud GPU üzerinde çalıştırır ve iki anahtar kare arasındaki hareketi eşleşen bir ses parçasıyla birlikte döndürür. Açılış ve kapanış karelerini verin; model aralarındaki çekimi doldurur. Son kare isteğe bağlıdır: onu dışarıda bırakırsanız hareket bunun yerine ilk kareden uzağa doğru ilerler. Bu bir beta düğümdür ve GPU saniyesi başına ücretlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı görüntü. İş akışı çalıştırılmadan önce 2048x2048 piksele kadar yüklenir. | IMAGE | Evet | - |
| `last_frame` | İsteğe bağlı kapanış karesi. Bağlandığında, oluşturulan hareket bu görüntüde sona erer; bağlanmadığında hareket `first_frame`'den uzağa doğru ilerler. | IMAGE | Hayır | - |
| `prompt` | Hareketin ve çekimin taşıması gereken seslerin metin açıklaması. Gönderimden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 - 4096 karakter |
| `seed` | Oluşturulan sonucu kontrol eden rastgele tohum (varsayılan: 42). | INT | Evet | 0 - 18446744073709551615 |
| `aspect_ratio` | Oluşturulan videonun en-boy oranı (varsayılan: `"1:1"`). | COMBO | Evet | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Kare boyutu bütçesi (varsayılan: `"480p"`). 720p, yaklaşık olarak 480p'nin iki katı GPU saniyesine mal olur. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `duration_seconds` | Saniye cinsinden uzunluk (varsayılan: 5). İşlem hattı 24 fps'te 17 karelik adımlara nicemleme yapar; bu nedenle klip, bu değerin yaklaşık üçte iki saniyesi içinde kalır. | INT | Evet | 5 - 15 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Ses parçasıyla birlikte oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3FirstLastFrameToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `5b9d1a2155951fb953e94726f0c6ca7720a805ab5d3015adaa5cc496acaa0de3`

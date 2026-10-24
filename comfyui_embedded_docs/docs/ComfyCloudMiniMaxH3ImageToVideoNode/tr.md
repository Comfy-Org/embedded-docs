# Comfy Cloud MiniMax H3 Görüntüden Videoya [BETA]

MiniMax H3 görüntüden videoya iş akışını bir Comfy Cloud GPU üzerinde çalıştırır ve eşleşen bir ses parçasıyla birlikte video döndürür. Hareketsiz görsel ilk kare olur. Bir klibin kapanış karesini yeniden beslemek diziyi sürdürür; böylece birkaç çalıştırmayı zincirlemek daha uzun bir çekim oluşturur. Bu bir beta düğümdür ve GPU saniyesi başına faturalandırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Videonun başladığı görsel. İş akışı çalıştırılmadan önce en fazla 2048x2048 piksel olacak şekilde yüklenir. | IMAGE | Evet | - |
| `prompt` | Hareketin ve çekimin taşıması gereken seslerin metin açıklaması. Gönderimden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 ila 4096 karakter |
| `seed` | Üretilen sonucu kontrol eden rastgele tohum (varsayılan: 42). | INT | Evet | 0 ila 18446744073709551615 |
| `aspect_ratio` | Üretilen videonun en-boy oranı (varsayılan: `"1:1"`). | COMBO | Evet | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Kare boyutu bütçesi (varsayılan: `"480p"`). 720p, 480p'nin yaklaşık iki katı GPU-saniyesine mal olur. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `duration_seconds` | Saniye cinsinden uzunluk (varsayılan: 5). İşlem hattı, 24 fps'de 17 karelik adımlarla nicemleme yapar; bu nedenle klip, bu değerin yaklaşık saniyenin üçte ikisi kadar yakınında yer alır. | INT | Evet | 5 ila 15 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Ses parçasıyla birlikte üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d3657e266f2b9f789414a106ef66b6c64ec314d27c3b6a99c3a6a9b8584abf61`

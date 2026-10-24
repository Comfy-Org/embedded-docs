# Comfy Cloud MiniMax H3 Metinden Videoya [BETA]

MiniMax H3 metinden videoya iş akışını bir Comfy Cloud GPU üzerinde çalıştırır ve uyumlu bir film müziğiyle birlikte video döndürür. Görüntü ve ses, sonradan dublaj yapılmak yerine aynı geçişte üretilir. Bu bir beta düğümdür ve GPU saniyesi üzerinden ücretlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Videonun metin açıklaması; çekimin taşıması gereken sesler dahil. Gönderimden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 ile 4096 karakter |
| `seed` | Üretilen sonucu kontrol eden rastgele tohum (varsayılan: 42). | INT | Evet | 0 ile 18446744073709551615 |
| `aspect_ratio` | Üretilen videonun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Kare boyutu bütçesi (varsayılan: `"480p"`). 720p, 480p'nin yaklaşık iki katı GPU saniyesine mal olur. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `duration_seconds` | Saniye cinsinden uzunluk (varsayılan: 5). İşlem hattı 24 fps'te 17 karelik adımlara nicemleme yapar, bu nedenle klip bu değerin yaklaşık üçte iki saniyesi içinde kalır. | INT | Evet | 5 ile 15 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Film müziğiyle birlikte üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`

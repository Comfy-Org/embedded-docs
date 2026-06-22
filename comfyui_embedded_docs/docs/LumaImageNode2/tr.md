# Luma UNI-1 Image

Bu belge, Luma UNI-1 modelini kullanarak metin açıklamalarından görseller üretir. Bir metin istemi ve en boy oranı ile stil gibi isteğe bağlı ayarları alır, ardından bir görsel oluşturmak için Luma API'sine istek gönderir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | İstenen görselin metin açıklaması. | STRING | Evet | 1–6000 karakter |
| `model` | Üretim için kullanılacak model. Bir model seçmek, o modele özel ek ayarları ortaya çıkarır. | COMBO | Evet | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar, tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

### Modele Özel Girişler

`model` parametresi için `"uni-1"` veya `"uni-1-max"` seçildiğinde aşağıdaki girişler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Çıktı görselinin en boy oranı. `"auto"`, modelin isteme göre seçim yapmasını sağlar. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Oluşturulan görsel için görsel stil. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"manga"` |
| `web_search` | Modelin ek bağlam için web'de arama yapmasına izin verilip verilmeyeceği. (varsayılan: False) | BOOLEAN | Evet | True / False |
| `image_ref` | Üretimi yönlendirmek için referans görseller. | IMAGE | Hayır | En fazla 9 görsel |

**`style` ve `aspect_ratio` kısıtlamalarına ilişkin not:** `style` `"manga"` olarak ayarlanmışsa, `aspect_ratio` ya `"auto"` olmalı ya da şu portre oranlarından biri olmalıdır: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. `"manga"` stili ile yatay veya kare bir oran kullanmak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Bir tensör olarak oluşturulan görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/tr.md)

---
**Source fingerprint (SHA-256):** `0a71bcd7c68c3610c162601b4c3f700034e47af8f16cf7853606753ad270c96e`

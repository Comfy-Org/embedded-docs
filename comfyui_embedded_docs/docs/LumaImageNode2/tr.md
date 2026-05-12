> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/tr.md)

## Genel Bakış

Bu düğüm, Luma UNI-1 modelini kullanarak metin açıklamalarından görseller oluşturur. Bir metin istemi ve en boy oranı, stil gibi isteğe bağlı ayarları alır, ardından bir görsel oluşturmak için Luma API'sine istek gönderir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | 1–6000 karakter | İstenen görselin metin açıklaması. |
| `model` | COMBO | Evet | `"uni-1"`<br>`"uni-1-max"` | Oluşturma için kullanılacak model. Bir model seçmek, o modele özel ek ayarları görünür hale getirir. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) |

### Modele Özel Girdiler

`model` parametresi için `"uni-1"` veya `"uni-1-max"` seçildiğinde aşağıdaki girdiler kullanılabilir hale gelir:

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | Evet | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` | Çıktı görselinin en boy oranı. `"auto"` seçeneği, modelin isteme göre seçim yapmasını sağlar. (varsayılan: `"auto"`) |
| `style` | COMBO | Evet | `"auto"`<br>`"manga"` | Oluşturulan görsel için görsel stil. (varsayılan: `"auto"`) |
| `web_search` | BOOLEAN | Evet | True / False | Modelin ek bağlam için web'de arama yapmasına izin verilip verilmeyeceği. (varsayılan: False) |
| `image_ref` | IMAGE | Hayır | En fazla 9 görsel | Oluşturmayı yönlendirmek için referans görseller. |

**`style` ve `aspect_ratio` kısıtlamaları hakkında not:** `style` `"manga"` olarak ayarlanırsa, `aspect_ratio` ya `"auto"` olmalı ya da şu portre oranlarından biri olmalıdır: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. `"manga"` stiliyle yatay veya kare oran kullanmak hataya neden olur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `image` | IMAGE | Bir tensör olarak oluşturulan görsel. |
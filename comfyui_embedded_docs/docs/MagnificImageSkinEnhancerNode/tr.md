**Magnific Image Skin Enhancer Düğümü**

Magnific Image Skin Enhancer düğümü, portre görüntülerine özel yapay zeka işleme uygulayarak cilt görünümünü iyileştirir. Farklı iyileştirme hedefleri için üç ayrı mod sunar: sanatsal efektler için yaratıcı, orijinal görünümü korumak için sadık ve aydınlatma veya gerçekçilik gibi hedefli iyileştirmeler için esnek. Düğüm, işleme için görüntüyü harici bir API'ye yükler ve iyileştirilmiş sonucu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | İyileştirilecek portre görüntüsü. | IMAGE | Evet | - |
| `sharpen` | Keskinleştirme yoğunluk seviyesi (varsayılan: 0). | INT | Hayır | 0 ila 100 |
| `smart_grain` | Akıllı gren yoğunluk seviyesi (varsayılan: 2). | INT | Hayır | 0 ila 100 |
| `mode` | Kullanılacak işleme modu. `"creative"` sanatsal iyileştirme, `"faithful"` orijinal görünümü koruma ve `"flexible"` hedefli optimizasyon içindir. | COMBO | Evet | `"creative"`<br>`"faithful"`<br>`"flexible"` |
| `skin_detail` | Cilt detayı iyileştirme seviyesi. Bu girdi yalnızca `mode` `"faithful"` olarak ayarlandığında kullanılabilir ve zorunludur (varsayılan: 80). | INT | Hayır | 0 ila 100 |
| `optimized_for` | İyileştirme optimizasyon hedefi. Bu girdi yalnızca `mode` `"flexible"` olarak ayarlandığında kullanılabilir ve zorunludur. | COMBO | Hayır | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` |

**Kısıtlamalar:**

* Düğüm tam olarak bir giriş görüntüsü kabul eder.
* Giriş görüntüsünün minimum yükseklik ve genişliği 160 piksel olmalıdır.
* Giriş görüntüsünün en-boy oranı 1:3 ile 3:1 arasında olmalıdır (katı olmayan doğrulama).
* `skin_detail` parametresi yalnızca `mode` `"faithful"` olarak ayarlandığında etkindir.
* `optimized_for` parametresi yalnızca `mode` `"flexible"` olarak ayarlandığında etkindir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | İyileştirilmiş portre görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/tr.md)

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`

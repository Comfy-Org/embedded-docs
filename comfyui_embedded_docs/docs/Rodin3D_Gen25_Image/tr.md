## Genel Bakış

Bu düğüm, Rodin Gen-2.5 API'sini kullanarak bir ila beş referans görüntüden 3B model oluşturur. Üretim hızı ve maliyeti dengelemek için Hızlı, Normal veya Aşırı-Yüksek kalite modları arasından seçim yapabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Bir ila beş giriş görüntüsü. Birden fazla görüntü sağlandığında, ilk görüntü malzemeler için kullanılır. | IMAGE | Evet | 1 ila 5 görüntü |
| `mod` | Üretim kalite modu. Daha yüksek kalite modları daha iyi sonuçlar üretir ancak daha maliyetlidir. | COMBO | Evet | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `materyal` | Oluşturulan 3B model için malzeme türü. | COMBO | Evet | `"PBR"`<br>`"Matte"` |
| `geometri_dosya_formatı` | 3B model geometrisi için çıktı dosya biçimi. | COMBO | Evet | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `doku_modu` | Doku oluşturma modu. "Original" giriş dokularını korur, "Clean" bunları kaldırır ve "Style" stilize bir doku uygular. | COMBO | Evet | `"Original"`<br>`"Clean"`<br>`"Style"` |
| `tohum` | Tekrarlanabilir sonuçlar için rastgele tohum değeri. Aynı çıktıyı almak için aynı tohum değerini kullanın. | INT | Evet | 0 ila 2147483647 |
| `TAPose` | Oluşturulan modele T-pozu uygulanıp uygulanmayacağı. | BOOLEAN | Evet | True / False |
| `hd_doku` | Yüksek çözünürlüklü doku haritası oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | True / False |
| `doku_aydınlatma` | Doku oluşturmadan önce giriş görüntülerinden aydınlatmanın kaldırılıp kaldırılmayacağı. | BOOLEAN | Evet | True / False |
| `orijinal_alfa_kullan` | Giriş görüntülerinden orijinal alfa kanalının kullanılıp kullanılmayacağı. | BOOLEAN | Evet | True / False |
| `ek_highpack` | Standart modele ek olarak modelin yüksek çokgenli bir sürümünün oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | True / False |
| `bbox_genişliği` | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden genişliği. | INT | Evet | 1 ila 1000 |
| `bbox_yüksekliği` | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden yüksekliği. | INT | Evet | 1 ila 1000 |
| `bbox_uzunluğu` | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden uzunluğu. | INT | Evet | 1 ila 1000 |
| `yükseklik_cm` | Oluşturulan modelin santimetre cinsinden yüksekliği. | INT | Evet | 1 ila 300 |

**Görüntü Sayısı Hakkında Not:** Düğüm 1 ila 5 görüntü kabul eder. Bir grup görüntü (örneğin, 4 görüntülü bir grup) sağlarsanız, gruptaki her görüntü ayrı bir giriş görüntüsü olarak işlenir. 5'ten fazla görüntü sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_dosyası` | Seçilen geometri biçiminde oluşturulan 3B model dosyası. | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/tr.md)

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`

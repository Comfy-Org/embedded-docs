> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/tr.md)

## Genel Bakış

Bu düğüm, Rodin Gen-2.5 API'sini kullanarak bir ila beş referans görüntüden 3B model oluşturur. Üretim hızı ve maliyeti dengelemek için Hızlı, Normal veya Aşırı-Yüksek kalite modları arasından seçim yapabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | 1 ila 5 görüntü | Bir ila beş giriş görüntüsü. Birden fazla görüntü sağlandığında, ilk görüntü malzemeler için kullanılır. |
| `mode` | COMBO | Evet | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | Üretim kalite modu. Daha yüksek kalite modları daha iyi sonuçlar üretir ancak daha maliyetlidir. |
| `material` | COMBO | Evet | `"PBR"`<br>`"Matte"` | Oluşturulan 3B model için malzeme türü. |
| `geometry_file_format` | COMBO | Evet | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | 3B model geometrisi için çıktı dosya biçimi. |
| `texture_mode` | COMBO | Evet | `"Original"`<br>`"Clean"`<br>`"Style"` | Doku oluşturma modu. "Original" giriş dokularını korur, "Clean" bunları kaldırır ve "Style" stilize bir doku uygular. |
| `seed` | INT | Evet | 0 ila 2147483647 | Tekrarlanabilir sonuçlar için rastgele tohum değeri. Aynı çıktıyı almak için aynı tohum değerini kullanın. |
| `TAPose` | BOOLEAN | Evet | True / False | Oluşturulan modele T-pozu uygulanıp uygulanmayacağı. |
| `hd_texture` | BOOLEAN | Evet | True / False | Yüksek çözünürlüklü doku haritası oluşturulup oluşturulmayacağı. |
| `texture_delight` | BOOLEAN | Evet | True / False | Doku oluşturmadan önce giriş görüntülerinden aydınlatmanın kaldırılıp kaldırılmayacağı. |
| `use_original_alpha` | BOOLEAN | Evet | True / False | Giriş görüntülerinden orijinal alfa kanalının kullanılıp kullanılmayacağı. |
| `addon_highpack` | BOOLEAN | Evet | True / False | Standart modele ek olarak modelin yüksek çokgenli bir sürümünün oluşturulup oluşturulmayacağı. |
| `bbox_width` | INT | Evet | 1 ila 1000 | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden genişliği. |
| `bbox_height` | INT | Evet | 1 ila 1000 | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden yüksekliği. |
| `bbox_length` | INT | Evet | 1 ila 1000 | Oluşturulan model için sınırlayıcı kutunun santimetre cinsinden uzunluğu. |
| `height_cm` | INT | Evet | 1 ila 300 | Oluşturulan modelin santimetre cinsinden yüksekliği. |

**Görüntü Sayısı Hakkında Not:** Düğüm 1 ila 5 görüntü kabul eder. Bir grup görüntü (örneğin, 4 görüntülü bir grup) sağlarsanız, gruptaki her görüntü ayrı bir giriş görüntüsü olarak işlenir. 5'ten fazla görüntü sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | FILE3D | Seçilen geometri biçiminde oluşturulan 3B model dosyası. |

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`

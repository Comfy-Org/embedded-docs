> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/tr.md)

GLSL Shader düğümü, giriş görüntülerine özel GLSL ES fragment shader kodu uygular. Birden fazla görüntüyü işleyebilen ve tek tip parametreler (float, integer, boolean ve eğriler) kabul eden shader programları yazarak karmaşık görsel efektler oluşturmanıza olanak tanır. Çıktı boyutu, ilk giriş görüntüsüne göre belirlenebilir veya manuel olarak ayarlanabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Evet | Yok | GLSL fragment shader kaynak kodu (GLSL ES 3.00 / WebGL 2.0 uyumlu). Varsayılan: İlk giriş görüntüsünü çıktı olarak veren temel bir shader. |
| `size_mode` | COMBO | Evet | `"from_input"`<br>`"custom"` | Çıktı boyutu: 'from_input' ilk giriş görüntüsü boyutlarını kullanır, 'custom' manuel boyutlandırmaya izin verir. |
| `width` | INT | Hayır | 1 ila 16384 | `size_mode` değeri `"custom"` olarak ayarlandığında çıktı görüntüsünün genişliği. Varsayılan: 512. |
| `height` | INT | Hayır | 1 ila 16384 | `size_mode` değeri `"custom"` olarak ayarlandığında çıktı görüntüsünün yüksekliği. Varsayılan: 512. |
| `images` | IMAGE | Evet | 1 ila 8 görüntü | Shader tarafından işlenecek giriş görüntüleri. Görüntülere shader kodunda `u_image0` ile `u_image7` (sampler2D) olarak erişilebilir. |
| `floats` | FLOAT | Hayır | 0 ila 8 float | Shader için kayan noktalı tek tip değerler. Float değerlerine shader kodunda `u_float0` ile `u_float7` olarak erişilebilir. Varsayılan: 0.0. |
| `ints` | INT | Hayır | 0 ila 8 integer | Shader için tamsayı tek tip değerler. Tamsayılara shader kodunda `u_int0` ile `u_int7` olarak erişilebilir. Varsayılan: 0. |
| `bools` | BOOLEAN | Hayır | 0 ila 8 boolean | Shader için boolean tek tip değerler. Boolean değerlerine shader kodunda `u_bool0` ile `u_bool7` (bool) olarak erişilebilir. Varsayılan: Yanlış. |
| `curves` | CURVE | Hayır | 0 ila 8 eğri | Shader için eğri tek tip değerler. Eğrilere shader kodunda `u_curve0` ile `u_curve7` (sampler2D, 1D LUT) olarak erişilebilir. `texture(u_curve0, vec2(x, 0.5)).r` ile örnekleyin. |

**Notlar:**

* `width` ve `height` parametreleri yalnızca `size_mode` değeri `"custom"` olarak ayarlandığında gereklidir ve görünür.
* En az bir giriş görüntüsü gereklidir.
* Shader kodu her zaman çıktı boyutlarını içeren bir `u_resolution` (vec2) tek tip değerine erişebilir.
* En fazla 8 giriş görüntüsü, 8 float tek tip değeri, 8 integer tek tip değeri, 8 boolean tek tip değeri ve 8 eğri tek tip değeri sağlanabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE1` | IMAGE | Shader'dan gelen ilk çıktı görüntüsü. Shader kodunda `layout(location = 0) out vec4 fragColor0` ile kullanılabilir. |
| `IMAGE2` | IMAGE | Shader'dan gelen ikinci çıktı görüntüsü. Shader kodunda `layout(location = 1) out vec4 fragColor1` ile kullanılabilir. |
| `IMAGE3` | IMAGE | Shader'dan gelen üçüncü çıktı görüntüsü. Shader kodunda `layout(location = 2) out vec4 fragColor2` ile kullanılabilir. |
| `IMAGE3` | IMAGE | Shader'dan gelen dördüncü çıktı görüntüsü. Shader kodunda `layout(location = 3) out vec4 fragColor3` ile kullanılabilir. |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`

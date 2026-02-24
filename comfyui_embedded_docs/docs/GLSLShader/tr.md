> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/tr.md)

GLSL Shader düğümü, özel GLSL ES fragment shader kodunu giriş görüntülerine uygular. Birden fazla görüntüyü işleyebilen ve karmaşık görsel efektler oluşturmak için uniform parametreler (float ve integer) kabul edebilen shader programları yazmanıza olanak tanır. Çıktı boyutu, ilk giriş görüntüsü tarafından belirlenebilir veya manuel olarak ayarlanabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Evet | Yok | GLSL fragment shader kaynak kodu (GLSL ES 3.00 / WebGL 2.0 uyumlu). Varsayılan: İlk giriş görüntüsünü çıktılayan temel bir shader. |
| `size_mode` | COMBO | Evet | `"from_input"`<br>`"custom"` | Çıktı boyutu: 'from_input' ilk giriş görüntüsünün boyutlarını kullanır, 'custom' manuel boyut ayarına izin verir. |
| `width` | INT | Hayır | 1 - 16384 | `size_mode` `"custom"` olarak ayarlandığında çıktı görüntüsünün genişliği. Varsayılan: 512. |
| `height` | INT | Hayır | 1 - 16384 | `size_mode` `"custom"` olarak ayarlandığında çıktı görüntüsünün yüksekliği. Varsayılan: 512. |
| `images` | IMAGE | Evet | 1 - 8 görüntü | Shader tarafından işlenecek giriş görüntüleri. Görüntüler, shader kodunda `u_image0` ile `u_image7` (sampler2D) olarak kullanılabilir. |
| `floats` | FLOAT | Hayır | 0 - 8 float | Shader için kayan noktalı uniform değerler. Float değerleri, shader kodunda `u_float0` ile `u_float7` olarak kullanılabilir. Varsayılan: 0.0. |
| `ints` | INT | Hayır | 0 - 8 tamsayı | Shader için tamsayı uniform değerler. Tamsayılar, shader kodunda `u_int0` ile `u_int7` olarak kullanılabilir. Varsayılan: 0. |

**Notlar:**
*   `width` ve `height` parametreleri yalnızca `size_mode` `"custom"` olarak ayarlandığında gerekli ve görünür olur.
*   En az bir giriş görüntüsü gereklidir.
*   Shader kodu her zaman çıktı boyutlarını içeren bir `u_resolution` (vec2) uniform değişkenine erişebilir.
*   Maksimum 8 giriş görüntüsü, 8 float uniform ve 8 tamsayı uniform sağlanabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | Shader'dan ilk çıktı görüntüsü. Shader kodunda `layout(location = 0) out vec4 fragColor0` ile kullanılabilir. |
| `IMAGE1` | IMAGE | Shader'dan ikinci çıktı görüntüsü. Shader kodunda `layout(location = 1) out vec4 fragColor1` ile kullanılabilir. |
| `IMAGE2` | IMAGE | Shader'dan üçüncü çıktı görüntüsü. Shader kodında `layout(location = 2) out vec4 fragColor2` ile kullanılabilir. |
| `IMAGE3` | IMAGE | Shader'dan dördüncü çıktı görüntüsü. Shader kodunda `layout(location = 3) out vec4 fragColor3` ile kullanılabilir. |
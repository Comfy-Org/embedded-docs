# Bria FIBO 2.0 Image Generate

Metin isteminden, yapılandırılmış JSON isteminden veya tek bir referans görüntüden Bria FIBO 2.0 kullanarak yeni bir görüntü oluşturur. Düğüm, isteği Bria API'sine gönderir, oluşturmanın tamamlanmasını bekler ve görüntüyü, daha sonraki bir çalıştırmada yeniden oluşturmak veya iyileştirmek için kullanılabilecek yapılandırılmış bir istemle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntünün düz dilde açıklaması (varsayılan: boş). | STRING | Evet | Çok satırlı metin |
| `structured_prompt` | Önceki bir Bria FIBO sonucundan alınan JSON yapılandırılmış istem. Aynı seed ile o görüntüyü yeniden oluşturur; JSON'u değiştirin veya iyileştirmek için bir istem ekleyin (varsayılan: boş). | STRING | Evet | Çok satırlı metin |
| `aspect_ratio` | Çıktı en-boy oranı (varsayılan: `"1:1"`). `"16:10"` ve sonrasındaki oranlar, aşağıda listelenen ek gereksinimlere sahip FIBO 2.0 boyutlarıdır. | COMBO | Evet | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | Megapiksel cinsinden çıktı çözünürlüğü (varsayılan: `"1MP"`). | COMBO | Evet | `"1MP"`<br>`"4MP"` |
| `seed` | Oluşturmayı başlatan seed değeri (varsayılan: 42). | INT | Evet | 1 - 2147483647 |
| `moderation` | Moderasyon ayarları. `"true"` seçildiğinde aşağıda listelenen moderasyon girdileri ortaya çıkar. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `image` | Üzerine çizim yapılacak isteğe bağlı referans görüntü. Sonuç, seçilen en-boy oranında yeni bir görüntüdür; bu görüntünün düzenlenmiş hali değildir. | IMAGE | Hayır | - |

### Moderasyon Girdileri

`moderation` değeri `"true"` olarak ayarlandığında, bu ek girdiler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | İstem metninin moderasyona tabi tutulup tutulmayacağı; moderasyon reddettiğinde istek başarısız olur (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_input_moderation` | Referans görüntünün moderasyona tabi tutulup tutulmayacağı; moderasyon reddettiğinde istek başarısız olur (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_output_moderation` | Oluşturulan görüntünün moderasyona tabi tutulup tutulmayacağı; moderasyon reddettiğinde istek başarısız olur (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |

**Önemli Kısıtlamalar:**

- `prompt`, `structured_prompt` veya bir referans `image` değerlerinden en az birini sağlayın. Üçü de boşsa düğüm bir hata verir.
- Bir referans görüntü `structured_prompt` ile birleştirilemez: birini veya diğerini kullanın.
- FIBO 2.0 oranları (`"16:10"`, `"10:16"`, `"2:1"`, `"1:2"`, `"21:9"`, `"9:21"`, `"3:1"`, `"1:3"`, `"4:1"`, `"1:4"`, `"5:1"`, `"1:5"`) `resolution` değerinin `"1MP"` olmasını ve `prompt` veya `structured_prompt` değerlerinden tam olarak birinin sağlanmasını gerektirir.
- Bu düğüm ücretli bir API düğümüdür; ComfyUI her çalıştırma için yaklaşık 0.0572 USD ücret alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria API'si tarafından döndürülen oluşturulmuş görüntü. | IMAGE |
| `structured_prompt` | Oluşturulan görüntünün, bu düğümle yeniden oluşturmak veya iyileştirmek için yapılandırılmış açıklaması. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/tr.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`

# OpenAIDalle2

OpenAI'nin DALL·E 2 uç noktası aracılığıyla senkron olarak görseller oluşturur. Düğüm, bir metin istemini OpenAI'nin DALL·E 2 API'sine gönderir ve elde edilen görsel(leri) ComfyUI'ye döndürür. Ayrıca hem bir `image` hem de bir `mask` birlikte sağlandığında mevcut bir görseli düzenleyebilir.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görseller oluşturmak için OpenAI'nin DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda düğüm bunu OpenAI'nin sunucularına gönderir; sunucular karşılık gelen görselleri oluşturur ve ComfyUI'ye döndürür. Düğüm iki modda çalışabilir: yalnızca bir metin istemi kullanan standart görsel oluşturma veya hem bir görsel hem de maske sağlandığında görsel düzenleme modu. Düzenleme modunda, orijinal görselin hangi bölümlerinin değiştirilmesi gerektiğini belirlemek için maskeyi kullanır ve diğer alanları değiştirmeden bırakır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | DALL·E için metin istemi (varsayılan: boş) | STRING | Evet | - |
| `seed` | arka uçta henüz uygulanmadı (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `size` | Görsel boyutu (varsayılan: "1024x1024") | COMBO | Hayır | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Kaç görsel oluşturulacağı (varsayılan: 1) | INT | Hayır | 1 ile 8 |
| `image` | Görsel düzenleme için isteğe bağlı referans görseli. | IMAGE | Hayır | - |
| `mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilecektir) | MASK | Hayır | - |

**Not:** Görsel düzenleme modu yalnızca `image` ve `mask` birlikte sağlandığında etkinleştirilir. Bunlardan yalnızca biri sağlanırsa hata verilir. `mask`, `image` ile aynı boyutta olmalıdır; aksi halde hata verilir. Düzenleme modunda, maskenin beyaz alanları değiştirilecek bölgeleri belirtir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | DALL·E 2'den oluşturulan veya düzenlenen görsel(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

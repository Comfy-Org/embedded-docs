# OpenAI DALL·E 2

Generates images synchronously via OpenAI's DALL·E 2 endpoint.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görüntüler oluşturmak için OpenAI'ın DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda, düğüm bunu OpenAI sunucularına gönderir; sunucular ilgili görüntüleri üretir ve ComfyUI'ye geri döndürür. Düğüm iki modda çalışabilir: yalnızca metin istemi kullanan standart görüntü üretimi veya hem bir görüntü hem de maske sağlandığında görüntü düzenleme modu. Düzenleme modunda, orijinal görüntünün hangi bölümlerinin değiştirileceğini belirlemek için maskeyi kullanır; diğer alanlar ise değişmeden kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | DALL·E için metin istemi (varsayılan: boş) | STRING | Evet | - |
| `tohum` | Arka uçta henüz uygulanmadı (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |
| `boyut` | Görüntü boyutu (varsayılan: "1024x1024") | COMBO | Hayır | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1) | INT | Hayır | 1 ila 8 |
| `görüntü` | Görüntü düzenleme için isteğe bağlı referans görüntüsü. | IMAGE | Hayır | - |
| `maske` | İnpainting için isteğe bağlı maske (beyaz alanlar değiştirilir) | MASK | Hayır | - |

**Not:** Görüntü düzenleme modu yalnızca hem `image` hem de `mask` birlikte sağlandığında etkinleştirilir. Yalnızca biri sağlandığında hata oluşur. `mask`, `image` ile aynı boyutta olmalıdır; aksi halde hata oluşur. Düzenleme modunda, maskenin beyaz alanları değiştirilecek bölgeleri belirtir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | DALL·E 2 tarafından üretilen veya düzenlenen görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

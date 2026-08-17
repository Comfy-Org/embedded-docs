# OpenAI DALL·E 2

OpenAI DALL·E 2, OpenAI'nin DALL·E 2 uç noktası aracılığıyla eşzamanlı olarak görseller üretir. Yeni görseller oluşturmak için bir metin istemi sağlayın veya mevcut bir görseli düzenlemek için hem bir görsel hem de bir maske sağlayın.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görseller oluşturmak için OpenAI'nin DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda, düğüm bunu OpenAI'nin sunucularına gönderir; sunucular ilgili görselleri üretir ve ComfyUI'ye geri döndürür. Düğüm iki modda çalışabilir: yalnızca bir metin istemi kullanan standart görsel üretimi veya hem bir görsel hem de bir maske sağlandığında görsel düzenleme modu. Düzenleme modunda, orijinal görselin diğer alanlarını değiştirmeden korurken hangi bölümlerinin değiştirileceğini belirlemek için maskeyi kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | DALL·E için metin istemi (varsayılan: boş) | STRING | Evet | - |
| `seed` | backend'de henüz uygulanmadı (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `size` | Görsel boyutu (varsayılan: "1024x1024") | COMBO | Hayır | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Oluşturulacak görsel sayısı (varsayılan: 1) | INT | Hayır | 1 ile 8 |
| `image` | Görsel düzenleme için isteğe bağlı referans görseli. | IMAGE | Hayır | - |
| `mask` | İnpainting için isteğe bağlı maske (beyaz alanlar değiştirilecektir) | MASK | Hayır | - |

Not: `image` ve `mask` birlikte sağlanmalıdır. Her ikisi de sağlandığında, düğüm görsel düzenleme moduna geçer. Yalnızca biri sağlanırsa, bir hata oluşur. `mask`, `image` ile aynı boyutta olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | DALL·E 2'den üretilen veya düzenlenen görsel(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

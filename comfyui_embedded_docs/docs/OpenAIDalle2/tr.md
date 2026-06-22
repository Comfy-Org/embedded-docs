# OpenAI DALL·E 2

OpenAI'nin DALL·E 2 uç noktası aracılığıyla eşzamanlı olarak görseller oluşturur.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görseller oluşturmak için OpenAI'nin DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda, düğüm bunu OpenAI sunucularına gönderir; sunucular karşılık gelen görselleri oluşturur ve ComfyUI'ye geri döndürür. Düğüm iki modda çalışabilir: yalnızca metin istemi kullanarak standart görsel oluşturma veya hem görsel hem de maske sağlandığında görsel düzenleme modu. Düzenleme modunda, orijinal görselin hangi bölümlerinin değiştirileceğini belirlemek için maskeyi kullanırken diğer alanları değiştirmeden bırakır.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `istem` | DALL·E için metin istemi | STRING | zorunlu | "" | - |
| `tohum` | arka uçta henüz uygulanmadı | INT | isteğe bağlı | 0 | 0 ile 2147483647 arası |
| `boyut` | Görsel boyutu | COMBO | isteğe bağlı | "1024x1024" | "256x256", "512x512", "1024x1024" |
| `n` | Oluşturulacak görsel sayısı | INT | isteğe bağlı | 1 | 1 ile 8 arası |
| `görüntü` | Görsel düzenleme için isteğe bağlı referans görseli. | IMAGE | isteğe bağlı | Yok | - |
| `maske` | İç boyama için isteğe bağlı maske (beyaz alanlar değiştirilecektir) | MASK | isteğe bağlı | Yok | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | DALL·E 2'den oluşturulan veya düzenlenen görsel(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

---
**Source fingerprint (SHA-256):** `ad10b149ac28559ad18c09e0f071286509680603d953833106ad6a2d578f7efe`

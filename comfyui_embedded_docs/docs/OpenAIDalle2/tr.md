> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

# OpenAIDalle2

OpenAI'nin DALL·E 2 uç noktası aracılığıyla eşzamanlı olarak görseller oluşturur.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görseller oluşturmak için OpenAI'nin DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda, düğüm bunu OpenAI sunucularına gönderir; sunucular karşılık gelen görselleri oluşturur ve ComfyUI'ye geri döndürür. Düğüm iki modda çalışabilir: yalnızca metin istemi kullanarak standart görsel oluşturma veya hem görsel hem de maske sağlandığında görsel düzenleme modu. Düzenleme modunda, orijinal görselin hangi bölümlerinin değiştirileceğini belirlemek için maskeyi kullanırken diğer alanları değiştirmeden bırakır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|------------|--------|----------|
| `prompt` | STRING | zorunlu | "" | - | DALL·E için metin istemi |
| `seed` | INT | isteğe bağlı | 0 | 0 ile 2147483647 arası | arka uçta henüz uygulanmadı |
| `size` | COMBO | isteğe bağlı | "1024x1024" | "256x256", "512x512", "1024x1024" | Görsel boyutu |
| `n` | INT | isteğe bağlı | 1 | 1 ile 8 arası | Oluşturulacak görsel sayısı |
| `image` | IMAGE | isteğe bağlı | Yok | - | Görsel düzenleme için isteğe bağlı referans görseli. |
| `mask` | MASK | isteğe bağlı | Yok | - | İç boyama için isteğe bağlı maske (beyaz alanlar değiştirilecektir) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `IMAGE` | IMAGE | DALL·E 2'den oluşturulan veya düzenlenen görsel(ler) |

---
**Source fingerprint (SHA-256):** `ad10b149ac28559ad18c09e0f071286509680603d953833106ad6a2d578f7efe`

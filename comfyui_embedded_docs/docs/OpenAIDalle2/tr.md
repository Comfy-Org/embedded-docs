> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/tr.md)

```markdown
OpenAI'nin DALL·E 2 uç noktası aracılığıyla senkron olarak görüntü oluşturur.

## Nasıl Çalışır

Bu düğüm, metin açıklamalarına dayalı görüntüler oluşturmak için OpenAI'nin DALL·E 2 API'sine bağlanır. Bir metin istemi sağladığınızda, düğüm bunu OpenAI'nin sunucularına gönderir ve bu sunucular ilgili görüntüleri oluşturarak ComfyUI'ye geri döndürür. Düğüm iki modda çalışabilir: sadece metin istemi kullanarak standart görüntü oluşturma veya hem görüntü hem de maske sağlandığında görüntü düzenleme modu. Düzenleme modunda, orijinal görüntünün hangi bölümlerinin değiştirileceğini belirlemek için maskeyi kullanırken diğer alanları değişmeden bırakır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | gerekli | "" | - | DALL·E için metin istemi |
| `seed` | INT | isteğe bağlı | 0 | 0 ile 2147483647 arası | arka uçta henüz uygulanmadı |
| `size` | COMBO | isteğe bağlı | "1024x1024" | "256x256", "512x512", "1024x1024" | Görüntü boyutu |
| `n` | INT | isteğe bağlı | 1 | 1 ile 8 arası | Kaç adet görüntü oluşturulacağı |
| `image` | IMAGE | isteğe bağlı | Yok | - | Görüntü düzenleme için isteğe bağlı referans görüntüsü. |
| `mask` | MASK | isteğe bağlı | Yok | - | İç boyama için isteğe bağlı maske (beyaz alanlar değiştirilecektir) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | DALL·E 2'den oluşturulan veya düzenlenen görüntü(ler) |
```
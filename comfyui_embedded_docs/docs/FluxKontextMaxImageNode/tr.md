# Flux.1 Kontext [maks] Görüntü

Flux.1 Kontext [max] ile BFL API'si üzerinden bir istem ve en-boy oranına dayalı olarak görsel üretir veya düzenler. `input_image` bağlıyken istem, düzenlemeyi tanımlar; bağlı değilken düğüm yalnızca isteme dayanarak yeni bir görsel üretir. Flux.1 Kontext [pro] Image ile aynı girdileri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|----------|--------|
| `istem` | Görsel üretimi için istem. Bir giriş görseli varsa neyin ve nasıl düzenleneceğini belirtin. | STRING | Evet | - |
| `en-boy_oranı` | Görselin en-boy oranı; 1:4 ile 4:1 arasında olmalıdır (varsayılan: `"16:9"`). | STRING | Evet | - |
| `rehberlik` | Görsel üretim süreci için yönlendirme gücü (varsayılan: 3.0). | FLOAT | Evet | 0.1 ile 99.0 arası (adım: 0.1) |
| `adımlar` | Görsel üretim süreci için adım sayısı (varsayılan: 50). | INT | Evet | 1 ile 150 arası |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele seed (varsayılan: 1234). | INT | Evet | 0 ile 18446744073709551615 arası |
| `istem_yukarı_örnekleme` | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinse istem daha yaratıcı üretim için otomatik olarak değiştirilir, ancak sonuçlar deterministik değildir; bu nedenle aynı seed tam olarak aynı sonucu üretmez (varsayılan: `False`). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True / False |
| `girdi_görüntüsü` | Düzenlemek için isteğe bağlı görsel. Atlandığında, istemin boş olmadığından emin olmak için doğrulama yapılır. | IMAGE | Hayır | - |

**Not:** Düğüm isteği BFL'ye gönderir ve görsel hazır olana kadar yoklar. BFL'nin içerik moderasyonu tarafından reddedilen istekler, görsel döndürmek yerine başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Üretilen veya düzenlenen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMaxImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `557f9e69de37ee89e161dffdaef7458ed026b884298594f2046454b6b8d3c415`

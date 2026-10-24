# Flux.1 Kontext [pro] Görüntü

Flux.1 Kontext [pro] ile BFL API'si üzerinden, bir istem ve en-boy oranına dayalı olarak görsel oluşturur veya düzenler. `input_image` bağlıyken istem düzenlemeyi açıklar; bağlı değilken düğüm yalnızca istemden yeni bir görsel oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Görsel oluşturma için istem. Bir giriş görseliyle birlikte, neyin ve nasıl düzenleneceğini belirtin. | STRING | Evet | - |
| `en-boy_oranı` | Görselin en-boy oranı; 1:4 ile 4:1 arasında olmalıdır (varsayılan: `"16:9"`). | STRING | Evet | - |
| `kılavuzluk` | Görsel oluşturma süreci için yönlendirme gücü (varsayılan: 3.0). | FLOAT | Evet | 0.1 ile 99.0 arası (adım: 0.1) |
| `adımlar` | Görsel oluşturma süreci için adım sayısı (varsayılan: 50). | INT | Evet | 1 ile 150 arası |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 1234). | INT | Evet | 0 ile 18446744073709551615 arası |
| `istek_artırma` | İstem üzerinde üst örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı oluşturma için istem otomatik olarak değiştirilir; ancak sonuçlar deterministik değildir, bu nedenle aynı tohum tam olarak aynı sonucu üretmeyecektir (varsayılan: `False`). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True / False |
| `girdi_görseli` | Düzenlenecek isteğe bağlı görsel. Belirtilmediğinde, istemin boş olmadığından emin olmak için istem doğrulanır. | IMAGE | Hayır | - |

**Not:** Düğüm isteği BFL'ye gönderir ve görsel hazır olana kadar yoklar. BFL'nin içerik denetimi tarafından reddedilen istekler, görsel döndürmek yerine başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan veya düzenlenen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextProImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `7a5be7e7859b1aca5130552345c76045ab64be3b4bee588091d147480a9ae1ac`

# FluxProImageNode

İstem ve çözünürlüğe göre görüntüleri eşzamanlı olarak oluşturur. Bu düğüm, bir API uç noktasına istekler göndererek ve oluşturulan görüntüyü döndürmeden önce tam yanıtı bekleyerek Flux 1.1 Pro modelini kullanarak görüntüler oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Görüntü oluşturma istemi (varsayılan: boş dize) | STRING | Evet | - |
| `prompt_upsampling` | İstem üzerinde üst örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum tam olarak aynı sonucu üretmez). (varsayılan: False) | BOOLEAN | Evet | - |
| `width` | Piksel cinsinden görüntü genişliği (varsayılan: 1024, adım: 32) | INT | Evet | 256-1440 |
| `height` | Piksel cinsinden görüntü yüksekliği (varsayılan: 768, adım: 32) | INT | Evet | 256-1440 |
| `seed` | Gürültüyü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `image_prompt` | Oluşturmayı yönlendirmek için isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | API'den döndürülen oluşturulmuş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`

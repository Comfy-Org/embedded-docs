> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/tr.md)

## Genel Bakış

Bu düğüm, metin istemi ve çözünürlüğe göre eşzamanlı olarak görseller oluşturur. Flux 1.1 Pro modelini kullanarak bir API uç noktasına istek gönderir ve oluşturulan görseli döndürmeden önce tam yanıtı bekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `prompt` | STRING | Evet | - | Görsel oluşturma için metin istemi (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Evet | - | Metin isteminde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı üretim için metin istemi otomatik olarak değiştirilir, ancak sonuçlar deterministik değildir (aynı tohum değeri tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `width` | INT | Evet | 256-1440 | Piksel cinsinden görsel genişliği (varsayılan: 1024, adım: 32) |
| `height` | INT | Evet | 256-1440 | Piksel cinsinden görsel yüksekliği (varsayılan: 768, adım: 32) |
| `seed` | INT | Evet | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `image_prompt` | IMAGE | Hayır | - | Üretimi yönlendirmek için isteğe bağlı referans görseli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | IMAGE | API'den döndürülen oluşturulmuş görsel |

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`

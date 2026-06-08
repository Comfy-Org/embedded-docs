Pikaffects düğümü, bir girdi görüntüsüne çeşitli görsel efektler uygulayarak videolar oluşturur. Statik görüntüleri erime, patlama veya havaya yükselme gibi belirli efektlerle animasyonlu videolara dönüştürmek için Pika'nın video oluşturma API'sini kullanır. Düğüm, Pika hizmetine erişmek için bir API anahtarı ve kimlik doğrulama belirteci gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Pikaffect'in uygulanacağı referans görüntü. | IMAGE | Evet | - |
| `pikaffect` | Görüntüye uygulanacak belirli görsel efekt (varsayılan: "Cake-ify"). | COMBO | Evet | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Video oluşturmayı yönlendiren metin açıklaması. | STRING | Evet | - |
| `negative_prompt` | Oluşturulan videoda kaçınılması gerekenleri belirten metin açıklaması. | STRING | Evet | - |
| `seed` | Tekrarlanabilir sonuçlar için rastgele tohum değeri. | INT | Evet | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Uygulanan Pikaffect ile oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/tr.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`

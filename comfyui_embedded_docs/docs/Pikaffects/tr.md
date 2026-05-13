> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/tr.md)

Pikaffects düğümü, bir girdi görüntüsüne çeşitli görsel efektler uygulayarak videolar oluşturur. Statik görüntüleri erime, patlama veya havaya yükselme gibi belirli efektlerle animasyonlu videolara dönüştürmek için Pika'nın video oluşturma API'sini kullanır. Düğüm, Pika hizmetine erişmek için bir API anahtarı ve kimlik doğrulama belirteci gerektirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Pikaffect'in uygulanacağı referans görüntü. |
| `pikaffect` | COMBO | Evet | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | Görüntüye uygulanacak belirli görsel efekt (varsayılan: "Cake-ify"). |
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması. |
| `negative_prompt` | STRING | Evet | - | Oluşturulan videoda kaçınılması gerekenleri belirten metin açıklaması. |
| `seed` | INT | Evet | 0 ile 4294967295 arası | Tekrarlanabilir sonuçlar için rastgele tohum değeri. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Uygulanan Pikaffect ile oluşturulan video. |

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`

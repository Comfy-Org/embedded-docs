> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/tr.md)

Pikaffects düğümü, bir giriş görseline çeşitli görsel efektler uygulanmış videolar oluşturur. Pika'nın video oluşturma API'sini kullanarak statik görselleri erime, patlama veya havaya kalkma gibi belirli efektlerle animasyonlu videolara dönüştürür. Düğümün Pika hizmetine erişmek için bir API anahtarı ve kimlik doğrulama belirteci gerektirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Pikaffect uygulanacak referans görsel. |
| `pikaffect` | COMBO | Evet | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | Görsele uygulanacak belirli görsel efekt (varsayılan: "Cake-ify"). |
| `istem_metni` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması. |
| `negatif_istem` | STRING | Evet | - | Oluşturulan videoda nelerden kaçınılacağını belirten metin açıklaması. |
| `tohum` | INT | Evet | 0 - 4294967295 | Tekrarlanabilir sonuçlar için rastgele tohum değeri. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Uygulanan Pikaffect ile oluşturulan video. |
> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/tr.md)

Bu düğüm, HunyuanVideo 1.5 modeli ile kullanım için özel olarak biçimlendirilmiş boş bir gizli tensör oluşturur. Modelin gizli uzayı için doğru kanal sayısı ve uzamsal boyutlara sahip bir sıfırlar tensörü tahsis ederek video oluşturma için boş bir başlangıç noktası üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | - | Video karesinin piksel cinsinden genişliği. |
| `height` | INT | Evet | - | Video karesinin piksel cinsinden yüksekliği. |
| `length` | INT | Evet | - | Video dizisindeki kare sayısı. |
| `batch_size` | INT | Hayır | - | Bir partide oluşturulacak video örneği sayısı (varsayılan: 1). |

**Not:** Oluşturulan gizli tensörün uzamsal boyutları, giriş `width` ve `height` değerlerinin 16'ya bölünmesiyle hesaplanır. Zamansal boyut (kareler) ise `((length - 1) // 4) + 1` formülüyle hesaplanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | HunyuanVideo 1.5 modeli için uygun boyutlara sahip boş bir gizli tensör. Tensörün şekli `[batch_size, 32, frames, height//16, width//16]` şeklindedir. |

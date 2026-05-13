> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/tr.md)

Bu düğüm, HunyuanVideo 1.5 modeliyle kullanılmak üzere özel olarak biçimlendirilmiş boş bir gizli tensör oluşturur. Modelin gizli alanı için doğru kanal sayısına ve uzamsal boyutlara sahip sıfırlardan oluşan bir tensör tahsis ederek video oluşturma için boş bir başlangıç noktası üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `genişlik` | INT | Evet | - | Video karesinin piksel cinsinden genişliği. |
| `yükseklik` | INT | Evet | - | Video karesinin piksel cinsinden yüksekliği. |
| `uzunluk` | INT | Evet | - | Video dizisindeki kare sayısı. |
| `toplu_boyut` | INT | Hayır | - | Bir grupta oluşturulacak video örneklerinin sayısı (varsayılan: 1). |

**Not:** Oluşturulan gizli tensörün uzamsal boyutları, giriş `width` ve `height` değerlerinin 16'ya bölünmesiyle hesaplanır. Zamansal boyut (kareler) ise `((length - 1) // 4) + 1` formülüyle hesaplanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `samples` | LATENT | HunyuanVideo 1.5 modeli için uygun boyutlara sahip boş bir gizli tensör. Tensör `[batch_size, 32, frames, height//16, width//16]` şeklindedir. Çıktı ayrıca 16 değerinde bir `downscale_ratio_spacial` içerir. |

---
**Source fingerprint (SHA-256):** `eebc131adfe63f6bc8367f2a96b3ac7f3f3223c5b1fb308eda3ec09c94fff2ee`

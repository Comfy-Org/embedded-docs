> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/tr.md)

Boş Qwen Görüntü Katmanlı Gizli (Empty Qwen Image Layered Latent) düğümü, Qwen görüntü modelleriyle kullanılmak üzere boş, çok katmanlı bir gizli temsil oluşturur. Belirtilen sayıda katman, grup boyutu ve uzamsal boyutlarla yapılandırılmış, sıfırlarla dolu bir tensör üretir. Bu boş gizli temsil, sonraki görüntü oluşturma veya düzenleme iş akışları için bir başlangıç noktası görevi görür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `genişlik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Oluşturulacak gizli görüntünün genişliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) |
| `yükseklik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Oluşturulacak gizli görüntünün yüksekliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) |
| `katmanlar` | INT | Evet | 0 ile MAX_RESOLUTION arası | Gizli yapıya eklenecek ek katman sayısı. Bu, gizli temsilin derinliğini tanımlar. (varsayılan: 3) |
| `toplu_boyut` | INT | Hayır | 1 ile 4096 arası | Bir grupta oluşturulacak gizli örnek sayısı. (varsayılan: 1) |

**Not:** `width` ve `height` parametreleri, çıktı gizli tensörünün uzamsal boyutlarını belirlemek için dahili olarak 8'e bölünür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Sıfırlarla dolu bir gizli tensör. Şekli `[batch_size, 16, layers + 1, height // 8, width // 8]` şeklindedir. |

---
**Source fingerprint (SHA-256):** `99497e3e4a67bf7b3f650573e7b8eb2d7fad6be5819b7ebbbb8736291dc44e0c`

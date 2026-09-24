# Quiver Metinden SVG'ye

Quiver Text to SVG düğümü, Quiver AI'nin modellerini kullanarak bir metin açıklamasından Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü oluşturur. Oluşturma sürecine yön vermek için isteğe bağlı olarak referans görüntüler ve stil talimatları sağlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | İstenen SVG çıktısının metin açıklaması. Oluşturulacak şey için ana talimattır. | STRING | Evet | N/A |
| `instructions` | Ek stil veya biçimlendirme rehberliği. Bu isteğe bağlı, gelişmiş bir parametredir. | STRING | Hayır | N/A |
| `reference_images` | Oluşturmaya yön vermek için en fazla 4 referans görüntü. Bu isteğe bağlı bir girdidir. | IMAGE | Hayır | 0 - 4 görüntü |
| `model` | SVG oluşturmak için kullanılacak model. Bir model seçildiğinde, o modele özgü ek parametreler görünür: `temperature`, `top_p` ve `presence_penalty`. | DYNAMIC_COMBO | Evet | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ile 2147483647 arası |
| `reasoning_effort` | Modelin çizim yapmadan önce ne kadar akıl yürütmeye harcadığı. Daha yüksek seviyeler ayrıntıyı iyileştirir ve daha fazla token maliyeti doğurur. Yalnızca Arrow 2 modelleri tarafından kullanılır (varsayılan: "high"). | COMBO | Hayır | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**Not:** `reference_images` girdisi en fazla 4 görüntü kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Oluşturulan Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `8b6f21c26748f48eddf2eddaed785a2331a29364744edf30e86e420b0c117e49`

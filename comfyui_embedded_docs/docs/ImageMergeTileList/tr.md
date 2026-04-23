> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/tr.md)

Bu düğüm, bir görüntü döşeme listesini alır ve bunları tek, daha büyük bir görüntü halinde birleştirir. Daha önce üst üste binen döşemelerden oluşan bir ızgaraya bölünmüş bir görüntüyü, kesintisiz bir nihai sonuç oluşturmak için ağırlıklı bir karıştırma tekniği kullanarak yeniden oluşturmak üzere tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image_list` | IMAGE | Evet | Yok | Birleştirilecek görüntü döşemelerinin listesi. Listedeki ilk döşeme, tüm işlem için döşeme boyutlarını ve veri türünü belirlemek amacıyla kullanılır. |
| `final_width` | INT | Hayır | 64 - 32768 | Nihai birleştirilmiş görüntünün piksel cinsinden genişliği (varsayılan: 1024). |
| `final_height` | INT | Hayır | 64 - 32768 | Nihai birleştirilmiş görüntünün piksel cinsinden yüksekliği (varsayılan: 1024). |
| `overlap` | INT | Hayır | 0 - 4096 | Bitişik döşemeler arasındaki piksel cinsinden örtüşme miktarı. 0'dan büyük bir değer, döşeme birleşim yerlerinde yumuşak bir karıştırma efekti sağlar (varsayılan: 128). |

**Not:** `image_list` dinamik bir giriş listesidir. Düğüm, döşemeleri sağlandıkları sırayla, `final_width`, `final_height` ve ilk döşemenin boyutları tarafından tanımlanan ızgarayı doldurmak için gereken sayıya kadar işleyecektir. Liste gerekenden daha fazla döşeme içeriyorsa, fazladan döşemeler yok sayılır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Giriş döşemelerinden yeniden oluşturulan nihai birleştirilmiş görüntü. |
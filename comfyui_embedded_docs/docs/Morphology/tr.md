> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/tr.md)

Morphology düğümü, görüntülerdeki şekilleri işlemek ve analiz etmek için kullanılan matematiksel işlemler olan çeşitli morfolojik işlemleri görüntülere uygular. Etki gücünü kontrol etmek için özelleştirilebilir bir çekirdek boyutu kullanarak aşındırma, genişletme, açma, kapama ve daha fazlası gibi işlemleri gerçekleştirebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | İşlenecek giriş görüntüsü |
| `işlem` | STRING | Evet | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | Uygulanacak morfolojik işlem |
| `çekirdek_boyutu` | INT | Hayır | 3-999 | Yapılandırıcı eleman çekirdeğinin boyutu (varsayılan: 3) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Morfolojik işlem uygulandıktan sonra işlenmiş görüntü |
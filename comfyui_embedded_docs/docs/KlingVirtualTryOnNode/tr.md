> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/tr.md)

Kling Sanal Giyim Node. Bir insan görüntüsü ve bir giysi görntüsü girerek, giysinin insanın üzerinde denenmiş halini elde edin. Birden fazla giysi parçasının resmini beyaz bir arka planda tek bir görüntüde birleştirebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | Evet | - | Üzerine giysi denenecak insan görüntüsü |
| `cloth_image` | IMAGE | Evet | - | İnsanın üzerinde denenecek giysi görüntüsü |
| `model_name` | STRING | Evet | `"kolors-virtual-try-on-v1"` | Kullanılacak sanal giydirme modeli (varsayılan: "kolors-virtual-try-on-v1") |

## Çıktılar

| Çıktı Adı | Veri Türu | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Giysi parçasının insanın üzerinde denenmiş halini gösteren sonuç görüntüsü |
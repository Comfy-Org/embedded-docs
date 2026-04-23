> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/tr.md)

## Genel Bakış

Frame Interpolate (Kare Enterpolasyonu) düğümü, bir görüntü dizisindeki mevcut kareler arasında yeni kareler oluşturarak kare hızını etkili bir şekilde artırır. Ara karelerin nasıl görünmesi gerektiğini tahmin etmek için bir yapay zeka modeli kullanır; bu sayede yumuşak ağır çekim efektleri oluşturmak veya bir videonun akıcılığını artırmak için kullanılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `interp_model` | MODEL | Evet | - | Ara kareler oluşturmak için kullanılacak kare enterpolasyon modeli |
| `images` | IMAGE | Evet | - | Enterpolasyon yapılacak ardışık görüntüler (kareler) topluluğu. En az 2 görüntü gerektirir. |
| `multiplier` | INT | Evet | 2 ile 16 | Kare sayısını çarpma katsayısı. Örneğin, 2 çarpanı kare sayısını iki katına çıkarır. (varsayılan: 2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Orijinal kareler arasına enterpolasyonlu karelerin eklendiği yeni bir görüntü topluluğu. Sonuçta daha akıcı bir dizi elde edilir. Toplam çıktı kare sayısı `(giriş kare sayısı - 1) * çarpan + 1` formülüyle hesaplanır. |
# Kare Enterpolasyonu

Frame Interpolate düğümü, bir görüntü dizisindeki mevcut kareler arasına yeni kareler oluşturarak kare hızını etkili bir şekilde artırır. Ara karelerin nasıl görünmesi gerektiğini tahmin etmek için bir yapay zeka modeli kullanır; bu, akıcı ağır çekim efektleri oluşturmak veya bir videonun akıcılığını artırmak için kullanılabilir. Düğüm, ardışık her kare çifti için `multiplier - 1` yeni kare üretir ve bunları orijinallerin arasına ekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `interp_model` | Ara karelerin üretilmesi için kullanılacak kare enterpolasyon modeli (örneğin, RIFE veya FILM modelleri) | INTERP_MODEL | Evet | - |
| `images` | Araya enterpolasyon yapılacak ardışık görüntülerden (karelerden) oluşan bir yığın. En az 2 görüntü gerektirir; daha az sağlanırsa, düğüm giriş görüntülerini değiştirmeden döndürür. | IMAGE | Evet | - |
| `multiplier` | Kare sayısının çarpılacağı katsayı. Örneğin, 2 çarpanı kare sayısını ikiye katlar. (varsayılan: 2) | INT | Evet | 2 to 16 |

Not: Giriş görüntü yığını en az 2 kare içermelidir, çünkü enterpolasyon ardışık kare çiftleri arasında gerçekleştirilir. Çıktıdaki toplam kare sayısı `(number of input frames - 1) * multiplier + 1` formülüyle hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Ara karelerin orijinal kareler arasına eklenmesiyle elde edilen, daha akıcı bir dizi oluşturan yeni görüntü yığını. Çıktıdaki toplam kare sayısı `(number of input frames - 1) * multiplier + 1` formülüyle hesaplanır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/tr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`

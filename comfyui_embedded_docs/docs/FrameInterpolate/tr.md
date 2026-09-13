# Kare Enterpolasyonu

Frame Interpolate düğümü, bir görüntü dizisindeki mevcut kareler arasında yeni kareler oluşturarak kare hızını etkili biçimde artırır. Ara karelerin nasıl görünmesi gerektiğini tahmin etmek için bir yapay zeka modeli kullanır; bu, akıcı ağır çekim efektleri oluşturmak veya bir videonun akıcılığını artırmak için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `interp_model` | Ara kareleri oluşturmak için kullanılacak kare enterpolasyon modeli | INTERP_MODEL | Evet | - |
| `images` | Aralarında enterpolasyon yapılacak ardışık görüntü (kare) grubu. En az 2 görüntü gerektirir. 2'den az kare sağlanırsa düğüm, giriş görüntülerini değiştirmeden döndürür. | IMAGE | Evet | - |
| `multiplier` | Kare sayısının kaç katına çıkarılacağı. Örneğin, 2 çarpanı kare sayısını iki katına çıkarır. (varsayılan: 2) | INT | Evet | 2 ile 16 |

**Not:** Düğüm, en az 2 giriş karesi ve `multiplier` için en az 2 değeri gerektirir. Bu koşullardan biri karşılanmazsa, giriş görüntüleri değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Orijinal karelerin arasına enterpolasyonlu kareler eklenmiş yeni bir görüntü grubu; bu, daha akıcı bir dizi oluşturur. Toplam çıktı karesi sayısı `(number of input frames - 1) * multiplier + 1` olur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/tr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`

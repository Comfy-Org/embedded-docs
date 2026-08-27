# Kare Enterpolasyonu

Frame Interpolate düğümü, bir görüntü dizisindeki mevcut kareler arasında yeni kareler oluşturarak kare hızını etkili bir şekilde artırır. Ara karelerin nasıl görünmesi gerektiğini tahmin etmek için bir yapay zeka modeli kullanır; bu, akıcı ağır çekim efektleri oluşturmak veya bir videonun akıcılığını artırmak için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `enterpolasyon_modeli` | Ara karelerin oluşturulması için kullanılacak kare interpolasyon modeli | INTERP_MODEL | Evet | - |
| `görseller` | Aralarında interpolasyon yapılacak ardışık görüntülerden (karelerden) oluşan bir küme. En az 2 görüntü gerektirir. 2'den az kare sağlanırsa, düğüm girdi görüntülerini değiştirmeden döndürür. | IMAGE | Evet | - |
| `çarpan` | Kare sayısının kaç katına çıkarılacağını belirtir. Örneğin, 2 çarpanı kare sayısını iki katına çıkarır. (varsayılan: 2) | INT | Evet | 2 ila 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Orijinal karelerin arasına interpolasyon karelerinin eklenmesiyle oluşan ve daha akıcı bir sekans sağlayan yeni görüntü kümesi. Toplam çıktı karesi sayısı `(number of input frames - 1) * multiplier + 1` formülüyle hesaplanır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/tr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`

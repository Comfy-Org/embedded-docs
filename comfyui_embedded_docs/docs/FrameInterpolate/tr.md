## Genel Bakış

Frame Interpolate düğümü, bir görüntü dizisindeki mevcut kareler arasına yeni kareler ekleyerek kare hızını etkili bir şekilde artırır. Ara karelerin nasıl görünmesi gerektiğini tahmin etmek için bir yapay zeka modeli kullanır. Bu özellik, yumuşak ağır çekim efektleri oluşturmak veya bir videonun akıcılığını artırmak için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `enterpolasyon_modeli` | Ara kareler oluşturmak için kullanılacak kare enterpolasyon modeli | MODEL | Evet | - |
| `görseller` | Enterpolasyon yapılacak ardışık görüntüler (kareler) topluluğu. En az 2 görüntü gerektirir. | IMAGE | Evet | - |
| `çarpan` | Kare sayısının çarpılacağı katsayı. Örneğin, 2 çarpanı kare sayısını ikiye katlar. (varsayılan: 2) | INT | Evet | 2 ila 16 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Orijinal kareler arasına enterpolasyonlu kareler eklenmiş yeni bir görüntü topluluğu. Bu sayede daha akıcı bir dizi elde edilir. Toplam çıktı kare sayısı: `(giriş kare sayısı - 1) * çarpan + 1` formülüyle hesaplanır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/tr.md)

---
**Source fingerprint (SHA-256):** `05fdac188d9d7c7d5cac9ade55ba22cc743395b3c659a519ca03fe293b9a6e34`

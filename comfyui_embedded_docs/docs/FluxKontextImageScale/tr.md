> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/tr.md)

Bu düğüm, giriş görüntüsünün en-boy oranına dayanarak, Flux Kontext modeli eğitimi sırasında kullanılan optimal bir boyuta ölçeklendirir ve Lanczos algoritmasını kullanır. Bu düğüm, özellikle büyük boyutlu görüntüler girilirken kullanışlıdır, çünkü aşırı büyük girişler model çıktı kalitesinin düşmesine veya çıktıda birden fazla konunun belirmesi gibi sorunlara yol açabilir.

## Girişler

| Parametre Adı | Veri Türü | Giriş Türü | Varsayılan Değer | Değer Aralığı | Açıklama |
|----------------|-----------|------------|---------------|-------------|-------------|
| `image` | IMAGE | Gerekli | - | - | Yeniden boyutlandırılacak giriş görüntüsü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Yeniden boyutlandırılmış görüntü |

## Önceden Ayarlanmış Boyut Listesi

Aşağıda, model eğitimi sırasında kullanılan standart boyutların bir listesi bulunmaktadır. Düğüm, giriş görüntüsünün en-boy oranına en yakın boyutu seçecektir:

| Genişlik | Yükseklik | En-Boy Oranı |
|-------|--------|--------------|
| 672   | 1568   | 0.429       |
| 688   | 1504   | 0.457       |
| 720   | 1456   | 0.494       |
| 752   | 1392   | 0.540       |
| 800   | 1328   | 0.603       |
| 832   | 1248   | 0.667       |
| 880   | 1184   | 0.743       |
| 944   | 1104   | 0.855       |
| 1024  | 1024   | 1.000       |
| 1104  | 944    | 1.170       |
| 1184  | 880    | 1.345       |
| 1248  | 832    | 1.500       |
| 1328  | 800    | 1.660       |
| 1392  | 752    | 1.851       |
| 1456  | 720    | 2.022       |
| 1504  | 688    | 2.186       |
| 1568  | 672    | 2.333       |
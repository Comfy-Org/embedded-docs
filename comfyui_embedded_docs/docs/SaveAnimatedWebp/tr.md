Bu düğüm, bir dizi görüntüyü animasyonlu WEBP dosyası olarak kaydetmek için tasarlanmıştır. Tek tek kareleri tutarlı bir animasyonda birleştirir, belirtilen meta verileri uygular ve kalite ve sıkıştırma ayarlarına göre çıktıyı optimize eder.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Animasyonlu WEBP'de kare olarak kaydedilecek görüntü listesi. Bu parametre, animasyonun görsel içeriğini tanımlamak için gereklidir. | `IMAGE` |
| `dosyaadı_öneki` | Çıktı dosyası için temel adı belirtir; bu ada bir sayaç ve '.webp' uzantısı eklenir. Bu parametre, kaydedilen dosyaları tanımlamak ve düzenlemek için çok önemlidir. | `STRING` |
| `fps` | Animasyonun saniyedeki kare sayısını belirler ve oynatma hızını etkiler. | `FLOAT` |
| `kayıpsız` | Kayıpsız sıkıştırma kullanılıp kullanılmayacağını belirten bir boole değeridir; animasyonun dosya boyutunu ve kalitesini etkiler. | `BOOLEAN` |
| `kalite` | 0 ile 100 arasında bir değer alarak sıkıştırma kalite seviyesini ayarlar; daha yüksek değerler daha iyi görüntü kalitesi ancak daha büyük dosya boyutları sağlar. | `INT` |
| `yöntem` | Kullanılacak sıkıştırma yöntemini belirtir; kodlama hızını ve dosya boyutunu etkileyebilir. | COMBO[STRING] |

## Çıktılar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui` | Kaydedilen animasyonlu WEBP görüntülerini meta verileriyle birlikte gösteren ve animasyonun etkin olup olmadığını belirten bir UI bileşeni sağlar. | N/A |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/tr.md)

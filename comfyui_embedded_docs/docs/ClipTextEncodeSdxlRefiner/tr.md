> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/tr.md)

Bu düğüm, SDXL Refiner modeli için özel olarak tasarlanmış olup, metin prompt'larını koşullandırma bilgisine dönüştürürken estetik puanları ve boyutsal bilgileri dahil ederek üretim görevleri için koşulları geliştirir ve böylece nihai iyileştirme etkisini artırır. Profesyonel bir sanat yönetmeni gibi davranarak yalnızca yaratıcı niyetinizi iletmekle kalmaz, aynı zamanda esere kesin estetik standartlar ve özellik gereksinimleri de enjekte eder.

## SDXL Refiner Hakkında

SDXL Refiner, SDXL temel modeli temel alınarak görüntü detaylarını ve kalitesini geliştirmeye odaklanan özel bir iyileştirme modelidir. Bu süreç, bir sanat rötüşçüsüne sahip olmak gibidir:

1.  İlk olarak, temel model tarafından oluşturulan ön görüntüleri veya metin açıklamalarını alır
2.  Ardından, kesin estetik puanlama ve boyutsal parametreler aracılığıyla iyileştirme sürecini yönlendirir
3.  Son olarak, genel kaliteyi artırmak için yüksek frekanslı görüntü detaylarının işlenmesine odaklanır

Refiner iki şekilde kullanılabilir:

-   Temel model tarafından oluşturulan görüntüler için son işlem olarak bağımsız bir iyileştirme adımı olarak
-   Uzman bir entegrasyon sisteminin parçası olarak, üretimin düşük gürültülü aşamasında işlemi devralarak

## Girdiler

| Parametre Adı | Veri Türü | Girdi Türü | Varsayılan Değer | Değer Aralığı | Açıklama |
|----------------|-----------|------------|---------------|-------------|-------------|
| `clip` | CLIP | Gerekli | - | - | Metin tokenizasyonu ve kodlama için kullanılan CLIP model örneği, metni model tarafından anlaşılabilir formata dönüştüren çekirdek bileşen |
| `askor` | FLOAT | İsteğe Bağlı | 6.0 | 0.0-1000.0 | Oluşturulan görüntülerin görsel kalitesini ve estetiğini kontrol eder, bir sanat eseri için kalite standartları belirlemek gibidir:<br/>- Yüksek puanlar (7.5-8.5): Daha rafine, detay zengini efektler hedefler<br/>- Orta puanlar (6.0-7.0): Dengeli kalite kontrolü<br/>- Düşük puanlar (2.0-3.0): Negatif prompt'lar için uygundur |
| `genişlik` | INT | Gerekli | 1024 | 64-16384 | Çıktı görüntü genişliğini (piksel) belirtir, 8'in katı olmalıdır. SDXL, toplam piksel sayısı 1024×1024'e (yaklaşık 1M piksel) yakın olduğunda en iyi performansı gösterir |
| `yükseklik` | INT | Gerekli | 1024 | 64-16384 | Çıktı görüntü yüksekliğini (piksel) belirtir, 8'in katı olmalıdır. SDXL, toplam piksel sayısı 1024×1024'e (yaklaşık 1M piksel) yakın olduğunda en iyi performansı gösterir |
| `metin` | STRING | Gerekli | - | - | Metin prompt açıklaması, çok satırlı girişi ve dinamik prompt sözdizimini destekler. Refiner'da, metin prompt'ları istenen görsel kalite ve detay özelliklerini tanımlamaya daha fazla odaklanmalıdır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Metin anlambilimi, estetik standartlar ve boyutsal bilginin entegre kodlamasını içeren, iyileştirilmiş koşullu çıktı; özellikle SDXL Refiner modeline kesin görüntü iyileştirmesi için rehberlik etmek üzere |

## Notlar

1.  Bu düğüm, SDXL Refiner modeli için özel olarak optimize edilmiştir ve normal CLIPTextEncode düğümlerinden farklıdır
2.  7.5 estetik puanı, temel değer olarak önerilir; bu, SDXL eğitiminde kullanılan standart ayardır
3.  Tüm boyutsal parametreler 8'in katı olmalıdır ve toplam piksel sayısının 1024×1024'e (yaklaşık 1M piksel) yakın olması önerilir
4.  Refiner modeli, görüntü detaylarını ve kalitesini geliştirmeye odaklandığından, metin prompt'ları sahne içeriğinden ziyade istenen görsel efektleri vurgulamalıdır
5.  Pratik kullanımda, Refiner tipik olarak üretimin sonraki aşamalarında (yaklaşık son adımların %20'si) kullanılır ve detay optimizasyonuna odaklanır
> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/tr.md)

Bu düğüm, metin istemlerini estetik puanları ve boyut bilgilerini dahil ederek koşullandırma bilgisine dönüştürmek, böylece üretim görevleri için koşulları iyileştirmek ve nihai iyileştirme etkisini artırmak üzere özel olarak SDXL Refiner modeli için tasarlanmıştır. Profesyonel bir sanat yönetmeni gibi çalışarak yalnızca yaratıcı niyetinizi iletmekle kalmaz, aynı zamanda çalışmaya hassas estetik standartlar ve teknik özellik gereksinimleri de enjekte eder.

## SDXL Refiner Hakkında

SDXL Refiner, SDXL temel modeline dayalı olarak görüntü ayrıntılarını ve kalitesini geliştirmeye odaklanan özel bir iyileştirme modelidir. Bu süreç, bir görüntü rötuşçusuna sahip olmak gibidir:

1. İlk olarak, temel model tarafından oluşturulan ön görüntüleri veya metin açıklamalarını alır
2. Ardından, hassas estetik puanlama ve boyut parametreleri aracılığıyla iyileştirme sürecini yönlendirir
3. Son olarak, genel kaliteyi artırmak için görüntünün yüksek frekanslı ayrıntılarını işlemeye odaklanır

Refiner iki şekilde kullanılabilir:

- Temel model tarafından oluşturulan görüntüleri işlemek için bağımsız bir iyileştirme adımı olarak
- Uzman entegrasyon sisteminin bir parçası olarak, üretimin düşük gürültü aşamasında işlemi devralarak

## Girişler

| Parametre Adı | Veri Türü | Giriş Türü | Varsayılan Değer | Değer Aralığı | Açıklama |
|---------------|-----------|------------|-----------------|---------------|----------|
| `clip` | CLIP | Zorunlu | - | - | Metin tokenizasyonu ve kodlaması için kullanılan CLIP model örneği, metni modelin anlayabileceği formata dönüştüren temel bileşen |
| `ascore` | FLOAT | İsteğe Bağlı | 6.0 | 0.0-1000.0 | Oluşturulan görüntülerin görsel kalitesini ve estetiğini kontrol eder, sanat eserleri için kalite standartları belirlemeye benzer:<br/>- Yüksek puanlar (7.5-8.5): Daha rafine, ayrıntı açısından zengin efektler hedefler<br/>- Orta puanlar (6.0-7.0): Dengeli kalite kontrolü<br/>- Düşük puanlar (2.0-3.0): Negatif istemler için uygundur |
| `width` | INT | Zorunlu | 1024 | 64-16384 | Çıktı görüntü genişliğini (piksel) belirtir, 8'in katı olmalıdır. SDXL, toplam piksel sayısı 1024×1024'e (yaklaşık 1M piksel) yakın olduğunda en iyi performansı gösterir |
| `height` | INT | Zorunlu | 1024 | 64-16384 | Çıktı görüntü yüksekliğini (piksel) belirtir, 8'in katı olmalıdır. SDXL, toplam piksel sayısı 1024×1024'e (yaklaşık 1M piksel) yakın olduğunda en iyi performansı gösterir |
| `text` | STRING | Zorunlu | - | - | Metin istemi açıklaması, çok satırlı girişi ve dinamik istem sözdizimini destekler. Refiner'da metin istemleri, istenen görsel kalite ve ayrıntı özelliklerini tanımlamaya daha fazla odaklanmalıdır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `CONDITIONING` | CONDITIONING | Metin anlambilimi, estetik standartlar ve boyut bilgilerinin entegre kodlamasını içeren, özellikle SDXL Refiner modelini hassas görüntü iyileştirmede yönlendirmek için kullanılan rafine koşullu çıktı |

## Notlar

1. Bu düğüm, SDXL Refiner modeli için özel olarak optimize edilmiştir ve normal CLIPTextEncode düğümlerinden farklıdır
2. Estetik puanı olarak 7.5'in temel değer olarak kullanılması önerilir; bu, SDXL eğitiminde kullanılan standart ayardır
3. Tüm boyut parametreleri 8'in katı olmalıdır ve toplam piksel sayısının 1024×1024'e (yaklaşık 1M piksel) yakın olması önerilir
4. Refiner modeli, görüntü ayrıntılarını ve kalitesini geliştirmeye odaklanır, bu nedenle metin istemleri sahne içeriğinden ziyade istenen görsel efektleri vurgulamalıdır
5. Pratik kullanımda, Refiner tipik olarak üretimin sonraki aşamalarında (yaklaşık son %20'lik adım) kullanılır ve ayrıntı optimizasyonuna odaklanır
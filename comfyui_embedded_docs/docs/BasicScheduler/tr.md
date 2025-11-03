> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/tr.md)

`BasicScheduler` düğümü, sağlanan zamanlayıcı, model ve gürültü giderme parametrelerine dayanarak yayılım modelleri için bir sigma değerleri dizisi hesaplamak üzere tasarlanmıştır. Yayılım sürecini hassas bir şekilde ayarlamak için toplam adım sayısını gürültü giderme faktörüne göre dinamik olarak ayarlar ve ince kontrol gerektiren gelişmiş örnekleme süreçlerinde (çok aşamalı örnekleme gibi) farklı aşamalar için kesin "tarifler" sağlar.

## Girdiler

| Parametre   | Veri Türü     | Girdi Türü | Varsayılan | Aralık     | Metafor Açıklaması           | Teknik Amaç                |
| ----------- | ------------- | ---------- | ------- | --------- | ------------------------------ | ---------------------------- |
| `model`     | MODEL         | Input      | -       | -         | **Tuval Türü**: Farklı tuval malzemeleri farklı boya formülleri gerektirir | Yayılım model nesnesi, sigma hesaplama temelini belirler |
| `zamanlayıcı` | COMBO[STRING] | Widget     | -       | 9 seçenek | **Karıştırma Tekniği**: Boya konsantrasyonunun nasıl değişeceğini seçin | Zamanlama algoritması, gürültü azalma modunu kontrol eder |
| `adımlar`     | INT           | Widget     | 20      | 1-10000   | **Karıştırma Sayısı**: 20 karıştırma ile 50 karıştırmanın hassasiyet farkı | Örnekleme adımları, oluşturma kalitesini ve hızını etkiler |
| `gürültü_azaltma`   | FLOAT         | Widget     | 1.0     | 0.0-1.0   | **Oluşturma Yoğunluğu**: İnce ayardan yeniden boyamaya kadar kontrol seviyesi | Gürültü giderme gücü, kısmi yeniden boyama senaryolarını destekler |

### Zamanlayıcı Türleri

Kaynak kodu `comfy.samplers.SCHEDULER_NAMES` temel alınarak, aşağıdaki 9 zamanlayıcı desteklenir:

| Zamanlayıcı Adı       | Özellikler      | Kullanım Alanları                    | Gürültü Azalma Deseni          |
| -------------------- | -------------------- | ---------------------------- | ---------------------------- |
| **normal**           | Standart doğrusal      | Genel senaryolar, dengeli  | Tekdüze azalma                |
| **karras**           | Pürüzsüz geçiş    | Yüksek kalite, detay zengini    | Pürüzsüz doğrusal olmayan azalma      |
| **exponential**      | Üstel azalma    | Hızlı oluşturma, verimlilik  | Üstel hızlı azalma      |
| **sgm_uniform**      | SGM tekdüze          | Belirli model optimizasyonu  | SGM optimize edilmiş azalma          |
| **simple**           | Basit zamanlama    | Hızlı test, temel kullanım     | Basitleştirilmiş azalma             |
| **ddim_uniform**     | DDIM tekdüze         | DDIM örnekleme optimizasyonu   | DDIM'a özgü azalma          |
| **beta**             | Beta dağılımı    | Özel dağılım ihtiyaçları   | Beta fonksiyonu azalması          |
| **linear_quadratic** | Doğrusal ikinci dereceden     | Karmaşık senaryo optimizasyonu| İkinci dereceden fonksiyon azalması     |
| **kl_optimal**       | KL optimal           | Teorik optimizasyon     | KL ıraksaması optimize edilmiş azalma|

## Çıktılar

| Parametre | Veri Türü | Çıktı Türü | Metafor Açıklaması   | Teknik Anlamı                |
| --------- | --------- | ----------- | ---------------------- | -------------------------------- |
| `sigmas`  | SIGMAS    | Output      | **Boya Tarifi Tablosu**: Adım adım kullanım için detaylı boya konsantrasyon listesi | Gürültü seviyesi dizisi, yayılım modelinin gürültü giderme sürecine rehberlik eder |

## Düğüm Rolü: Sanatçının Renk Karıştırma Asistanı

Kaotik bir boya karışımından (gürültü) net bir görüntü oluşturan bir sanatçı olduğunuzu hayal edin. `BasicScheduler`, **profesyonel renk karıştırma asistanınız** gibi davranır ve işi, bir dizi kesin boya konsantrasyonu tarifi hazırlamaktır:

### İş Akışı

- **Adım 1**: %90 konsantrasyonda boya kullan (yüksek gürültü seviyesi)
- **Adım 2**: %80 konsantrasyonda boya kullan
- **Adım 3**: %70 konsantrasyonda boya kullan
- **...**
- **Son Adım**: %0 konsantrasyon kullan (temiz tuval, gürültüsüz)

### Renk Asistanının Özel Becerileri

**Farklı karıştırma yöntemleri (zamanlayıcı)**:

- **"karras" karıştırma yöntemi**: Boya konsantrasyonu çok pürüzsüz değişir, profesyonel sanatçının degrade tekniği gibi
- **"exponential" karıştırma yöntemi**: Boya konsantrasyonu hızla azalır, hızlı oluşturma için uygun
- **"linear" karıştırma yöntemi**: Boya konsantrasyonu tekdüze şekilde azalır, kararlı ve kontrol edilebilir

**İnce kontrol (adımlar)**:

- **20 karıştırma**: Hızlı boyama, verimlilik öncelikli
- **50 karıştırma**: İnce boyama, kalite öncelikli

**Oluşturma yoğunluğu (gürültü giderme)**:

- **1.0 = Tamamen yeni oluşturma**: Tamamen boş tuvalden başla
- **0.5 = Yarı dönüşüm**: Orijinal resmin yarısını koru, yarısını dönüştür
- **0.2 = İnce ayar**: Orijinal resme sadece ince ayarlar yap

### Diğer Düğümlerle İş Birliği

`BasicScheduler` (Renk Asistanı) → Tarifi Hazırla → `SamplerCustom` (Sanatçı) → Gerçek Boyama → Tamamlanmış Eser
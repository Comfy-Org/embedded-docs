# Temel Zamanlayıcı

`BasicScheduler` düğümü, sağlanan zamanlayıcı, model ve gürültü giderme parametrelerine dayanarak difüzyon modelleri için bir dizi sigma değeri hesaplamak üzere tasarlanmıştır. Gürültü giderme (denoise) faktörüne bağlı olarak toplam adım sayısını dinamik olarak ayarlayarak difüzyon sürecini ince ayarlar ve hassas kontrol gerektiren gelişmiş örnekleme süreçlerinde (çok aşamalı örnekleme gibi) farklı aşamalar için hassas "tarifler" sağlar.

## Girişler

| Parametre | Metafor Açıklaması | Veri Türü | Giriş Türü | Varsayılan | Aralık | Teknik Amaç |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | **Tuval Türü**: Farklı tuval malzemeleri farklı boya formülleri gerektirir | MODEL | Giriş | - | - | Difüzyon modeli nesnesi, sigma hesaplama temelini belirler |
| `zamanlayıcı` | **Karıştırma Tekniği**: Boya konsantrasyonunun nasıl değişeceğini seçin | COMBO[STRING] | Widget | - | 9 seçenek | Zamanlama algoritması, gürültü azalma modunu kontrol eder |
| `adımlar` | **Karıştırma Sayısı**: 20 karıştırma ile 50 karıştırma arasındaki hassasiyet farkı | INT | Widget | 20 | 1-10000 | Örnekleme adımları, üretim kalitesini ve hızını etkiler |
| `gürültü_azaltma` | **Yaratım Yoğunluğu**: İnce ayardan yeniden boyamaya kadar kontrol seviyesi | FLOAT | Widget | 1.0 | 0.0-1.0 | Gürültü giderme gücü, kısmi yeniden boyama senaryolarını destekler |

### Zamanlayıcı Türleri

Kaynak kod `comfy.samplers.SCHEDULER_NAMES` temel alınarak aşağıdaki 9 zamanlayıcı desteklenir:

| Zamanlayıcı Adı       | Özellikler           | Kullanım Alanları                | Gürültü Azalma Modeli         |
| --------------------- | -------------------- | -------------------------------- | ----------------------------- |
| **normal**            | Standart doğrusal    | Genel senaryolar, dengeli        | Tekdüze azalma                |
| **karras**            | Yumuşak geçiş        | Yüksek kalite, detay zengini     | Yumuşak doğrusal olmayan azalma |
| **exponential**       | Üstel azalma         | Hızlı üretim, verimlilik         | Üstel hızlı azalma            |
| **sgm_uniform**       | SGM tekdüze          | Belirli model optimizasyonu      | SGM optimize azalma           |
| **simple**            | Basit zamanlama      | Hızlı test, temel kullanım       | Basitleştirilmiş azalma       |
| **ddim_uniform**      | DDIM tekdüze         | DDIM örnekleme optimizasyonu     | DDIM'e özgü azalma            |
| **beta**              | Beta dağılımı        | Özel dağılım ihtiyaçları         | Beta fonksiyonu azalması      |
| **linear_quadratic**  | Doğrusal ikinci derece| Karmaşık senaryo optimizasyonu  | İkinci derece fonksiyon azalması |
| **kl_optimal**        | KL optimal           | Teorik optimizasyon              | KL diverjansı optimize azalma |

## Çıktılar

| Parametre | Metafor Açıklaması | Veri Türü | Çıktı Türü | Teknik Anlamı |
| --- | --- | --- | --- | --- |
| `sigmas` | **Boya Tarifi Tablosu**: Adım adım kullanım için ayrıntılı boya konsantrasyonu listesi | SIGMAS | Çıktı | Gürültü seviyesi dizisi, difüzyon modelinin gürültü giderme sürecini yönlendirir |

## Düğümün Rolü: Sanatçının Renk Karıştırma Asistanı

Kendinizi, kaotik bir boya (gürültü) karışımından net bir görüntü oluşturan bir sanatçı olarak hayal edin. `BasicScheduler`, bir dizi hassas boya konsantrasyonu tarifi hazırlamakla görevli **profesyonel renk karıştırma asistanınız** gibi davranır:

### İş Akışı

- **Adım 1**: %90 konsantrasyonlu boya kullanın (yüksek gürültü seviyesi)
- **Adım 2**: %80 konsantrasyonlu boya kullanın
- **Adım 3**: %70 konsantrasyonlu boya kullanın
- **...**
- **Son Adım**: %0 konsantrasyon kullanın (temiz tuval, gürültü yok)

### Renk Asistanının Özel Yetenekleri

**Farklı karıştırma yöntemleri (zamanlayıcı)**:

- **"karras" karıştırma yöntemi**: Boya konsantrasyonu, profesyonel bir sanatçının gradyan tekniği gibi çok yumuşak bir şekilde değişir
- **"exponential" karıştırma yöntemi**: Boya konsantrasyonu hızla azalır, hızlı yaratım için uygundur
- **"linear" karıştırma yöntemi**: Boya konsantrasyonu eşit şekilde azalır, kararlı ve kontrol edilebilir

**Hassas kontrol (adımlar)**:

- **20 karıştırma**: Hızlı çizim, verimlilik öncelikli
- **50 karıştırma**: İnce çizim, kalite öncelikli

**Yaratım yoğunluğu (gürültü giderme)**:

- **1.0 = Tamamen yeni yaratım**: Tamamen boş bir tuvalden başlayın
- **0.5 = Yarı dönüşüm**: Orijinal resmin yarısını koruyun, yarısını dönüştürün
- **0.2 = İnce ayar**: Orijinal resimde yalnızca küçük ayarlamalar yapın

### Diğer Düğümlerle İş Birliği

`BasicScheduler` (Renk Asistanı) → Tarifi Hazırla → `SamplerCustom` (Sanatçı) → Gerçek Çizim → Tamamlanmış Eser

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/tr.md)

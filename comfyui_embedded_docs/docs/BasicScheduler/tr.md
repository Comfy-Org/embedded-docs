# Temel Zamanlayıcı

`BasicScheduler` düğümü, sağlanan zamanlayıcı, model ve gürültü giderme parametrelerine dayalı olarak difüzyon modelleri için bir sigma değerleri dizisi hesaplamak üzere tasarlanmıştır. Gürültü giderme faktörüne göre toplam adım sayısını dinamik olarak ayarlayarak difüzyon sürecini ince ayarlar ve hassas kontrol gerektiren gelişmiş örnekleme süreçlerindeki (çok aşamalı örnekleme gibi) farklı aşamalar için kesin "tarifler" sunar.

## Girdiler

| Parametre | Metafor Açıklaması | Veri Türü | Girdi Türü | Varsayılan | Aralık | Teknik Amaç |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | **Tuval Türü**: Farklı tuval malzemeleri farklı boya formülleri gerektirir | MODEL | Girdi | - | - | Difüzyon modeli nesnesi, sigma hesaplamasının temelini belirler |
| `zamanlayıcı` | **Karıştırma Tekniği**: Boya yoğunluğunun nasıl değişeceğini seçin | COMBO[STRING] | Widget | - | 9 seçenek | Zamanlama algoritması, gürültü azalma modunu kontrol eder |
| `adımlar` | **Karıştırma Sayısı**: 20 karışım ile 50 karışım arasındaki hassasiyet farkı | INT | Widget | 20 | 1-10000 | Örnekleme adımları, üretim kalitesini ve hızını etkiler |
| `gürültü_azaltma` | **Oluşturma Yoğunluğu**: İnce ayardan yeniden boyamaya kadar kontrol düzeyi | FLOAT | Widget | 1.0 | 0.0-1.0 | Gürültü giderme gücü, kısmi yeniden boyama senaryolarını destekler |

### Zamanlayıcı Türleri

Kaynak kodundaki `comfy.samplers.SCHEDULER_NAMES` temel alınarak aşağıdaki 9 zamanlayıcıyı destekler:

| Zamanlayıcı Adı | Özellikler | Kullanım Alanları | Gürültü Azalma Deseni |
| --- | --- | --- | --- |
| **normal** | Standart doğrusal | Genel senaryolar, dengeli | Tekdüze azalma |
| **karras** | Yumuşak geçiş | Yüksek kalite, ayrıntı zengini | Yumuşak doğrusal olmayan azalma |
| **exponential** | Üstel azalma | Hızlı üretim, verimlilik | Üstel hızlı azalma |
| **sgm_uniform** | SGM tekdüze | Belirli model optimizasyonu | SGM için optimize edilmiş azalma |
| **simple** | Basit zamanlama | Hızlı test, temel kullanım | Basitleştirilmiş azalma |
| **ddim_uniform** | DDIM tekdüze | DDIM örnekleme optimizasyonu | DDIM'e özgü azalma |
| **beta** | Beta dağılımı | Özel dağılım ihtiyaçları | Beta fonksiyonu azalması |
| **linear_quadratic** | Doğrusal ikinci dereceden | Karmaşık senaryo optimizasyonu | İkinci dereceden fonksiyon azalması |
| **kl_optimal** | KL optimal | Teorik optimizasyon | KL sapması için optimize edilmiş azalma |

## Çıktılar

| Parametre | Metafor Açıklaması | Veri Türü | Çıktı Türü | Teknik Anlam |
| --- | --- | --- | --- | --- |
| `sigmas` | **Boya Tarifi Tablosu**: Adım adım kullanım için ayrıntılı boya yoğunluğu listesi | SIGMAS | Çıktı | Gürültü seviyesi dizisi, difüzyon modelinin gürültü giderme sürecine rehberlik eder |

## Düğüm Rolü: Sanatçının Renk Karıştırma Asistanı

Kaotik bir boya karışımından (gürültü) net bir görüntü oluşturan bir sanatçı olduğunuzu hayal edin. `BasicScheduler`, görevi bir dizi kesin boya yoğunluğu tarifi hazırlamak olan **profesyonel renk karıştırma asistanınız** gibi davranır:

### İş Akışı

- **Adım 1**: %90 yoğunlukta boya kullanın (yüksek gürültü seviyesi)
- **Adım 2**: %80 yoğunlukta boya kullanın  
- **Adım 3**: %70 yoğunlukta boya kullanın
- **...**
- **Son Adım**: %0 yoğunluk kullanın (temiz tuval, gürültü yok)

### Renk Asistanının Özel Becerileri

**Farklı karıştırma yöntemleri (`scheduler`)**:

- **"karras" karıştırma yöntemi**: Boya yoğunluğu, profesyonel bir sanatçının gradyan tekniği gibi çok yumuşak değişir
- **"exponential" karıştırma yöntemi**: Boya yoğunluğu hızla azalır, hızlı oluşturma için uygundur
- **"linear" karıştırma yöntemi**: Boya yoğunluğu tekdüze azalır, kararlı ve kontrol edilebilir

**İnce kontrol (`steps`)**:

- **20 karışım**: Hızlı boyama, verimlilik öncelikli
- **50 karışım**: İnce boyama, kalite öncelikli

**Oluşturma yoğunluğu (`denoise`)**:

- **1.0 = Tamamen yeni oluşturma**: Tamamen boş tuvalden başlayın
- **0.5 = Yarı dönüşüm**: Orijinal resmin yarısını koruyun, yarısını dönüştürün
- **0.2 = İnce ayar**: Orijinal resimde yalnızca küçük ayarlamalar yapın

### Diğer Düğümlerle İş Birliği

`BasicScheduler` (Renk Asistanı) → Tarif Hazırla → `SamplerCustom` (Sanatçı) → Gerçek Boyama → Tamamlanmış Eser

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/tr.md)

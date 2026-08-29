# PixVerse V6 Füzyon (Referanstan Videoya)

PixVerse V6 Fusion (Reference to Video), PixVerse ile referans öznelerden, arka planlardan ve videolardan bir video oluşturur. İstemde referansı adıyla belirterek sahneye yerleştirin, örneğin '@Subject1 walks through @Background1'. Bir referans videosu bağlamak, modeli Omni moduna geçirir; bu modda çıktı uzunluğu en uzun referans videosuna eşit olur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model ve üretim ayarları. Modeli seçer ve üretim ayarlarını aşağıda görüntüler. Kullanılabilir tek seçenek "PixVerse V6"dır. | DYNAMIC_COMBO | Evet | "PixVerse V6" |

### PixVerse V6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için istem. Bağlı referanslara @Subject1, @Background1, @Video1 olarak başvurun. Varsayılan: boş. | STRING | Evet | 1 ila 5000 karakter |
| `aspect_ratio` | Çıktı en boy oranı. "auto" seçeneğine yalnızca en az bir referans videosu bağlandığında izin verilir. | COMBO | Evet | "auto"<br>ve PixVerse V6'nın ön tanımlı en boy oranları |
| `quality` | Çıktı çözünürlüğü. Uzun kenarı ayarlar: 360p 640px, 540p 1024px, 720p 1280px, 1080p 1920px. Varsayılan: "720p". | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Oluşturulan videonun saniye cinsinden uzunluğu. Referans videoları bağlandığında, çıktı uzunluğu bunun yerine en uzun referans videosunu izler ve bu ayar yok sayılır. Varsayılan: 5. | INT | Evet | 1 ila 15 |
| `generate_audio` | Video ile birlikte doğal bir ses parçası oluşturun. Varsayılan: True. | BOOLEAN | Evet | True<br>False |
| `seed` | Video üretimi için tohum. PixVerse bunu kaydeder ancak bu değerden bir üretimi yeniden oluşturmaz. Varsayılan: 42. | INT | Evet | 0 ila 2147483647 |
| `negative_prompt` | Videoda istenmeyen öğelerin isteğe bağlı metin açıklaması. Varsayılan: boş. | STRING | Hayır | En fazla 2048 karakter |
| `style` | Videonun tamamına uygulanan isteğe bağlı bir görsel stil. Varsayılan: "none". | COMBO | Hayır | "none"<br>ve PixVerse V6'nın ön tanımlı stilleri |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `özneler` | Genişletilebilir yuva: sahneye yerleştirilecek öznelerin referans görsellerini bağlayın. Yuvalar subject1'den subject8'e kadar adlandırılır; istemde bunlara @Subject1, @Subject2 vb. olarak başvurun. | IMAGE | Hayır | 0 ila 8 görsel |
| `arka planlar` | Genişletilebilir yuva: öznelerin yerleştirildiği sahnenin referans görsellerini bağlayın. Yuvalar background1'den background2'ye kadar adlandırılır; istemde bunlara @Background1, @Background2 olarak başvurun. | IMAGE | Hayır | 0 ila 2 görsel |
| `videolar` | Genişletilebilir yuva: özneler, hareket, çerçeveleme veya stil ödünç almak için referans videolarını bağlayın. Yuvalar video1'den video2'ye kadar adlandırılır; istemde bunlara @Video1, @Video2 olarak başvurun. Her video en fazla 15 saniye uzunluğunda olmalı ve toplam süre 15 saniyeyi aşmamalıdır. En az bir video bağlamak, düğümü Omni moduna geçirir. | VIDEO | Hayır | 0 ila 2 video<br>Her biri en fazla 15 saniye<br>Toplam 15 saniye |

Not: En az bir özne, arka plan veya referans videosu bağlayın. İstemdeki referans etiketleri (örneğin @Subject1, @Background1, @Video1) bağlı yuvalarla eşleşmelidir, aksi takdirde istek reddedilir. En az bir referans videosu bağlandığında (Omni modu), çıktı uzunluğu en uzun referans videosuna eşit olur, `duration_seconds` yok sayılır, `aspect_ratio` "auto" olarak ayarlanabilir ve en fazla 10 referans görseli kabul edilir. Referans videosu olmadan, en fazla 7 referans görseli (özneler ve arka planlar birlikte) kabul edilir ve "auto" en boy oranına izin verilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | PixVerse'ten indirilen oluşturulmuş füzyon videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`

# HeyGen Avatar 6 Identity to Video

Avatar 6 ile bir HeyGen avatarının konuşan videosunu oluşturun. Avatar 6'yı destekleyen yerleşik görünümlerden birini seçin veya kendi HeyGen avatar kimliğinizi yapıştırın, ardından avatarı bir metin betiği veya kendi sesinizle yönlendirin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"heygen-avatar-6-turbo"` daha ucuz, daha hızlı kademedir; her iki model de aynı girdileri ve çözünürlükleri kabul eder. | COMBO | Evet | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `avatar` | Sunulacak avatar görünümü. Avatar 6'yı destekleyen 19 yerleşik görünüm doğrudan listelenir; `custom avatar`, HeyGen'de oluşturduğunuz bir görünüm için `custom_avatar_id` alanını gösterir. | DYNAMIC_COMBO | Evet | 19 yerleşik görünüm<br>`custom avatar` |
| `konuşma` | Avatarı bir metin betiğiyle (HeyGen metinden konuşmaya) veya kendi sesinizle yönlendirin. Görünen ad: konuşma kaynağı. | DYNAMIC_COMBO | Evet | `"script"`<br>`"audio"` |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. Varsayılan: `"1080p"`. | COMBO | Evet | `"1080p"`<br>`"2k"` |
| `en_boy_oranı` | Çıktı videosunun en-boy oranı. `"auto"`, avatar görünümünün kendi görüntüsünü takip eder. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `hareket_istemi` | Hareketler, ifade, duruş ve kamera hareketi için isteğe bağlı yönlendirme. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `hareket_ifadeciliği` | `"less"` daha az ve daha küçük jestler sağlar. Hareket istemi, ikisinin çakıştığı yerlerde önceliklidir. Varsayılan: `"default"`. | COMBO | Evet | `"less"`<br>`"default"` |
| `tohum` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### `custom avatar` Girdileri

Bu girdiler `avatar` değeri `custom avatar` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `custom_avatar_id` | Avatar 6'yı destekleyen HeyGen avatar görünüm kimliği; örneğin HeyGen Create Avatar ile oluşturulmuş bir görünüm. Varsayılan: boş dize. | STRING | Evet | - |

### `script` Konuşma Girdileri

Bu girdiler `speech` değeri `"script"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Avatarın konuşacağı metin. Varsayılan: boş dize. | STRING | Evet | En fazla 5000 karakter |
| `voice` | Betik için ses. Varsayılan seçenek, HeyGen'in avatara atadığı sesi kullanır; HeyGen Create Avatar ile oluşturulan avatarlarda ses yoktur, bu nedenle onlar için bir ses seçin. | COMBO | Evet | `"(avatar's default voice)"` artı HeyGen'in genel ses listesi |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlandığında, yukarıda seçilen sesin üzerine yazar. Varsayılan: boş dize. | STRING | Hayır | - |
| `voice_speed` | Konuşma hızı çarpanı. Varsayılan: 1.0. | FLOAT | Hayır | 0.5 ile 1.5 arası (adım: 0.05) |

### `audio` Konuşma Girdileri

Bu girdiler `speech` değeri `"audio"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Avatar için konuşma. Video uzunluğu sesi takip eder. | AUDIO | Evet | 0.5 saniye ile 10 dakika arası |

**Kısıtlamalar ve davranış:**

* `custom avatar`, boş olmayan bir avatar kimliği gerektirir; aksi halde düğüm hata verir.
* Bir betik 5000 karakterle, ses ise 10 dakikayla sınırlıdır.
* Fiyatlandırma, çıktı videosunun saniyesi başına yapılır ve model ile çözünürlüğe bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan konuşan video; işleme tamamlandığında HeyGen'den indirilir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`

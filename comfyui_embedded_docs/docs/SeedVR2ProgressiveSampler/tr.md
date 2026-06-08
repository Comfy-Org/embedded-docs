# SeedVR2ProgressiveSampler

SeedVR2 yerel iş akışları için sıralı zamansal parça örnekleyici. Bu düğüm, uzun video gizil katmanlarını daha küçük zamansal parçalara bölerek, her parçayı sırayla örnekleyerek ve sonuçları birleştirerek işler. SeedVR2 modelleriyle, aksi takdirde bellek yetersizliği hatalarına neden olacak dizilerde çalışırken standart KSampler'ın doğrudan yerine kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Girdi gizil katmanını gürültüden arındırmak için kullanılan model | MODEL | Evet | |
| `seed` | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Evet | 0 ile 0xffffffffffffffff arası |
| `steps` | Gürültü giderme işleminde kullanılan adım sayısı (varsayılan: 20) | INT | Evet | 1 ile 10000 arası |
| `cfg` | Sınıflandırıcısız Kılavuzluk ölçeği, yaratıcılık ile istem bağlılığı arasındaki dengeyi ayarlar. Yüksek değerler istemle daha uyumlu görüntüler üretir ancak çok yüksek değerler kaliteyi olumsuz etkiler (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 arası |
| `sampler_name` | Örnekleme sırasında kullanılan algoritma; üretilen çıktının kalitesini, hızını ve stilini etkileyebilir | COMBO | Evet | Birden çok seçenek mevcut |
| `scheduler` | Zamanlayıcı, görüntüyü oluşturmak için gürültünün kademeli olarak nasıl kaldırılacağını kontrol eder | COMBO | Evet | Birden çok seçenek mevcut |
| `positive` | Görüntüye dahil etmek istediğiniz özellikleri tanımlayan koşullandırma | CONDITIONING | Evet | |
| `negative` | Görüntüden çıkarmak istediğiniz özellikleri tanımlayan koşullandırma | CONDITIONING | Evet | |
| `latent` | Gürültüden arındırılacak gizil katman görüntüsü | LATENT | Evet | |
| `denoise` | Uygulanan gürültü giderme miktarı; düşük değerler başlangıç görüntüsünün yapısını koruyarak görüntüden görüntüye örneklemeye olanak tanır (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `frames_per_chunk` | Zamansal parça başına piksel karesi. SeedVR2 kısıtlamalarına uymak için 4n+1 değeri olmalıdır (1, 5, 9, 13, 17, 21, ...) (varsayılan: 21) | INT | Evet | 1 ile 16384 arası (4'er adım) |
| `temporal_overlap` | Bitişik parçalar arasında birleştirilen gizil katman kareleri; dikiş izini gizlemek için kullanılır; 0 hiçbir birleştirme yapılmaz (varsayılan: 0) | INT | Evet | 0 ile 16384 arası |
| `chunking_mode` | manual = frames_per_chunk değerini tam olarak kullanır; auto = VRAM'e sığana kadar parçayı küçültür (varsayılan: "manual") | COMBO | Evet | "manual"<br>"auto" |

**`frames_per_chunk` hakkında not:** Bu parametre 4n+1 piksel-kare sayısı olmalıdır (1, 5, 9, 13, 17, 21, ...). Geçersiz bir değer girilirse düğüm hata verecektir.

**`temporal_overlap` hakkında not:** Birleştirme değeri, geçerli parça işlemeyi sağlamak için otomatik olarak gizil katman parça boyutundan en fazla bir eksik olacak şekilde sınırlandırılır.

**`chunking_mode` hakkında not:** "auto" olarak ayarlandığında, mevcut parça bellek yetersizliği hatasına neden olursa düğüm otomatik olarak daha küçük parça boyutlarını dener. Tüm denemeler başarısız olursa düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `latent` | Tüm zamansal parçalardan tek bir birleştirilmiş SeedVR2 gizil katman tensörüne birleştirilmiş, gürültüden arındırılmış gizil katman çıktısı | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/tr.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`

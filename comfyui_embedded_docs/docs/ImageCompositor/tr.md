# Katmanlı Görsel Oluştur

Bu düğüm, birden çok görüntü katmanını tek bir bileşik görüntüde birleştirir. Add Layer düğümüyle oluşturulmuş bir katman yığınını alır ve isteğe bağlı olarak compositor editöründen kaydedilmiş kompozisyon ayarlarını uygular; katmanları yerleşimlerine, boyutlarına, döndürmelerine, opaklıklarına ve karışım modlarına göre harmanlar. Geçerli girdilerle eşleşen kaydedilmiş bir kompozisyon öncelik alır; aksi halde düğüm katman özelliklerinden kompozisyon oluşturur ve kaydedilmiş durumu bayat olarak işaretler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `katmanlar` | Birleştirilecek katman yığını; Add Layer ile oluşturun. Öğeler z_index'e göre yığılır, bir öğe içindeki toplu kareler ardışık katmanlara genişler ve öğe yerleşimi, opaklığı ve karışım modu başlangıç kompozisyonunu tanımlar. Açık bir belge tuvali olmadan boyut, yerleştirilen katmanların en iyi çaba ile hesaplanan maksimum kapsamıdır. Geçerli girdilerle eşleşen kaydedilmiş bir kompozisyon öncelik alır. | LAYERS | Evet | Maksimum 50 katman |
| `kompozitör` | Compositor editörü tarafından kaydedilmiş katmanlı kompozisyon. | COMPOSITOR | Hayır | Yok |

**Kısıtlamalarla ilgili notlar:**

- Katman yığını en fazla 50 genişletilmiş katmanı destekler; daha fazlasını sağlamak hata verir.
- Şu anda yalnızca raster katman öğeleri desteklenir; diğer öğe türleri hata verir.
- `layers` belge sürümü 1 olmalıdır; diğer sürümler hata verir.
- Kaydedilmiş `compositor` durumu yalnızca kaydedilen girdi parmak izleri geçerli katman yığınıyla eşleştiğinde yeniden oynatılır. Eşleşmezlerse düğüm, katman özelliklerinden kompozisyon oluşturmaya geri döner ve kaydedilmiş durumu bayat olarak işaretler.
- Katman opaklığı 0.0 ile 1.0 aralığına sınırlandırılır.
- Katman yatay ve dikey yerleşimi (`x`, `y`) maksimum çözünürlük sınırına sınırlandırılır.
- Katman genişliği ve yüksekliği sıfır veya daha az olarak ayarlandığında doğal görüntü boyutuna geri döner ve maksimum çözünürlük sınırıyla sınırlandırılır.
- Birleştirilmiş tuval boyutu maksimum çözünürlük sınırını aşmamalıdır.
- Katman sağlanmadığında 64x64 yer tutucu görüntü döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Birleştirilmiş görüntü. Kompozitin saydam alanları olduğunda (örn. gizli arka plan) alfa kanalı taşır; aksi halde düz RGB'dir. | IMAGE |
| `MASK` | Kompozitin saydamlığı (1 = tamamen saydam). Kompozit opak olduğunda tamamen sıfırdır. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/tr.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`

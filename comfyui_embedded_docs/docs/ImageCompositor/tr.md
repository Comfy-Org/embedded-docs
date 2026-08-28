# ImageCompositor

Bu düğüm, birden fazla görüntü katmanını tek bir birleşik görüntüde birleştirir. Add Layer düğümüyle oluşturulmuş bir katman yığınını ve isteğe bağlı olarak kompozitör düzenleyiciden kaydedilmiş bir kompozisyonu alır; ardından katmanları yerleşim, boyut, dönüş, opaklık ve karışım modu ayarlarını kullanarak harmanlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `katmanlar` | Birleştirilecek katman yığını; Add Layer ile oluşturun. Öğeler z_index'e göre istiflenir, bir öğe içindeki batch kareleri ardışık katmanlara genişler ve öğe yerleşimi, opaklığı ve karışım modu ilk birleşimi tanımlar. Açık bir belge tuvali olmadığında boyut, yerleştirilen katmanların maksimum kapsamına göre belirlenir. Mevcut girdilerle eşleşen kaydedilmiş bir kompozisyon önceliklidir. | LAYERS | Evet | Maksimum 50 katman |
| `kompozitör` | Kompozitör düzenleyici tarafından kaydedilmiş katmanlı kompozisyon. | COMPOSITOR | Hayır | Yok |

**Kısıtlamalara ilişkin notlar:**

- Katman yığını en fazla 50 katmanı (genişletilmiş kareler) destekler; daha fazlası hata oluşturur.
- Şu anda yalnızca raster katmanlar desteklenmektedir; diğer katman öğesi türleri hata oluşturur.
- `layers` belge sürümü 1 olmalıdır; diğer sürümler hata oluşturur.
- Kaydedilmiş `compositor` durumu yalnızca, kaydedilmiş girdi parmak izleri mevcut katman yığınıyla eşleştiğinde yeniden oynatılır. Eşleşmezse, düğüm katman özelliklerinden birleştirme yapmaya geri döner ve kaydedilmiş durumu bayat olarak işaretler.
- Katman opaklığı 0.0 ile 1.0 aralığına sınırlandırılır.
- Katmanın yatay/dikey yerleşimi (`x`, `y`) maksimum çözünürlük sınırına sınırlandırılır.
- Katman genişliği ve yüksekliği sıfır veya daha az ayarlandığında doğal görüntü boyutuna geri döner ve maksimum çözünürlük sınırıyla sınırlandırılır.
- Birleştirilmiş tuval boyutu maksimum çözünürlük sınırını aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Birleştirilmiş görüntü. Birleşimde şeffaf alanlar olduğunda (örn. gizli arka plan) alfa kanalı taşır, aksi halde düz RGB. | IMAGE |
| `MASK` | Birleşimin şeffaflığı (1 = tamamen şeffaf). Birleşim opak olduğunda tümü sıfır. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/tr.md)

---
**Source fingerprint (SHA-256):** `1eca5c151b3737ccf76e6fd7a83cd1458b2acc314609753d597eec711bcf4bd8`

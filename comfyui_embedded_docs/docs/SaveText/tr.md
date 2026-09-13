# Metni Kaydet

Save Text düğümü, metin içeriğini çıktı dizinindeki bir dosyaya yazar. .txt, .csv, .md veya .json biçimlerinde kaydetmeyi destekler ve geçerli JSON sağlandığında JSON'u otomatik olarak okunaklı biçimde yazdırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Dosyaya kaydedilecek metin içeriği. Bu girdi başka bir düğüme bağlanmalıdır. | STRING | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek. Mevcut dosyaların üzerine yazılmasını önlemek için 5 haneli bir sayaç eklenir (varsayılan: "ComfyUI"). | STRING | Hayır | - |
| `format` | Metnin kaydedileceği dosya biçimi (varsayılan: "txt"). "json" seçildiğinde, geçerli JSON metni 2 boşluk girintisiyle okunaklı biçimde yazdırılır; aksi takdirde metin olduğu gibi kaydedilir. | COMBO | Hayır | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### Notlar

- `text` bağlantı zorunlu bir girdidir ve başka bir düğüme bağlanmalıdır; doğrudan yazılamaz.
- Kaydedilen dosya `<filename_prefix>_<5-digit counter>.<extension>` olarak adlandırılır ve ComfyUI çıktı dizinine (önekten türetilen bir alt klasöre) yazılır.
- `"json"` biçimini seçmek, metni JSON olarak ayrıştırmayı dener. Ayrıştırma başarılı olursa içerik 2 boşluk girintisiyle okunaklı biçimde yazılır; ayrıştırma başarısız olursa ham metin değiştirilmeden yazılır.
- Düğüm, kaydedilen dosyayı arayüze bildirir; böylece dosya, oluşturulan diğer çıktı dosyalarıyla birlikte görünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Dosyaya kaydedilen özgün metin içeriği | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/tr.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`

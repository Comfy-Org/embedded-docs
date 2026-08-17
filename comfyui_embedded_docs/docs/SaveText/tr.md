# Metni Kaydet

Save Text düğümü, çıktı dizinindeki bir dosyaya metin içeriği yazar. .txt, .csv, .md veya .json formatında kaydetmeyi destekler ve geçerli bir JSON sağlandığında otomatik olarak JSON'ın güzel biçimlendirilmesini (pretty-printing) yapar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Dosyaya kaydedilecek metin içeriği. Bu girdi başka bir düğümden bağlanmalıdır. | STRING | Evet | - |
| `filename_prefix` | Çıktı dosya adı için ön ek. Mevcut dosyaların üzerine yazılmasını önlemek için 5 haneli bir sayaç eklenir (varsayılan: "ComfyUI"). | STRING | Hayır | - |
| `format` | Metnin kaydedileceği dosya biçimi (varsayılan: "txt"). "json" seçildiğinde, geçerli JSON metni 2 boşluk girintili olarak güzel biçimlendirilir; aksi takdirde metin olduğu gibi kaydedilir. | COMBO | Hayır | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Dosyaya kaydedilen orijinal metin içeriği | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/tr.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`

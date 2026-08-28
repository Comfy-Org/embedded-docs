# Metni Kaydet

Save Text düğümü, metin içeriğini çıktı dizinindeki bir dosyaya yazar. .txt, .csv, .md veya .json formatında kaydetmeyi destekler ve geçerli JSON sağlandığında JSON'u otomatik olarak güzel biçimlendirir (pretty-printing).

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Dosyaya kaydedilecek metin içeriği. Bu girdi başka bir düğümden bağlanmalıdır. | STRING | Evet | - |
| `filename_prefix` | Çıktı dosya adı için önek. Mevcut dosyaların üzerine yazılmasını önlemek için 5 haneli bir sayaç eklenir (varsayılan: "ComfyUI"). | STRING | Hayır | - |
| `format` | Metnin kaydedileceği dosya biçimi (varsayılan: "txt"). "json" seçildiğinde, geçerli JSON metni 2 boşluklu girintiyle güzel biçimlendirilir; aksi takdirde metin olduğu gibi kaydedilir. | COMBO | Hayır | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Dosyaya kaydedilen orijinal metin içeriği | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/tr.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`

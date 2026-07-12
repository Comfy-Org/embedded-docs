# SaveText

## Genel Bakış

Save Text düğümü, metin içeriğini çıktı dizinindeki bir dosyaya yazar. .txt, .md veya .json formatında kaydetmeyi destekler ve geçerli bir JSON sağlandığında otomatik olarak JSON düzgün yazdırma işlemini gerçekleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Bir dosyaya kaydedilecek metin içeriği | STRING | Evet | - |
| `filename_prefix` | Çıktı dosya adı için ön ek (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `format` | Metnin kaydedileceği dosya biçimi (varsayılan: "txt") | STRING | Hayır | `"txt"`<br>`"md"`<br>`"json"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Dosyaya kaydedilen orijinal metin içeriği | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/tr.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`

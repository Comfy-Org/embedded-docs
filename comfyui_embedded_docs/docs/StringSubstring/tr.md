> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/tr.md)

StringSubstring düğümü, daha büyük bir metin dizesinden bir metin bölümü çıkarır. Çıkarmak istediğiniz bölümü tanımlamak için bir başlangıç konumu ve bitiş konumu alır ve bu iki konum arasındaki metni döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Alt dizenin çıkarılacağı giriş metin dizesi. Çok satırlı metni destekler. |
| `start` | INT | Evet | - | Alt dize için başlangıç konumu indeksi. İlk karakter 0 indeksindedir. |
| `end` | INT | Evet | - | Alt dize için bitiş konumu indeksi. Bu indeksteki karakter sonuca dahil edilmez. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | STRING | Giriş metninden çıkarılan alt dize; `start` konumundan başlayıp `end` konumuna kadar (ancak bu konum dahil değil) tüm karakterleri içerir. |

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`

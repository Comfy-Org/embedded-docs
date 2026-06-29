# Sözlüğü Metne Dönüştür

Bu düğüm, bir sözlüğü (anahtar-değer çiftleri koleksiyonu) genellikle JSON formatında bir metin dizisine dönüştürür. Çıktıyı daha okunabilir veya daha kompakt hale getirmek için girinti seviyesini kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `sözlük` | Dizgeye dönüştürülecek sözlük | DICT | Evet | - |
| `girinti` | Girinti seviyesi başına boşluk sayısı. 0 değeri, tek satırlık kompakt bir dize üretir (varsayılan: 2) | INT | Hayır | 0 ile 8 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | JSON formatlı bir dizgeye dönüştürülmüş sözlük | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertDictionaryToString/tr.md)

---
**Source fingerprint (SHA-256):** `ae4e9889d5347acfc69166bac66f2ba63f5cd37dafab25a9e0aff6bfe7381219`

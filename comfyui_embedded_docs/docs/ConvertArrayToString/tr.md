# Diziyi Metne Dönüştür

Dizi Metne Dönüştür düğümü, bir dizi (liste) öğeyi alır ve bunu biçimlendirilmiş bir JSON metnine dönüştürür. Bu, dizi verilerini görüntüleme, günlüğe kaydetme veya metin girişi bekleyen diğer sistemlere aktarma amacıyla serileştirmeniz gerektiğinde kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `dizi` | JSON metnine dönüştürülecek dizi | ARRAY | Evet | - |
| `girinti` | Girinti seviyesi başına boşluk sayısı. 0 değeri, tek satırlık sıkıştırılmış metin üretir (varsayılan: 2) | INT | Hayır | 0 ile 8 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `STRING` | JSON biçimli metne dönüştürülmüş dizi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertArrayToString/tr.md)

---
**Source fingerprint (SHA-256):** `ac8397fed0336f546403ee3e1f17d7e8f5973190b102e74943f098bf6905f726`

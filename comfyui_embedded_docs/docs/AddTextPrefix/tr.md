> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/tr.md)

Metin Ön Eki Ekle düğümü, her bir girdi metninin başına belirtilen bir dizeyi ekleyerek metni değiştirir. Metni ve bir ön eki girdi olarak alır ve birleştirilmiş sonucu döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | | Ön ekin ekleneceği metin. |
| `prefix` | STRING | Hayır | | Metnin başına eklenecek dize (varsayılan: ""). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | Ön ekin başına eklendiği sonuç metni. |

---
**Source fingerprint (SHA-256):** `7f1282b1b84ea06a96ecefdec8e9e684cb6e7d3e618250dfb6e54d01f9e9ba87`

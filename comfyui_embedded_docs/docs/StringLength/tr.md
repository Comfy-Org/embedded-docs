> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringLength/tr.md)

StringLength düğümü, bir metin dizisindeki karakter sayısını hesaplar. Herhangi bir metin girişini alır ve boşluklar ile noktalama işaretleri dahil olmak üzere toplam karakter sayısını döndürür. Bu, metin uzunluğunu ölçmek veya dizi boyutu gereksinimlerini doğrulamak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `string` | STRING | Evet | Yok | Uzunluğu ölçülecek metin dizisi. Çok satırlı girişi destekler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `length` | INT | Giriş dizisindeki boşluklar ve özel karakterler dahil toplam karakter sayısı. |

---
**Source fingerprint (SHA-256):** `dd72fac8330002e5e0ef2673ff208de36c6cf31aeec22a1c231495c742df62e3`

# Büyük/Küçük Harf Dönüştürücü

**Genel Bakış**

Case Converter düğümü, metin dizelerini farklı harf büyüklüğü biçimlerine dönüştürür. Bir girdi dizesi alır ve seçilen moda göre dönüştürerek, belirtilen büyüklük biçiminin uygulandığı bir çıktı dizesi üretir. Düğüm, metninizin büyük/küçük harf kullanımını değiştirmek için dört farklı büyüklük dönüştürme seçeneğini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `dize` | Farklı bir büyüklük biçimine dönüştürülecek metin dizesi | STRING | Evet | - |
| `mod` | Uygulanacak büyüklük dönüştürme modu (varsayılan: `"UPPERCASE"`) | STRING | Evet | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Belirtilen büyüklük biçimine dönüştürülmüş girdi dizesi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/tr.md)

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`

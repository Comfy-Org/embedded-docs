> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/tr.md)

**Genel Bakış**

Case Converter düğümü, metin dizelerini farklı harf büyüklüğü biçimlerine dönüştürür. Bir girdi dizesi alır ve seçilen moda göre dönüştürerek, belirtilen büyüklük biçiminin uygulandığı bir çıktı dizesi üretir. Düğüm, metninizin büyük/küçük harf kullanımını değiştirmek için dört farklı büyüklük dönüştürme seçeneğini destekler.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `dize` | STRING | Evet | - | Farklı bir büyüklük biçimine dönüştürülecek metin dizesi |
| `mod` | STRING | Evet | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` | Uygulanacak büyüklük dönüştürme modu (varsayılan: `"UPPERCASE"`) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | STRING | Belirtilen büyüklük biçimine dönüştürülmüş girdi dizesi |

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`

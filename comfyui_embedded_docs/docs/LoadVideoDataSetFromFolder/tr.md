# Video Yükle (Klasörden)

ComfyUI giriş dizinindeki seçili bir klasörden desteklenen tüm video dosyalarını yükler ve bunları bir video referansları listesi olarak döndürür. Bu düğüm, tembel (lazy) video referansları döndürür; bu nedenle kareler yalnızca başka bir düğüm bunlara gerçekten ihtiyaç duyduğunda çözülür. Desteklenen biçimler: MP4, AVI, MOV, WEBM, MKV ve FLV.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|-------|
| `folder` | Video dosyalarını içeren klasör. ComfyUI giriş dizinindeki mevcut alt klasörlerden seçin. | COMBO | Evet | ComfyUI giriş dizininde bulunan tüm alt klasörler |

**Not:** Seçilen klasör, desteklenen en az bir video dosyası içermelidir. Desteklenen uzantılar MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Desteklenen bir video dosyası bulunamazsa düğüm bir hata verir. Klasör, ComfyUI giriş dizini içinde bir konuma karşılık gelmelidir; dizinden kaçmaya çalışan klasör adları (örneğin ".." ile) bir hatayla reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `videos` | Seçilen klasördeki her video dosyası için bir tane olmak üzere tembel (lazy) video referansları listesi. Kareler yalnızca çıktı başka bir düğüm tarafından kullanıldığında çözülür. | VIDEO (liste) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`

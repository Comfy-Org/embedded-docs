# Video Yükle (Klasörden)

ComfyUI girdi dizini içindeki seçili klasörden desteklenen tüm video dosyalarını yükler ve bunları bir video referans listesi olarak döndürür. Bu düğüm tembel video referansları döndürür, bu nedenle kareler yalnızca başka bir düğüm gerçekten ihtiyaç duyduğunda çözülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|--------|
| `folder` | Video dosyalarını içeren klasör. ComfyUI girdi dizini içindeki mevcut alt klasörler arasından seçim yapın. | STRING | Evet | ComfyUI girdi dizininde bulunan tüm alt klasörler |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
**Not:** Seçilen klasör en az bir desteklenen video dosyası içermelidir. Desteklenen uzantılar MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Desteklenen video dosyası bulunamazsa düğüm bir hata oluşturur.
|-------------|-----------|-----------|
| `videos` | Seçili klasördeki her video dosyası için bir tane olmak üzere tembel video referanslarının listesi. Video kareleri yalnızca çıktı başka bir düğüm tarafından tüketildiğinde çözülür. | VIDEO (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`

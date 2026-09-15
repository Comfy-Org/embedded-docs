# Video Yükle (Klasörden)

ComfyUI girdi dizini içindeki seçili bir klasörden video veri kümesi yükler ve bunları tembel video referanslarından oluşan bir liste olarak döndürür. Bu düğüm bir video veri kümesi yükler: kareler yalnızca başka bir düğüm gerçekten ihtiyaç duyduğunda çözülür. Desteklenen biçimler MP4, AVI, MOV, WEBM, MKV ve FLV'dir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `folder` | Video dosyalarını içeren klasör. | COMBO | Evet | ComfyUI girdi dizininde bulunan tüm alt klasörler (dinamik olarak doldurulur) |

**Not:** Seçilen klasör, ComfyUI girdi dizininin bir alt klasörü olmalı ve en az bir desteklenen video dosyası içermelidir. Desteklenen uzantılar MP4, AVI, MOV, WEBM, MKV ve FLV'dir. Desteklenen video dosyası bulunamazsa veya klasör yolu girdi dizininin dışında bir konuma çözümlenirse, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `videos` | Seçili klasördeki desteklenen her video dosyası için bir tane olmak üzere tembel video referanslarından oluşan bir liste; dosya adına göre alfabetik olarak sıralanır. Video kareleri yalnızca çıktı başka bir düğüm tarafından kullanıldığında çözülür. | VIDEO (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`

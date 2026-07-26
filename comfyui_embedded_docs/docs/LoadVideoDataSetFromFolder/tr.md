# Video Yükle (Klasörden)

Belirtilen ComfyUI girdi dizinindeki bir klasörden video veri kümesi yükler. Düğüm, klasörü desteklenen video dosyaları için tarar ve tembel referanslar döndürür; gerçek kareler yalnızca aşağı akışta ihtiyaç duyulduğunda çözülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|--------|
| `folder` | Video dosyalarını içeren klasör. ComfyUI girdi dizini içindeki mevcut alt klasörler arasından seçim yapın. | STRING | Evet | *(girdi alt klasörlerinden doldurulur)* |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `videos` | Her dosya için bir tane olmak üzere tembel video referanslarının listesi. Video kareleri yalnızca çıktı başka bir düğüm tarafından tüketildiğinde çözülür. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`

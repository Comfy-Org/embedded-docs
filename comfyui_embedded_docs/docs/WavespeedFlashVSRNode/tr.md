> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/tr.md)

WavespeedFlashVSRNode, düşük çözünürlüklü veya bulanık görüntülerin çözünürlüğünü artıran ve netliğini geri kazandıran hızlı, yüksek kaliteli bir video yükselticidir. Bir video girdisini işler ve kullanıcı tarafından seçilen daha yüksek bir çözünürlükte yeni bir video çıktısı verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `video` | VIDEO | Evet | Yok | Yükseltilecek girdi video dosyası. Süresi 5 saniye ile 10 dakika arasında olan MP4 konteyner formatında olmalıdır. |
| `hedef_çözünürlük` | STRING | Evet | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` | Yükseltilmiş çıktı videosu için istenen çözünürlük. |

**Girdi Kısıtlamaları:**

* Girdi `video` dosyası MP4 konteyner formatında olmalıdır.
* Girdi `video` dosyasının süresi 5 saniye ile 10 dakika (600 saniye) arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Seçilen hedef çözünürlükte yükseltilmiş video dosyası. |

---
**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`

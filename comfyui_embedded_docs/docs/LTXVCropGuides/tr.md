# LTXVRehberleriKırp

LTXVCropGuides düğümü, ana kare bilgilerini kaldırarak ve gizli boyutları ayarlayarak video oluşturma için koşullandırma ve gizli girdileri işler. Gizli görüntüyü ve gürültü maskesini, ana kare bölümlerini hariç tutacak şekilde kırparken, hem pozitif hem de negatif koşullandırma girdilerinden ana kare indekslerini temizler. Bu, ana kare yönlendirmesi gerektirmeyen video oluşturma iş akışları için verileri hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturma için yönlendirme bilgisi içeren pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Oluşturmada kaçınılması gerekenler hakkında yönlendirme bilgisi içeren negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `gizli` | Görüntü örnekleri ve gürültü maskesi verilerini içeren gizli temsil | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Ana kare indeksleri ve kılavuz dikkat girişleri temizlenmiş, işlenmiş pozitif koşullandırma | CONDITIONING |
| `gizli` | Ana kare indeksleri ve kılavuz dikkat girişleri temizlenmiş, işlenmiş negatif koşullandırma | CONDITIONING |
| `gizli` | Ana kare bölümlerinin kaldırıldığı, ayarlanmış örnekler ve gürültü maskesi ile kırpılmış gizli temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`

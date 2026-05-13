> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

LTXVCropGuides düğümü, ana kare bilgilerini kaldırarak ve gizli boyutları ayarlayarak video oluşturma için koşullandırma ve gizli girdileri işler. Gizli görüntüyü ve gürültü maskesini, ana kare bölümlerini hariç tutacak şekilde kırparken, hem pozitif hem de negatif koşullandırma girdilerinden ana kare indekslerini temizler. Bu, ana kare yönlendirmesi gerektirmeyen video oluşturma iş akışları için verileri hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Oluşturma için yönlendirme bilgisi içeren pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | Oluşturmada kaçınılması gerekenler hakkında yönlendirme bilgisi içeren negatif koşullandırma girdisi |
| `latent` | LATENT | Evet | - | Görüntü örnekleri ve gürültü maskesi verilerini içeren gizli temsil |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Ana kare indeksleri ve kılavuz dikkat girişleri temizlenmiş, işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Ana kare indeksleri ve kılavuz dikkat girişleri temizlenmiş, işlenmiş negatif koşullandırma |
| `latent` | LATENT | Ana kare bölümlerinin kaldırıldığı, ayarlanmış örnekler ve gürültü maskesi ile kırpılmış gizli temsil |

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`

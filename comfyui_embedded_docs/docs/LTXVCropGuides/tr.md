> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

LTXVCropGuides düğümü, video üretimi için koşullandırma ve gizli girdileri işleyerek anahtar kare bilgilerini kaldırır ve gizli boyutları ayarlar. Gizli görüntüyü ve gürültü maskesini, anahtar kare bölümlerini hariç tutacak şekilde kırparken, hem pozitif hem de negatif koşullandırma girdilerinden anahtar kare indekslerini temizler. Bu, anahtar kare rehberliği gerektirmeyen video üretimi iş akışları için verileri hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Üretim için rehberlik bilgilerini içeren pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Üretim sırasında kaçınılması gerekenleri belirten rehberlik bilgilerini içeren negatif koşullandırma girdisi |
| `gizli` | LATENT | Evet | - | Görüntü örneklerini ve gürültü maskesi verilerini içeren gizli temsil |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Anahtar kare indeksleri temizlenmiş işlenmiş pozitif koşullandırma |
| `gizli` | CONDITIONING | Anahtar kare indeksleri temizlenmiş işlenmiş negatif koşullandırma |
| `gizli` | LATENT | Ayarlanmış örnekler ve gürültü maskesi ile kırpılmış gizli temsil |
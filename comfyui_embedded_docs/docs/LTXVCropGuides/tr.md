# LTXVRehberleriKırp

LTXVCropGuides düğümü, anahtar kare bilgilerini kaldırarak ve latent boyutlarını ayarlayarak video üretimi için koşullandırma ve latent girdilerini işler. Latent görüntüyü ve gürültü maskesini anahtar kare bölümlerini hariç tutacak şekilde kırpar ve hem pozitif hem de negatif koşullandırma girdilerindeki anahtar kare indekslerini temizler. Bu, anahtar kare rehberliği gerektirmeyen video üretim iş akışları için verileri hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretim için rehberlik bilgisi içeren pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | Üretimde kaçınılması gerekenler hakkında rehberlik bilgisi içeren negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `latent` | Görüntü örnekleri ve gürültü maskesi verilerini içeren latent temsil | LATENT | Evet | - |

Not: Pozitif koşullandırma anahtar kare indeksleri içermiyorsa, düğüm pozitif, negatif ve latent girdilerini değiştirmeden döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Anahtar kare indeksleri ve rehber dikkat kayıtları temizlenmiş, işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Anahtar kare indeksleri ve rehber dikkat kayıtları temizlenmiş, işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Anahtar kare bölümleri kaldırılmış, ayarlanmış örnekler ve gürültü maskesi içeren kırpılmış latent temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

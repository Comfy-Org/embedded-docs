# LTXVRehberleriKırp

LTXVCropGuides düğümü, anahtar kare bilgilerini kaldırarak ve latent boyutlarını ayarlayarak video üretimi için conditioning ve latent girdilerini işler. Anahtar kare bölümlerini hariç tutmak için latent görüntüyü ve gürültü maskesini kırpar; aynı zamanda hem pozitif hem de negatif conditioning girdilerinden anahtar kare indekslerini ve rehber dikkat kayıtlarını temizler. Bu, anahtar kare rehberliği gerektirmeyen video üretim iş akışları için verileri hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretim için rehberlik bilgisi içeren pozitif conditioning girdisi. Anahtar kare indeksleri, latentten kaç karenin kırpılacağını belirler. | CONDITIONING | Evet | - |
| `negatif` | Üretimde kaçınılması gerekenlere ilişkin rehberlik bilgisi içeren negatif conditioning girdisi. Anahtar kare verileri, pozitif conditioning ile birlikte temizlenir. | CONDITIONING | Evet | - |
| `gizli` | Görüntü örneklerini ve gürültü maskesi verilerini içeren latent temsil. Pozitif conditioning içinde anahtar kareler mevcut olduğunda, son anahtar kareye ait kareler hem örneklerden hem de gürültü maskesinden kaldırılır. | LATENT | Evet | - |

Not: Kırpma yalnızca pozitif conditioning anahtar kare indeksleri içerdiğinde gerçekleşir. Hiçbir anahtar kare tespit edilmezse, pozitif ve negatif conditioning, latent ile birlikte değiştirilmeden iletilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Anahtar kare indeksleri ve rehber dikkat kayıtları temizlenmiş işlenmiş pozitif conditioning | CONDITIONING |
| `negatif` | Anahtar kare indeksleri ve rehber dikkat kayıtları temizlenmiş işlenmiş negatif conditioning | CONDITIONING |
| `gizli` | Anahtar kare bölümlerinin kaldırıldığı, ayarlanmış örnekler ve gürültü maskesi içeren kırpılmış latent temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

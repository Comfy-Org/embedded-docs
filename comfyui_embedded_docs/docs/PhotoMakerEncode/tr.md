PhotoMakerEncode düğümü, yapay zeka görüntü oluşturma için koşullandırma verileri üretmek amacıyla görselleri ve metinleri işler. Bir referans görseli ve metin istemi alır, ardından referans görselin görsel özelliklerine dayanarak görüntü oluşturmayı yönlendirmek için kullanılabilecek gömmeler oluşturur. Düğüm, görsel tabanlı koşullandırmanın nereye uygulanacağını belirlemek için metinde özellikle "photomaker" tokenini arar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker` | Görseli işlemek ve gömmeler oluşturmak için kullanılan PhotoMaker modeli | PHOTOMAKER | Evet | - |
| `görüntü` | Koşullandırma için görsel özellikleri sağlayan referans görsel | IMAGE | Evet | - |
| `clip` | Metin tokenizasyonu ve kodlaması için kullanılan CLIP modeli | CLIP | Evet | - |
| `metin` | Koşullandırma oluşturma için metin istemi (varsayılan: "photograph of photomaker") | STRING | Evet | - |

**Not:** Metin "photomaker" kelimesini içerdiğinde, düğüm istemde bu konuma görsel tabanlı koşullandırma uygular. Metinde "photomaker" bulunamazsa, düğüm görsel etkisi olmadan standart metin koşullandırması oluşturur.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturmayı yönlendirmek için görsel ve metin gömmeleri içeren koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/tr.md)

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`

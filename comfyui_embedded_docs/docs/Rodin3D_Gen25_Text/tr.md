# Rodin 3D Gen-2.5 - Metinden 3D'ye

## Genel Bakış

Rodin Gen-2.5 API'sini kullanarak bir metin isteminden 3B model oluşturun. Oluşturma hızı ile çıktı kalitesi arasında denge kurmak için farklı kalite modları (Fast, Regular veya Extreme-High) arasından seçim yapabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | 3B model için metin istemi. | STRING | Evet | 1 ile 1024 karakter arası |
| `mod` | Oluşturma kalitesi ve hız modu. "Fast" en hızlısıdır, "Extreme-High" en yüksek kaliteyi üretir ancak daha uzun sürer. | COMBO | Evet | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `malzeme` | Oluşturulan 3B model için malzeme stili. | COMBO | Evet | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometri_dosya_formatı` | Çıktı 3B modeli için dosya biçimi. | COMBO | Evet | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `doku_modu` | Doku oluşturma modu. "None" doku üretmez, "Generated" standart dokular oluşturur, "Generated+HD" yüksek çözünürlüklü dokular oluşturur. | COMBO | Evet | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `tohum` | Tekrarlanabilir sonuçlar için rastgele tohum. Aynı tohumu aynı girdilerle kullanmak aynı çıktıyı üretir. | INT | Evet | 0 ile 2147483647 arası |
| `TAPose` | Oluşturulan modele T-pose (kollar yana açık) uygulanıp uygulanmayacağı. | BOOLEAN | Evet | True / False |
| `hd_doku` | Model için yüksek çözünürlüklü dokular oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | True / False |
| `doku_aydınlatma_kaldır` | Model için doku iyileştirme (geliştirilmiş doku kalitesi) uygulanıp uygulanmayacağı. | BOOLEAN | Evet | True / False |
| `eklenti_highpack` | Standart olana ek olarak modelin yüksek poligonlu bir sürümünün oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | True / False |
| `bbox_genişlik` | Sınırlayıcı kutunun dünya birimleri cinsinden genişliği. | INT | Evet | 1 ile 1000 arası |
| `bbox_yükseklik` | Sınırlayıcı kutunun dünya birimleri cinsinden yüksekliği. | INT | Evet | 1 ile 1000 arası |
| `bbox_uzunluk` | Sınırlayıcı kutunun dünya birimleri cinsinden uzunluğu. | INT | Evet | 1 ile 1000 arası |
| `yükseklik_cm` | Oluşturulan modelin santimetre cinsinden yüksekliği. | INT | Evet | 1 ile 300 arası |

**Not:** `prompt` parametresi 1 ile 1024 karakter arasında olmalıdır. `seed` parametresi belirtilmezse varsayılan olarak 0 (rastgele) değerini alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Belirtilen biçimde oluşturulan 3B model dosyası. | FILE3DANY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/tr.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`

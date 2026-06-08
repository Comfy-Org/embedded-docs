## Genel Bakış

Rodin Gen-2.5 API'sini kullanarak bir metin isteminden 3B model oluşturun. Üretim hızı ve çıktı kalitesini dengelemek için farklı kalite modları (Hızlı, Normal veya Aşırı Yüksek) arasından seçim yapabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Oluşturmak istediğiniz 3B modeli tanımlayan metin istemi. | STRING | Evet | Maksimum 2500 karakter |
| `mod` | Üretim kalitesi ve hız modu. "Hızlı" en hızlısıdır, "Aşırı Yüksek" en yüksek kaliteyi üretir ancak daha uzun sürer. | COMBO | Evet | `"Hızlı"`<br>`"Normal"`<br>`"Aşırı Yüksek"` |
| `malzeme` | Oluşturulan 3B model için malzeme stili. | COMBO | Evet | `"PBR"`<br>`"Mat"`<br>`"Parlak"` |
| `geometri_dosya_formatı` | Çıktı 3B modeli için dosya biçimi. | COMBO | Evet | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `doku_modu` | Doku oluşturma modu. "Yok" doku üretmez, "Oluşturuldu" standart dokular oluşturur, "Oluşturuldu+HD" yüksek çözünürlüklü dokular oluşturur. | COMBO | Evet | `"Yok"`<br>`"Oluşturuldu"`<br>`"Oluşturuldu+HD"` |
| `tohum` | Tekrarlanabilir sonuçlar için rastgele tohum değeri. Aynı girdilerle aynı tohum değerini kullanmak aynı çıktıyı üretecektir. | INT | Evet | 0 ile 2147483647 arası |
| `TAPose` | Oluşturulan modele T-pozu (kollar açık) uygulanıp uygulanmayacağı. | BOOLEAN | Evet | Doğru / Yanlış |
| `hd_doku` | Model için yüksek çözünürlüklü doku oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | Doğru / Yanlış |
| `doku_aydınlatma_kaldır` | Modele doku iyileştirmesi (gelişmiş doku kalitesi) uygulanıp uygulanmayacağı. | BOOLEAN | Evet | Doğru / Yanlış |
| `eklenti_highpack` | Standart modele ek olarak yüksek poligonlu bir sürüm oluşturulup oluşturulmayacağı. | BOOLEAN | Evet | Doğru / Yanlış |
| `bbox_genişlik` | Sınırlayıcı kutunun dünya birimleri cinsinden genişliği. | INT | Evet | 1 ile 1000 arası |
| `bbox_yükseklik` | Sınırlayıcı kutunun dünya birimleri cinsinden yüksekliği. | INT | Evet | 1 ile 1000 arası |
| `bbox_uzunluk` | Sınırlayıcı kutunun dünya birimleri cinsinden uzunluğu. | INT | Evet | 1 ile 1000 arası |
| `yükseklik_cm` | Oluşturulan modelin santimetre cinsinden yüksekliği. | INT | Evet | 1 ile 300 arası |

**Not:** `prompt` parametresi 1 ile 2500 karakter arasında olmalıdır. `seed` parametresi belirtilmezse varsayılan olarak 0 (rastgele) değerini alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Belirtilen biçimde oluşturulan 3B model dosyası. | FILE3DANY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/tr.md)

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`

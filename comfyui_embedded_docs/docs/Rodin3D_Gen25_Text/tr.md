> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/tr.md)

## Genel Bakış

Rodin Gen-2.5 API'sini kullanarak bir metin isteminden 3B model oluşturun. Üretim hızı ve çıktı kalitesini dengelemek için farklı kalite modları (Hızlı, Normal veya Aşırı Yüksek) arasından seçim yapabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | Maksimum 2500 karakter | Oluşturmak istediğiniz 3B modeli tanımlayan metin istemi. |
| `mod` | COMBO | Evet | `"Hızlı"`<br>`"Normal"`<br>`"Aşırı Yüksek"` | Üretim kalitesi ve hız modu. "Hızlı" en hızlısıdır, "Aşırı Yüksek" en yüksek kaliteyi üretir ancak daha uzun sürer. |
| `malzeme` | COMBO | Evet | `"PBR"`<br>`"Mat"`<br>`"Parlak"` | Oluşturulan 3B model için malzeme stili. |
| `geometri_dosya_formatı` | COMBO | Evet | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | Çıktı 3B modeli için dosya biçimi. |
| `doku_modu` | COMBO | Evet | `"Yok"`<br>`"Oluşturuldu"`<br>`"Oluşturuldu+HD"` | Doku oluşturma modu. "Yok" doku üretmez, "Oluşturuldu" standart dokular oluşturur, "Oluşturuldu+HD" yüksek çözünürlüklü dokular oluşturur. |
| `tohum` | INT | Evet | 0 ile 2147483647 arası | Tekrarlanabilir sonuçlar için rastgele tohum değeri. Aynı girdilerle aynı tohum değerini kullanmak aynı çıktıyı üretecektir. |
| `TAPose` | BOOLEAN | Evet | Doğru / Yanlış | Oluşturulan modele T-pozu (kollar açık) uygulanıp uygulanmayacağı. |
| `hd_doku` | BOOLEAN | Evet | Doğru / Yanlış | Model için yüksek çözünürlüklü doku oluşturulup oluşturulmayacağı. |
| `doku_aydınlatma_kaldır` | BOOLEAN | Evet | Doğru / Yanlış | Modele doku iyileştirmesi (gelişmiş doku kalitesi) uygulanıp uygulanmayacağı. |
| `eklenti_highpack` | BOOLEAN | Evet | Doğru / Yanlış | Standart modele ek olarak yüksek poligonlu bir sürüm oluşturulup oluşturulmayacağı. |
| `bbox_genişlik` | INT | Evet | 1 ile 1000 arası | Sınırlayıcı kutunun dünya birimleri cinsinden genişliği. |
| `bbox_yükseklik` | INT | Evet | 1 ile 1000 arası | Sınırlayıcı kutunun dünya birimleri cinsinden yüksekliği. |
| `bbox_uzunluk` | INT | Evet | 1 ile 1000 arası | Sınırlayıcı kutunun dünya birimleri cinsinden uzunluğu. |
| `yükseklik_cm` | INT | Evet | 1 ile 300 arası | Oluşturulan modelin santimetre cinsinden yüksekliği. |

**Not:** `prompt` parametresi 1 ile 2500 karakter arasında olmalıdır. `seed` parametresi belirtilmezse varsayılan olarak 0 (rastgele) değerini alır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | FILE3DANY | Belirtilen biçimde oluşturulan 3B model dosyası. |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`

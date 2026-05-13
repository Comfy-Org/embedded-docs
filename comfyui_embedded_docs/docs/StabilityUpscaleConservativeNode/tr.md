> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/tr.md)

## Genel Bakış

Görüntüyü minimum değişiklikle 4K çözünürlüğe yükseltir. Bu düğüm, Stability AI'nın koruyucu ölçekleme teknolojisini kullanarak görüntü çözünürlüğünü artırır, orijinal içeriği korur ve yalnızca ince ayarlamalar yapar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | Yükseltilecek giriş görüntüsü |
| `istem` | STRING | Evet | - | Çıktı görüntüsünde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir istem daha iyi sonuçlar sağlar. (varsayılan: boş dize) |
| `yaratıcılık` | FLOAT | Evet | 0.2-0.5 | Başlangıç görüntüsü tarafından yoğun şekilde koşullandırılmamış ek detaylar oluşturma olasılığını kontrol eder. (varsayılan: 0.35) |
| `tohum` | INT | Evet | 0-4294967294 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Çıktı görüntüsünde görmek istemediğiniz anahtar kelimeler. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `görüntü` | IMAGE | 4K çözünürlüğe yükseltilmiş görüntü |

---
**Source fingerprint (SHA-256):** `0a6eed22a37c1019ee97035bba70660b9619b0d65e443111d1d330968ded009a`

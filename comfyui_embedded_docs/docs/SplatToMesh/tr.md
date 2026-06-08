# Splat'tan Mesh Çıkarma

Bu düğüm, 3B Gauss splatını renkli bir mesh yüzeyine dönüştürür. Gaussian'ları bir yoğunluk ızgarasına rasterleştirerek, seçilen bir yoğunluk seviyesinde bir izo-yüzey çıkararak ve ardından isteğe bağlı yumuşatma ve temizleme uygulayarak temiz, renkli bir üçgen mesh üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|----------|--------|
| `splat` | Mesh'e dönüştürülecek giriş Gauss splatı | SPLAT | Evet | - |
| `çözünürlük` | En uzun eksen boyunca yoğunluk-ızgarası çözünürlüğü. Daha yüksek değerler daha ince yüzey detayı üretir ancak daha fazla VRAM ve işlem süresi gerektirir (resolution^3 ile büyür). Varsayılan: 384 | INT | Evet | 64 - 768 (adım 16) |
| `çekirdek` | Voksel cinsinden maksimum splat yarı genişliği. Her gaussian, kendi 3-sigma değerine göre boyutlandırılmış bir pencere üzerinde rasterleştirilir ve bu değerle sınırlandırılır. Küçük yüzey noktaları ucuz kalırken büyük olanlar kesilmez. Seyrek splat'lar boşluk bırakıyorsa yükseltin. Varsayılan: 5 | INT | Evet | 1 - 8 |
| `yumuşatma` | Taubin mesh yumuşatma iterasyonları. Yüzeyi küçültmeden yumuşatır (hacim koruyucu), yoğunluğu bulanıklaştırmanın aksine. 0 yumuşatma yapılmaz. Varsayılan: 0 | INT | Evet | 0 - 60 |
| `seviye` | İzo-yüzey seviyesi. Otsu eşikleme ile otomatik seçilir; bu değer otomatik seçimi yönlendirir (1.0 = otomatik, daha düşük değerler daha şişman/daha bağlantılı yüzeyler, daha yüksek değerler daha ince/daha sıkı yüzeyler üretir). Varsayılan: 0.4 | FLOAT | Evet | 0.0 - 2.0 (adım 0.01) |
| `min_bileşen` | Bu sayıdan daha az köşe noktasına sahip bağlı bileşenleri atar. Ayrılmış yüzen kümeleri ve çift duvarların iç kabuğunu temizler. 0 tüm bileşenleri korur. Varsayılan: 500 | INT | Evet | 0 - 100000 (adım 50) |
| `min_opaklık` | Mesh oluşturmadan önce bu değerden daha soluk olan gaussian'ları yok sayar. Varsayılan: 0.02 | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `renk_keskinleştirme` | Köşe noktası dokusunu keskinleştirir. 1.0 fiziksel olarak doğru karışımı verir; daha yüksek değerler her vokselin rengini komşuları ortalamak yerine baskın gaussian'ına doğru yönlendirir (dokuyu yaymaz). Yalnızca rengi etkiler, geometriyi etkilemez. Varsayılan: 2.0 | FLOAT | Evet | 1.0 - 8.0 (adım 0.5) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `mesh` | Splat görünümüyle eşleşmesi için ışıksız (emisif benzeri) işleme ile çıkarılmış renkli mesh | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `5a7060c26252b587ce533e5682abe880a6fcc83f6671232489c3de64b094cd84`

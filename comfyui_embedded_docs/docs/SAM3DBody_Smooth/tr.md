# SAM3D Gövde Poz Verilerini Yumuşat

Smooth SAM3D Body Pose Data, bir 3B gövde poz dizisinde kareler arası titremeyi zaman içinde hareketi ortalayarak azaltır. Kamera ve görünüm verileri tamamen yumuşatılır; özne hızlı döndüğünde ağ geometrisi daha az yumuşatılır, böylece hızlı dönüşler düzleştirilmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | Yumuşatılacak MHR poz verisi dizisi; model parametreleri, şekil parametreleri, ifade parametreleri, MHR70 anahtar nokta düzeni ve ilgili ağ verilerini içerir. | MHR_POSE_DATA | Evet | — |
| `güç` | Yumuşatma gücü. 0 = ham, 1 = yumuşatılmış. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.05) |
| `yöntem` | gaussian: simetrik ağırlıklı ortalama, en iyi genel amaçlı yumuşatıcı.<br>savgol: kayan polinom uyumu, keskin zirveleri korur. (varsayılan: "savgol") | COMBO | Evet | "gaussian"<br>"savgol" |
| `pencere` | Kare cinsinden zamansal pencere (tek değerler). (varsayılan: 7) | INT | Evet | 1 - 51 (tek değerler, adım 2) |
| `rotation_threshold_degrees` | Hızlı dönüşleri korumak için bu kök dönüş hızında (derece/kare) yumuşatmayı devre dışı bırakır. 30° çoğu içerik için uygundur; düşük değerler sıradan titremelerde yumuşatmayı devre dışı bırakabilir ve kaliteyi sessizce etkiler. 0 = devre dışı. (varsayılan: 30.0) | FLOAT | Evet | 0.0 - 90.0 (adım 1.0) |

Not: `strength` 0.0 veya daha düşük olduğunda ya da `window` 1 veya daha düşük olduğunda, düğüm girdi verilerini değiştirmeden döndürür. Girdi en az 2 kare ve anahtar nokta verisi içermelidir; aksi takdirde düğüm girdi verilerini değiştirmeden döndürür. `rotation_threshold_degrees` 0.0 olduğunda, dönüş tabanlı yumuşatma geri çekilmesi devre dışı bırakılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mhr_pose_data` | Kareler arası titremesi azaltılmış yumuşatılmış MHR poz verisi dizisi. | MHR_POSE_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/tr.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`

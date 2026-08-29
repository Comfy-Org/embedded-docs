# SAM3D Gövde Poz Verilerini Yumuşat

Smooth SAM3D Body Pose Data, 3D vücut poz dizilerindeki çerçeveden çerçeveye titremeyi, hareketi zaman içinde ortalamasını alarak azaltır. Kamera ve görünüm verilerine tam yumuşatma uygular; özne hızla döndüğünde ise mesh geometrisi üzerindeki yumuşatmayı azaltır, böylece hızlı dönüşler düzleştirilmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | Yumuşatılacak MHR poz verisi dizisi; model parametrelerini, şekil parametrelerini, ifade parametrelerini, MHR70 anahtar nokta düzenini ve ilgili mesh verilerini içerir. | MHR_POSE_DATA | Evet | — |
| `güç` | Yumuşatma gücü. 0 = ham, 1 = yumuşatılmış. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (adım 0.05) |
| `yöntem` | gaussian: simetrik ağırlıklı ortalama, genel amaçlı en iyi yumuşatıcı.<br>savgol: kayan polinom uyumu, keskin tepeleri korur. (varsayılan: "savgol") | COMBO | Evet | "gaussian"<br>"savgol" |
| `pencere` | Çerçeve cinsinden zamansal pencere (tek değerler). (varsayılan: 7) | INT | Evet | 1 ile 51 (tek değerler, adım 2) |
| `rotation_threshold_degrees` | Bu kök dönüş hızı (derece/çerçeve) için yumuşatmayı devre dışı bırakarak hızlı dönüşleri korur. 30° çoğu içerik için uygundur; düşük değerler sıradan titremelerde yumuşatmayı devre dışı bırakabilir ve kaliteyi sessizce etkileyebilir. 0 = devre dışı. (varsayılan: 30.0) | FLOAT | Evet | 0.0 ile 90.0 (adım 1.0) |

Not: `strength` 0.0 veya daha düşük olduğunda ya da `window` 1 veya daha düşük olduğunda, düğüm girdi verilerini değiştirmeden döndürür. Girdi en az 2 çerçeve ve anahtar nokta verisi içermelidir; aksi takdirde düğüm girdi verilerini değiştirmeden döndürür. `rotation_threshold_degrees` 0.0 olduğunda, rotasyon tabanlı yumuşatma geri çekilmesi devre dışı bırakılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mhr_pose_data` | Çerçeveden çerçeveye titremesi azaltılmış, yumuşatılmış MHR poz verisi dizisi. | MHR_POSE_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/tr.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`

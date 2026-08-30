# Yüz İfadesini SAM3D Body'ye Dönüştür

Bu düğüm, MediaPipe Face Landmarker ile bir görüntüdeki yüzleri algılayıp, algılanan her yüzü izlenen bir kişiyle eşleştirerek ve 52 ARKit blendshape'ini MHR'nin 72 eksenli ifade parametrelerine eşleyerek SAM3D gövdesine yüz ifadeleri ekler. Ardından gövde modelini yeniden çalıştırarak çıktı mesh köşelerinin ve anahtar noktalarının yeni ifadeyle eşleşmesini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | Yüzleri algılamak ve gövde mesh'ini yeniden oluşturmak için kullanılan yüz noktası detektörünü içeren SAM3D gövde modeli. | SAM3D_BODY_MODEL | Evet | - |
| `mhr_pose_data` | Sınırlayıcı kutular, anahtar noktalar ve ifade parametreleriyle birlikte kare başına izlenen kişileri içeren poz verisi. Düğüm, algılanan her yüzü bir kişiyle eşleştirir ve güncellenmiş ifade parametrelerini bu veriye yazar. | MHR_POSE_DATA | Evet | - |
| `image` | Yüzleri algılamak için kullanılan görüntü kareleri. Görüntü kümesi, poz verisinden daha az kare içeriyorsa, kalan kareler için son kare yeniden kullanılır. | IMAGE | Evet | - |
| `strength` | Tüm blendshape'ler üzerinde genel çarpan. >1 abartır. Varsayılan: 1.0. | FLOAT | Hayır | 0.0 ila 4.0 (adım 0.05, varsayılan 1.0) |
| `mouth_strength` | Ağız/çene şekilleri üzerinde çarpan. MediaPipe'ın jawOpen değeri 1.0'a yakın doygunluğa ulaşır. Varsayılan: 1.0. | FLOAT | Hayır | 0.0 ila 4.0 (adım 0.05, varsayılan 1.0) |
| `eye_strength` | Göz şekilleri üzerinde çarpan. MediaPipe nadiren 0.5'i aşar; genellikle 2-3x gerekir. Varsayılan: 2.0. | FLOAT | Hayır | 0.0 ila 4.0 (adım 0.05, varsayılan 2.0) |
| `brow_strength` | Kaş/yanak/sneer şekilleri üzerinde çarpan. MediaPipe ~0.1-0.3 çıktısı verir; 2-3x. Varsayılan: 2.0. | FLOAT | Hayır | 0.0 ila 4.0 (adım 0.05, varsayılan 2.0) |
| `input_threshold` | MediaPipe'ın ham çıktısındaki ölü bölge (altı = sıfır, üstü = doğrusal yeniden eşleme). Varsayılan: 0.02. | FLOAT | Hayır | 0.0 ila 0.5 (adım 0.01, varsayılan 0.02) |
| `blendshape_smooth_window` | MHR eşlemesinden önce MediaPipe'ın kare başına sinyaline uygulanan Gauss penceresi. MediaPipe'ın ham çıktısı, sabit yüzlerde kareden kareye %30-70 oranında dalgalanır. 1 = devre dışı. Tek değerler kullanın. Varsayılan: 7. | INT | Hayır | 1 ila 31 (adım 2, varsayılan 7) |

Not: Klip başına temel çizgi çıkarma, yalnızca klipte en az 30 kare algılanan kişiler içerdiğinde uygulanır. Kişi başına 12 kareye kadar olan algılama boşlukları enterpolasyonla doldurulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mhr_pose_data` | Güncellenmiş poz verisi. Her izlenen kişinin ifade parametreleri, eşlenen yüz ifadesiyle değiştirilir ve mesh köşeleri ile anahtar noktalar eşleşecek şekilde yeniden oluşturulur. | MHR_POSE_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/tr.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`

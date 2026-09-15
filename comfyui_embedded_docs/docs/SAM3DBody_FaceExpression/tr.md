# Yüz İfadesini SAM3D Body'ye Dönüştür

Bu düğüm, bir görüntüdeki yüzleri MediaPipe Face Landmarker ile algılayarak, algılanan her yüzü izlenen bir kişiyle eşleştirerek ve 52 ARKit blendshape'ini MHR'nin 72 eksenli ifade parametrelerine eşleyerek bir SAM3D gövdesine yüz ifadeleri ekler. Ardından, çıktı mesh köşeleri ve anahtar noktaları yeni ifadeyi yansıtacak şekilde gövde modelini yeniden çalıştırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | Yüzleri algılamak ve gövde mesh'ini yeniden oluşturmak için kullanılan yüz landmark algılayıcısını içeren SAM3D gövde modeli. | SAM3D_BODY_MODEL | Evet | - |
| `mhr_pose_data` | Sınırlayıcı kutular, anahtar noktalar ve ifade parametreleriyle birlikte kare başına izlenen kişileri içeren poz verisi. Düğüm, algılanan her yüzü bir kişiyle eşleştirir ve güncellenmiş ifade parametrelerini bu veriye yazar. | MHR_POSE_DATA | Evet | - |
| `image` | Yüzleri algılamak için kullanılan görüntü kareleri. Görüntü partisi poz verisinden daha az kareye sahipse, kalan kareler için son kare yeniden kullanılır. | IMAGE | Evet | - |
| `strength` | Tüm blendshape'ler üzerinde genel çarpan. >1 abartır. Varsayılan: 1.0. | FLOAT | Hayır | 0.0 ile 4.0 (step 0.05, default 1.0) |
| `mouth_strength` | Ağız/çene şekilleri üzerinde çarpan. MediaPipe'ın jawOpen değeri 1.0 civarında doyuma ulaşır. Varsayılan: 1.0. | FLOAT | Hayır | 0.0 ile 4.0 (step 0.05, default 1.0) |
| `eye_strength` | Göz şekilleri üzerinde çarpan. MediaPipe nadiren 0.5'i aşar; sıklıkla 2-3 kat gerekir. Varsayılan: 2.0. | FLOAT | Hayır | 0.0 ile 4.0 (step 0.05, default 2.0) |
| `brow_strength` | Kaş/yanak/küçümseme şekilleri üzerinde çarpan. MediaPipe ~0.1-0.3 çıktı verir; 2-3 kat. Varsayılan: 2.0. | FLOAT | Hayır | 0.0 ile 4.0 (step 0.05, default 2.0) |
| `input_threshold` | MediaPipe'ın ham çıktısındaki ölü bölge (altında = sıfır, üstünde = doğrusal yeniden eşleme). Varsayılan: 0.02. | FLOAT | Hayır | 0.0 ile 0.5 (step 0.01, default 0.02) |
| `blendshape_smooth_window` | MHR eşlemesinden önce MediaPipe'ın kare başına sinyali üzerinde Gauss penceresi. MediaPipe'ın ham çıktısı statik yüzlerde kareden kareye %30-70 salınır. 1 = devre dışı. Tek değerler kullanın. Varsayılan: 7. | INT | Hayır | 1 ile 31 (step 2, default 7) |

Not: Klip başına baseline çıkarma yalnızca klipteki en az 30 kare algılanan kişi içerdiğinde uygulanır. Kişi başına 12 kareye kadar olan algılama boşlukları interpolasyonla doldurulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mhr_pose_data` | Güncellenmiş poz verisi. İzlenen her kişinin ifade parametreleri eşlenen yüz ifadesiyle değiştirilir ve mesh köşeleri ile anahtar noktalar buna uyacak şekilde yeniden oluşturulur. | MHR_POSE_DATA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/tr.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`

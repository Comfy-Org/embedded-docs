> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/tr.md)

Kling Kamera Kontrolleri düğümü, video oluşturmada hareket kontrol efektleri yaratmak için çeşitli kamera hareketi ve dönüş parametrelerini yapılandırmanıza olanak tanır. Farklı kamera hareketlerini simüle etmek için kamera konumlandırma, dönüş ve yakınlaştırma kontrolleri sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `kamera_kontrol_türü` | COMBO | Evet | Birden fazla seçenek mevcut | Kullanılacak kamera kontrol yapılandırma türünü belirtir |
| `yatay_hareket` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın yatay eksende (x-ekseni) hareketini kontrol eder. Negatif sola, pozitif sağa hareketi belirtir (varsayılan: 0.0) |
| `dikey_hareket` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın dikey eksende (y-ekseni) hareketini kontrol eder. Negatif aşağı, pozitif yukarı hareketi belirtir (varsayılan: 0.0) |
| `kaydırma` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın dikey düzlemde (x-ekseni) dönüşünü kontrol eder. Negatif aşağı, pozitif yukarı dönüşü belirtir (varsayılan: 0.5) |
| `eğme` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın yatay düzlemde (y-ekseni) dönüşünü kontrol eder. Negatif sola, pozitif sağa dönüşü belirtir (varsayılan: 0.0) |
| `yuvarlanma` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın yuvarlanma miktarını (z-ekseni) kontrol eder. Negatif saat yönünün tersine, pozitif saat yönünde dönüşü belirtir (varsayılan: 0.0) |
| `yakınlaştırma` | FLOAT | Hayır | -10.0 ile 10.0 arası | Kameranın odak uzunluğundaki değişimi kontrol eder. Negatif daha dar görüş alanını, pozitif daha geniş görüş alanını belirtir (varsayılan: 0.0) |

**Not:** Yapılandırmanın geçerli olması için kamera kontrol parametrelerinden (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` veya `zoom`) en az birinin sıfır olmayan bir değere sahip olması gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `camera_control` | CAMERA_CONTROL | Video oluşturmada kullanılmak üzere yapılandırılmış kamera kontrol ayarlarını döndürür |
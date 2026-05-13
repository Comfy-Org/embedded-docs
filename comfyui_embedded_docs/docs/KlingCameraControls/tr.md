> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/tr.md)

Kling Kamera Kontrolleri düğümü, video oluşturmada hareket kontrol efektleri oluşturmak için çeşitli kamera hareketi ve dönüş parametrelerini yapılandırmanıza olanak tanır. Farklı kamera hareketlerini simüle etmek için kamera konumlandırma, dönüş ve yakınlaştırma kontrolleri sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `kamera_kontrol_türü` | COMBO | Evet | `"simple"`<br>`"advanced"` | Kullanılacak kamera kontrol yapılandırmasının türünü belirtir |
| `yatay_hareket` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın yatay eksen (x ekseni) boyunca hareketini kontrol eder. Negatif değer sola, pozitif değer sağa hareketi belirtir (varsayılan: 0,0) |
| `dikey_hareket` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın dikey eksen (y ekseni) boyunca hareketini kontrol eder. Negatif değer aşağı, pozitif değer yukarı hareketi belirtir (varsayılan: 0,0) |
| `kaydırma` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın dikey düzlemdeki (x ekseni) dönüşünü kontrol eder. Negatif değer aşağı, pozitif değer yukarı dönüşü belirtir (varsayılan: 0,5) |
| `eğme` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın yatay düzlemdeki (y ekseni) dönüşünü kontrol eder. Negatif değer sola, pozitif değer sağa dönüşü belirtir (varsayılan: 0,0) |
| `yuvarlanma` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın yuvarlanma miktarını (z ekseni) kontrol eder. Negatif değer saat yönünün tersine, pozitif değer saat yönünde dönüşü belirtir (varsayılan: 0,0) |
| `yakınlaştırma` | FLOAT | Hayır | -10,0 ila 10,0 | Kameranın odak uzaklığındaki değişimi kontrol eder. Negatif değer daha dar, pozitif değer daha geniş görüş alanını belirtir (varsayılan: 0,0) |

**Not:** Yapılandırmanın geçerli olması için kamera kontrol parametrelerinden (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` veya `zoom`) en az birinin sıfır olmayan bir değere sahip olması gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `camera_control` | CAMERA_CONTROL | Video oluşturmada kullanılmak üzere yapılandırılmış kamera kontrol ayarlarını döndürür |

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`

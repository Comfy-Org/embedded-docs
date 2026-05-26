> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa katkıda bulunmaktan çekinmeyin. [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/tr.md)

## Genel bakış

MultiGPU CFG Split düğümü, difüzyon işlemini aynı bilgisayarda bulunan birden fazla GPU arasında paylaştırır. Hız artışı workflow'a göre değişir, ancak yaygın workflow'larda 1.95x'e kadar hızlanma ölçülmüştür.

## Önemli ayrıntılar

Farklı GPU türlerini karıştırmak desteklenmez. Kurulu GPU'ların aynı olması gerekir; örneğin 2x 5090 veya 2x 5080.

ComfyUI açılışta birden fazla kurulu GPU'yu otomatik olarak algılar.

## Desteklenen GPU'lar

Ampere veya daha yeni mimariye sahip, aynı türden iki GPU içeren tüm kurulumlar desteklenir; örneğin 2 x 3090 veya 2 x RTX6000 Pro.

## Desteklenen modeller

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - temel sürümler  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | MODEL | Evet | N/A | Örnekleme öncesinde MultiGPU CFG Split ile hazırlanacak model. |
| `max_gpus` | INT | Evet | Minimum: 1<br>Adım: 1<br>Varsayılan: 2 | Yükü bölmek için kullanılacak aynı türdeki GPU sayısının üst sınırı. Bu değeri sisteminizde kurulu eşleşen GPU sayısına göre ayarlayın. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `MODEL` | MODEL | MultiGPU CFG Split için hazırlanmış, hızlandırılmış örnekleme için hazır model. |

## Düğüm yerleşimi ve workflow notları

![image1.png](./asset/image1.png)

`max_gpus` alanı, sistemde kurulu aynı türdeki GPU'ların en yüksek sayısına göre ayarlanmalıdır.

**Düğüm yerleşimi:** MultiGPU CFG Split, Model Load düğümü ile Sampling düğümü arasına yerleştirilmelidir. Model yükleyicinin model çıkışına başka düğümler bağlıysa, MultiGPU CFG Split bu zincirde Sampling düğümünden önceki son düğüm olmalıdır.

![image2.png](./asset/image2.png)

**Workflow gereksinimleri:** Bu düğüm difüzyon workflow'unu CFG seviyesinde böler. Bu nedenle workflow içindeki CFG değeri 1'den büyük olmalıdır. CFG = 1 gerektiren distilled workflow'lar, MultiGPU CFG Split ile birden fazla GPU kullandığında performans kazancı göstermez.

## Çoklu GPU kullanımını doğrulama

MultiGPU CFG Split açık bir workflow çalıştırırken Windows Görev Yöneticisi'ni açıp performans kategorisini seçebilirsiniz.

![image3.webp](./asset/image3.webp)  
![image4.png](./asset/image4.png)

Workflow içinde sampler çalışırken kurulu iki GPU'da da etkinlik görmelisiniz.

## Bilinen sorunlar

Henüz netleştirilmedi.

## Örnek çoklu GPU workflow'u: (Wan 2.2 FP8)

[https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link](https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`

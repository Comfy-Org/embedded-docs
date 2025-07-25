这一节点将使用特定算法对潜空间图像进行缩放，它允许调整放大比例和放大方法，提供在提高潜在样本分辨率方面的灵活性。

### 关于upscale_method中几个方法的说明介绍

| 算法名称 | 描述 |
| --- | --- |
| Nearest-Exact (最近邻) | 最简单的插值方法，选取离目标像素最近的已知像素点的颜色作为该点颜色。在放大时会导致锯齿和块状效果，但计算速度快。 |
| Bilinear Interpolation（双线性插值） | 对于每个目标像素，基于其周围4个相邻像素的灰度值进行线性内插。能够提供更平滑的结果，特别是在图像缩放时改善了视觉质量，但可能仍保留轻微的块效应。 |
| Area Interpolation（区域插值） | 基于像素面积关系重采样（抗锯齿），计算目标像素值时考虑贡献源像素的面积。减少aliasing失真，适合保留精细细节|
| Bicubic Interpolation（双三次插值） | 双三次插值，使用三次多项式根据16个最近源像素计算像素值，提供更平滑的过渡和更好的细节保留，适用于高质量图像缩放。 |
| Bislerp | 结合了双线性插值的简洁性和 sinc 函数插值的优点，实现了高质量的图像缩放，同时减少了失真与伪影。它在图像质量和计算成本之间取得了平衡。|

## 输入

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `samples` | `LATENT` | 要放大的图像的潜在表示，此参数是确定将经历放大过程的输入数据的关键。 |
| `upscale_method` | COMBO[STRING] | 指定用于放大潜在样本的方法。方法的选择可以显著影响放大输出的质量和特性。 |
| `scale_by` | `FLOAT` | 确定潜在样本放大的比例。此参数直接影响输出的分辨率，允许对放大过程进行精确控制。 |

## 输出

| 参数名称 | 数据类型 | 作用 |
| --- | --- | --- |
| `latent` | `LATENT` | 放大后的潜在表示，准备好进行进一步的处理或生成任务。此输出对于提高生成图像的分辨率或后续模型操作至关重要。 |

---

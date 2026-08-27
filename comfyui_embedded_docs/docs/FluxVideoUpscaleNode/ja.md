# FluxVideoUpscaleNode

Flux Video Upscaleは、FLUX超解像を使用してビデオクリップを1.5倍から3倍に拡大します。クリエイティブモードでは微細なディテールを復元・生成し、プレサイスモードではソースを変更せずにシャープにします。

## 入力

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `video` | 1秒から20秒のソースクリップで、アスペクト比が1:4から4:1の間である必要があります。出力は24 fpsでレンダリングされ、1フレームあたり約14.4メガピクセルに制限されます。 | VIDEO | Yes | 1 to 20 seconds duration; aspect ratio between 1:4 and 4:1; minimum 64x64 pixels |
| `upscale_factor` | ソースに対する出力サイズ。フレームごとの上限があるため、非常に大きなソースは要求された倍率よりも小さい倍率で拡大されます。（デフォルト: 2.0） | FLOAT | Yes | 1.5 to 3.0 (step 0.1) |
| `mode` | 'creative' は微細なディテールを復元・生成し、生成映像、テクスチャ、風景に最適です。'precise' はソースを変更せずにシャープにし、顔、製品、実写映像に適しています。（デフォルト: "creative"） | COMBO | Yes | "creative"<br>"precise" |
| `prompt` | 拡大されるディテールを方向付ける、クリップの任意の説明文。ニュートラルな拡大を行うには空のままにします。（デフォルト: 空） | STRING | Yes | Multiline text |
| `auto_downscale` | 入力制限に収まるように、面積が3840x2160ピクセルより大きいソースを自動的にダウンスケールします。アスペクト比は保持され、小さいビデオは変更されません。（デフォルト: true） | BOOLEAN | Yes | true<br>false |
| `safety_tolerance` | モデレーションの許容度で、0が最も厳格です。（デフォルト: 2、上級者向けパラメータ） | INT | Yes | 0 to 4 |
| `seed` | ノードを再実行するかどうかを決定するシード。FLUXが独自のシードを選択するため、この値に関係なく実際の結果は非決定的です。（デフォルト: 42） | INT | Yes | 0 to 4294967295 |

注：ソースビデオは1秒以上20秒以下で、サイズが少なくとも64x64ピクセルである必要があります。`auto_downscale` が無効で、ビデオの面積が3840x2160ピクセルを超える場合、ノードはエラーを発生させます。出力ビデオは24 fpsでレンダリングされ、1フレームあたり約14.4メガピクセルに制限されるため、非常に大きなソースは要求された倍率よりも小さい倍率で拡大される場合があります。

## 出力

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `video` | 拡大されたビデオクリップ。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/ja.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`

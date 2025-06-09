このノードは、主にCLIPテキストエンコーダーモデルを単独でロードするために使用されます。
モデルファイルは以下のパスで検出できます：

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> ComfyUI起動後にモデルを保存した場合、最新のモデルファイルパスリストを取得するためにComfyUIフロントエンドを更新する必要があります

サポートされているモデル形式：

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

最新のモデルファイルのロードについての詳細は[folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)を参照してください

## 入力

| パラメータ     | データ型 | 説明 |
|---------------|----------|------|
| `clip名`      | COMBO[STRING] | ロードするCLIPモデルの名前を指定します。この名前は、事前定義されたディレクトリ構造内でモデルファイルを見つけるために使用されます。 |
| `タイプ`      | COMBO[STRING] | ロードするCLIPモデルのタイプを決定します。ComfyUIがサポートするモデルが増えるにつれて、新しいタイプがここに追加されます。詳細については[node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)の`CLIPLoader`クラスの定義を参照してください。 |
| `デバイス`    | COMBO[STRING] | CLIPモデルをロードするデバイスを選択します。`default`はGPUでモデルを実行し、`CPU`を選択するとCPUでの強制ロードを行います。 |

### デバイスオプションの説明

**"default"を選択する場合：**

- 十分なGPUメモリがある
- 最高のパフォーマンスを求める
- システムにメモリ使用の最適化を任せる

**"cpu"を選択する場合：**

- GPUメモリが不足している
- 他のモデル（UNetなど）のためにGPUメモリを確保する必要がある
- 低VRAMの環境で実行する
- デバッグや特別な目的が必要

**パフォーマンスへの影響**

CPU上での実行はGPUよりもかなり遅くなりますが、他の重要なモデルコンポーネントのために貴重なGPUメモリを節約できます。メモリに制約のある環境では、CLIPモデルをCPUに配置することは一般的な最適化戦略です。

### サポートされている組み合わせ

| モデルタイプ | 対応するエンコーダー |
|-------------|-------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

ComfyUIの更新に伴い、これらの組み合わせは拡張される可能性があります。詳細については[node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)の`CLIPLoader`クラスの定義を参照してください。

## 出力

| パラメータ | データ型 | 説明 |
|-----------|----------|------|
| `clip`    | CLIP     | 下流のタスクやさらなる処理に使用するために準備されたロード済みのCLIPモデル。 |

## 補足説明

CLIPモデルはComfyUIでテキストエンコーダーとして重要な役割を果たし、テキストプロンプトを拡散モデルが理解できる数値表現に変換する責任があります。これを翻訳者のように考えることができ、テキストを大規模モデルが理解できる言語に翻訳する役割を担っています。もちろん、異なるモデルには独自の「方言」があるため、異なるアーキテクチャ間でテキストエンコーディングプロセスを完了するには、異なるCLIPエンコーダーが必要です。

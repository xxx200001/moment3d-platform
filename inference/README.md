# Inference — 单图 3D 推理服务

基于深度学习的单图 3D 高斯泼溅推理引擎，提供 RESTful API 和 SSE 实时进度推送。

## 功能

- 单张图片生成 3D Gaussian Splatting 表示
- FP16 半精度推理，显存占用减少 ~50%
- GPU 加速后处理（SVD / 四元数转换，快 10-20x）
- 自动压缩 .ply → .sog 格式
- SQLite 元数据存储（内参/外参矩阵）
- SSE 实时状态推送

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt
pip install -r requirements-api.txt

# 复制并编辑配置
cp config.template.jsonc config.jsonc

# 启动服务
python start_api.py
```

服务启动后：
- API 文档: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/predict` | 上传图片，创建推理任务 |
| GET | `/stream/{task_id}` | SSE 实时状态推送 |
| GET | `/status/{task_id}` | 查询任务状态 |
| GET | `/result/{task_id}` | 下载 .sog 结果文件 |
| GET | `/metadata/{task_id}` | 获取相机内参/外参 |

## 配置

编辑 `config.jsonc`：

- `model.device`: 计算设备 (`auto` / `cuda` / `mps` / `cpu`)
- `model.use_fp16`: 是否启用 FP16 推理
- `compression.enabled`: 是否自动压缩
- `storage.output_dir`: 输出目录

## 处理流程

```
上传图片 → 排队 → 推理转换 → 保存 PLY → 压缩 .sog → 完成
              queued    converting    converting   compressing  completed
```

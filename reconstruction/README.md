# Reconstruction — 视频 3D 重建服务

基于视频输入的全自动 3D 高斯泼溅重建流水线后端。

## 功能

- 视频上传 / OSS 拉取
- 自动化流水线：帧提取 → SfM → 高斯泼溅训练 → 压缩
- 多进程任务队列，各阶段独立 Worker
- SQLite 持久化 + 批量状态查询
- 重建结果上传至对象存储

## 快速开始

```bash
# 安装依赖
uv sync

# 复制并编辑配置
cp config.jsonc.example config.jsonc

# 启动服务
uv run python start_api.py
# ✅ Running on http://localhost:4000
```

## 依赖工具

- FFmpeg（CUDA 加速）
- COLMAP
- LichtFeld Studio

## API

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/upload` | 上传视频创建任务 |
| POST | `/tasks/from-oss` | 从 OSS 拉取视频 |
| GET | `/status/{task_id}` | 查询任务状态 |
| POST | `/status/batch` | 批量查询 |
| GET | `/tasks/{task_id}/assets` | 下载重建结果 |
| GET | `/tasks/{task_id}/metadata` | 获取相机参数 |
| POST | `/tasks/{task_id}/upload-to-oss` | 上传结果至 OSS |
| GET | `/queue/stats` | 队列统计 |

## 重建流水线

```
上传视频 → Waiting → Preprocessing → SfM → Reconstruction → Compress → Finish
                       (帧提取)     (稀疏重建)  (GS训练)      (SOG压缩)
```
# Moment3D

**定格瞬间，留住世界** — 将一张照片转化为沉浸式 3D 高斯泼溅场景。

上传一张普通照片，Moment3D 在数秒内将其重建为可交互的 3D 场景，支持视角旋转、粒子特效和实时渲染。

## ✨ 核心特性

- **单图 → 3D**: 一张照片即可生成高质量 3D 高斯泼溅表示
- **实时渲染**: 基于 WebGL 的浏览器端渲染，流畅交互
- **多种粒子效果**: Magic / Spread / Unroll / Twister / Rain 等 6 种视觉特效
- **SSE 实时进度**: 从上传到完成的全流程实时状态推送
- **移动端适配**: 自动检测设备，优化触控交互和渲染性能
- **GPU 加速推理**: FP16 半精度 + GPU 后处理，推理速度提升 10-20x

## 🏗️ 架构

```
┌─────────────┐    HTTP/SSE    ┌──────────────┐    Internal    ┌────────────────┐
│   Frontend  │ ◄────────────► │   Inference   │               │ Reconstruction │
│  Next.js 15 │   :3000→:8000  │   FastAPI     │               │   FastAPI       │
│  React 19   │                │   PyTorch     │               │   COLMAP + GS   │
│  Three.js   │                │   CUDA/MPS    │               │   LichtFeld     │
└─────────────┘                └──────────────┘               └────────────────┘
     :3000                          :8000                          :4000
```

| 模块 | 目录 | 职责 |
|------|------|------|
| **frontend** | `frontend/` | Web 前端，图片上传 / 3D 查看器 / 粒子效果 |
| **inference** | `inference/` | 单图推理 API，生成 3DGS 点云 (.ply → .sog) |
| **reconstruction** | `reconstruction/` | 视频重建流水线 (帧提取 → SfM → 训练 → 压缩) |

## 🚀 快速开始

### 环境要求

- Python 3.13+, PyTorch (CUDA)
- Node.js 18+
- NVIDIA GPU（推荐，CPU/MPS 也可运行）

### 1. 启动推理后端

```bash
cd inference
pip install -r requirements.txt -r requirements-api.txt
python start_api.py
# ✅ Running on http://localhost:8000
```

### 2. 启动前端

```bash
cd frontend
npm install
npm run dev
# ✅ Ready on http://localhost:3000
```

### 3. 使用

打开浏览器访问 `http://localhost:3000`，上传一张照片，等待数秒即可查看 3D 效果。

## 📡 外网访问

```bash
# 使用 Cloudflare Tunnel 暴露前端
cloudflared tunnel --url http://localhost:3000
```

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 前端框架 | Next.js 15 (Turbopack), React 19, TypeScript |
| 3D 渲染 | Three.js, React Three Fiber, Spark.js |
| 样式 | Tailwind CSS 4 |
| 推理引擎 | PyTorch, timm (ViT), gsplat |
| 后端框架 | FastAPI, Uvicorn |
| 点云压缩 | splat-transform (.ply → .sog) |
| 数据库 | SQLite (aiosqlite) |

## 📄 License

MIT License

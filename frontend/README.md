# Frontend — Moment3D Web 应用

基于 Next.js 15 的 3D 高斯泼溅查看器，支持图片上传、实时进度追踪和沉浸式 3D 交互。

## 功能

- 📸 拖拽 / 点击上传图片（支持 JPG、PNG）
- ⚡ SSE 实时进度推送（上传 → 排队 → 重建 → 压缩）
- 🎨 6 种粒子特效（Magic / Spread / Unroll / Twister / Rain / 无效果）
- 📱 移动端自适应，触控交互优化
- 🎮 交互操作教程（PC / 移动端）

## 技术栈

- **Next.js 15** (Turbopack) + **React 19** + **TypeScript**
- **Three.js** + **React Three Fiber** — 3D 渲染
- **Spark.js** — 高斯泼溅渲染器
- **Framer Motion** — 动画
- **Tailwind CSS 4** — 样式

## 开发

```bash
# 安装依赖
npm install

# 配置后端地址
cp .env.local.example .env.local
# 编辑 BACKEND_URL=http://localhost:8000

# 启动开发服务器
npm run dev
```

访问 http://localhost:3000

## 项目结构

```
app/
├── (home)/                      # 首页（图片上传）
├── viewer/[taskId]/             # 3D 查看器
├── api/                         # API 代理层
│   ├── predict/                 # 图片上传代理
│   ├── stream/[taskId]/         # SSE 状态推送代理
│   ├── result/[taskId]/         # 结果文件代理
│   └── metadata/[taskId]/       # 元数据代理
└── _components/                 # 共享组件
    ├── splat-scene.tsx          # 3D 场景
    ├── splat-effects.ts         # 粒子效果
    └── interaction-tutorial.tsx # 操作教程
```

## 构建部署

```bash
npm run build     # 生产构建
npm run package   # 构建并打包 ZIP
```
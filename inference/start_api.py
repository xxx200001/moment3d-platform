"""快速启动 SHARP API 服务的脚本"""

import logging
import sys
from pathlib import Path

import uvicorn

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    # 检查配置文件
    config_file = Path("config.jsonc")
    if not config_file.exists():
        print("⚠️  未找到 config.jsonc，将使用默认配置")
        print("   提示: 复制 config.template.jsonc 为 config.jsonc 并修改配置")
        print("   命令: cp config.template.jsonc config.jsonc\n")
    
    # 加载配置
    from sharp.api.config import get_config
    config = get_config()
    
    # 命令行参数覆盖
    port = int(sys.argv[1]) if len(sys.argv) > 1 else config.server.port
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║         Moment3D Inference API 服务            ║
╚══════════════════════════════════════════════════════════╝

🚀 服务启动中...
📍 地址: http://{config.server.host}:{port}
📖 API 文档: http://localhost:{port}/docs
📚 ReDoc: http://localhost:{port}/redoc

⚙️  配置信息:
   设备: {config.model.device}
   输出目录: {config.storage.output_dir}
   压缩: {'启用' if config.compression.enabled else '禁用'}
   压缩 Workers: {config.compression.max_workers if config.compression.enabled else 'N/A'}
   保留 PLY: {'是' if config.storage.keep_ply else '否'}

💡 提示: 
   - 模型将在首次请求时自动下载和加载
   - config.json 支持 JSONC 格式（可以包含注释）
    """)
    
    uvicorn.run(
        "sharp.api.server:app",
        host=config.server.host,
        port=port,
        reload=False,
        log_level=config.server.log_level.lower()
    )

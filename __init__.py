"""
Simple Translate Node for ComfyUI
"""

from .simple_translate import SimpleTranslate

# 导出节点
NODE_CLASS_MAPPINGS = {
    "SimpleTranslate": SimpleTranslate
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTranslate": "简单翻译"
}
